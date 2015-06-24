__author__ = 'scorpheus'

from dfhack_connect import *
import gs
import gs.plus.render as render
import gs.plus.input as input
import gs.plus.scene as scene
import gs.plus.camera as camera
import gs.plus.clock as clock
import gs.plus.geometry as geometry
import geometry_iso
import math

from collections import OrderedDict
import threading
import numpy as np


scale_unit_y = 2.0


def from_world_to_dfworld(new_pos):
	return gs.Vector3(new_pos.x, new_pos.z, new_pos.y)


try:
	connect_socket()
	Handshake()
	ResetMapHashes()
	# dfversion = GetDFVersion()
	map_info = GetMapInfo()

	# get once to use after (material list is huge)
	tile_type_list = GetTiletypeList()
	# material_list = GetMaterialList()

	render.init(1920, 1080, "pkg.core")
	gs.MountFileDriver(gs.StdFileDriver("."))

	scn = scene.new_scene()
	# add lua system
	engine_env = gs.ScriptEngineEnv(render.get_render_system_async(), render.get_renderer_async(), None)

	lua_system = gs.LuaSystem(engine_env)
	lua_system.SetExecutionContext(gs.ScriptContextAll )
	lua_system.Open()
	scn.AddSystem(lua_system)

	scn.Load('@core/scene_templates/scene.scn', gs.SceneLoadContext(render.get_render_system()))
	light_cam = scene.add_light(scn, gs.Matrix4.TranslationMatrix(gs.Vector3(6, 200, -6)))
	light_cam.light.SetShadow(gs.Light.Shadow_None)
	cam = scene.add_camera(scn, gs.Matrix4.TranslationMatrix(gs.Vector3(112, 62, 112)))
	cam.camera.SetZoomFactor(gs.FovToZoomFactor(1.57))

	fps = camera.fps_controller(128, 72*scale_unit_y, 64)
	fps.rot = gs.Vector3(0.5, 0, 0)

	dwarf_geo = render.create_geometry(geometry.create_cube(0.1, 0.6, 0.1, "iso.mat"))

	pos = gs.Vector3(112//16, 62, 112//16)


	def hash_from_pos(x, y, z):
		return x + y * 2048 + z * 2048 * 2048


	def hash_from_layer(layer_pos, x, z):
		return hash_from_pos(layer_pos.x + x - (layer_size - 1) / 2, layer_pos.y, layer_pos.z + z - (layer_size - 1) / 2)


	block_fetched = 0
	layer_size = 5
	cache_block = {}
	cache_block_props = {}
	cache_block_mat = {}
	cache_geo_block = {}
	update_cache_block = {}
	update_cache_geo_block = {}
	current_update_get_block_threads = [None] * 2
	current_update_create_geo_threads = [None] * 1

	old_pos = gs.Vector3()

	mats_path = ["empty.mat", "floor.mat", "magma.mat", "rock.mat", "water.mat", "tree.mat"]
	geos = [render.load_geometry("environment_kit/geo-boulder.geo")]

	def get_block_simple(new_pos):
		_pos = gs.Vector3(new_pos)
		_pos.x = map_info.block_size_x - _pos.x
		_pos.x *= 16
		_pos.z *= 16

		# import time
		# first = time.time()

		block = GetBlock(from_world_to_dfworld(_pos))

		# print("get : %f" % (time.time() - first))

		array_has_geo = np.full((17, 17), 0, np.int8)
		array_tile_mat_id = np.full((17, 17), 0, np.int8)
		array_props = []

		if len(block.tile) > 0:
			x, z = 15, 0
			count_liquid = 0
			count_flow_size = 0
			for tile in block.tile:
				if tile != 0:
					type = tile_type_list.tiletype_list[tile]

					# choose a material
					block_mat = 0
					if block.flow_size[count_flow_size] > 0:
						if block.liquid_type[count_liquid] == Tile.Tile.MAGMA:
							block_mat = 2
						elif block.liquid_type[count_liquid] == Tile.Tile.WATER:
							block_mat = 4
						count_liquid += 1
						array_has_geo[x, z] = 1
					elif type.shape == remote_fortress.FLOOR:
						block_mat = 1
						array_has_geo[x, z] = 0
					elif type.shape == remote_fortress.BOULDER or type.shape == remote_fortress.PEBBLES:
						block_mat = 3
						array_has_geo[x, z] = 0
						array_props.append((gs.Vector3(new_pos.x*16 + x, new_pos.y, new_pos.z*16 + z), 0))
					elif type.shape == remote_fortress.WALL or type.shape == remote_fortress.FORTIFICATION:
						block_mat = 3
						array_has_geo[x, z] = 1
					# if type.material == remote_fortress.PLANT:
					# 	block_mat = 2
					elif type.shape == remote_fortress.SHRUB or type.shape == remote_fortress.SAPLING:
						block_mat = 1
						array_has_geo[x, z] = 0

					if type.material == remote_fortress.TREE_MATERIAL or type.shape == remote_fortress.TRUNK_BRANCH:
						block_mat = 0
						array_has_geo[x, z] = 0

					array_tile_mat_id[x, z] = block_mat
					count_flow_size += 1

				x -= 1
				if x < 0:
					x = 15
					z += 1


		array_has_geo[:, -1] = array_has_geo[:, -2]
		array_has_geo[-1, :] = array_has_geo[-2, :]

		array_tile_mat_id[:, -1] = array_tile_mat_id[:, -2]
		array_tile_mat_id[-1, :] = array_tile_mat_id[-2, :]

		return array_has_geo, array_tile_mat_id, array_props

	class UpdateCreateGeo(threading.Thread):
		def __init__(self, current_layer_block_name, upper_layer_block_name):
			threading.Thread.__init__(self)
			self.current_layer_block_name, self.upper_layer_block_name = current_layer_block_name, upper_layer_block_name

		def run(self):
			cache_geo_block[self.current_layer_block_name] = get_geo_from_blocks(self.current_layer_block_name, self.upper_layer_block_name, cache_block[self.current_layer_block_name], cache_block[self.upper_layer_block_name])


	class UpdateBlockFromDF(threading.Thread):
		def __init__(self, name_block, new_pos):
			threading.Thread.__init__(self)
			self.name_block = name_block
			self.block = None
			self.block_mat_id = None
			self.block_props = None
			self.pos = gs.Vector3(new_pos)

		def run(self):
			self.block, self.block_mat_id, self.block_props = get_block_simple(self.pos)


	class UpdateUnitListFromDF(threading.Thread):
		def __init__(self):
			threading.Thread.__init__(self)
			self.unit_list = None

		def run(self):
			self.unit_list = GetListUnits()

	block_drawn = 0
	props_drawn = 0
	unit_list_thread = UpdateUnitListFromDF()
	unit_list_thread.run()

	def draw_geo_block(geo_block, x, y, z):
		x *= 16
		z *= 16

		scn.renderable_system.DrawGeometry(geo_block, gs.Matrix4.TranslationMatrix(gs.Vector3(x+1, y*scale_unit_y, z)) * gs.Matrix4.ScaleMatrix(gs.Vector3(1, scale_unit_y, 1)))

		global block_drawn
		block_drawn += 1

	def draw_props_in_block(name_block):
		for prop in cache_block_props[name_block]:
			scn.renderable_system.DrawGeometry(geos[prop[1]], gs.Matrix4.TransformationMatrix(gs.Vector3(prop[0].x+1, prop[0].y*scale_unit_y, prop[0].z), gs.Vector3(name_block%5, name_block%4, name_block%3)))
			global props_drawn
			props_drawn += 1

	class Layer:
		def __init__(self):
			self.pos = gs.Vector3()

		def update(self, new_pos):
			self.pos = gs.Vector3(new_pos)

		def fill(self):
			global update_cache_block

			block_pos = gs.Vector3()
			block_pos.x = self.pos.x - (layer_size - 1) / 2
			block_pos.y = self.pos.y
			block_pos.z = self.pos.z - (layer_size - 1) / 2

			for z in range(layer_size):
				for x in range(layer_size):
					name_block = hash_from_layer(self.pos, x, z)
					if name_block not in cache_block and name_block not in update_cache_block:
						update_cache_block[name_block] = gs.Vector3(block_pos)

					block_pos.x += 1
				block_pos.x -= layer_size
				block_pos.z += 1
			return False

		def draw(self):
			for z in range(layer_size):
				for x in range(layer_size):
					name_block = hash_from_layer(self.pos, x, z)
					if name_block in cache_geo_block:
						pos_block_x, pos_block_y, pos_block_z = self.pos.x + x - (layer_size - 1) / 2, self.pos.y, self.pos.z + z - (layer_size - 1) / 2
						draw_geo_block(cache_geo_block[name_block], pos_block_x, pos_block_y, pos_block_z)
						draw_props_in_block(name_block)


	layers = []
	for i in range(20):
		layers.append(Layer())

	def get_cache_block_needed():
		global block_fetched
		global update_cache_block
		count = 0
		for update_thread in current_update_get_block_threads:
			if update_thread is not None:
				if not update_thread.is_alive():
					name_block = update_thread.name_block
					block_pos = update_thread.pos
					current_block = cache_block[name_block] = update_thread.block
					current_block_mat = cache_block_mat[name_block] = update_thread.block_mat_id
					cache_block_props[name_block] = update_thread.block_props

					current_update_get_block_threads[count] = None

					# update neighbour array
					north_name = hash_from_pos(block_pos.x, block_pos.y, block_pos.z-1)
					if north_name in cache_block:
						cache_block[north_name][:, -1] = current_block[:, 0]
						cache_block_mat[north_name][:, -1] = current_block_mat[:, 0]
					south_name = hash_from_pos(block_pos.x, block_pos.y, block_pos.z+1)
					if south_name in cache_block:
						current_block[:, -1] = cache_block[south_name][:, 0]
						current_block_mat[:, -1] = cache_block_mat[south_name][:, 0]
					west_name = hash_from_pos(block_pos.x-1, block_pos.y, block_pos.z)
					if west_name in cache_block:
						cache_block[west_name][-1, :] = current_block[0, :]
						cache_block_mat[west_name][-1, :] = current_block_mat[0, :]
					east_name = hash_from_pos(block_pos.x+1, block_pos.y, block_pos.z)
					if east_name in cache_block:
						current_block[-1, :] = cache_block[east_name][0, :]
						current_block_mat[-1, :] = cache_block_mat[east_name][0, :]

					# this block array is setup, ask the update the geo block
					update_cache_geo_block[name_block] = gs.Vector3(block_pos)
					update_cache_block.pop(name_block)
					block_fetched += 1

			elif len(update_cache_block) > count:
				ordered_update_cache_block = OrderedDict(sorted(update_cache_block.items(), key=lambda t: gs.Vector3.Dist2(gs.Vector3(t[1].x, t[1].y, t[1].z), pos)))

				iter_update_block = iter(ordered_update_cache_block.items())
				name_block, block_pos = None, None
				for i in range(count + 1):
					name_block, block_pos = next(iter_update_block)

				update_thread = UpdateBlockFromDF(name_block, block_pos)
				update_thread.run()
				current_update_get_block_threads[count] = update_thread

			count += 1

	def update_geo_block():
		global update_cache_geo_block
		count = 0
		for update_thread in current_update_create_geo_threads:
			if update_thread is not None:
				if not update_thread.is_alive():
					update_cache_geo_block.pop(update_thread.current_layer_block_name)
					current_update_create_geo_threads[count] = None

			elif len(update_cache_geo_block) > count:
				ordered_update_cache_geo = OrderedDict(sorted(update_cache_geo_block.items(), key=lambda t: gs.Vector3.Dist2(gs.Vector3(t[1].x, t[1].y, t[1].z), pos)))

				for name_block, block_pos in ordered_update_cache_geo.items():
					current_layer_block_name = hash_from_pos(block_pos.x, block_pos.y, block_pos.z)
					upper_layer_block_name = hash_from_pos(block_pos.x, block_pos.y + 1, block_pos.z)

					if current_layer_block_name in cache_block and upper_layer_block_name in cache_block:
						def check_block_can_generate_geo(x, y, z):
							# can update the geo block because it has all the neighbour
							counter_update = 0
							if hash_from_pos(x, y, z-1) in cache_block:
								counter_update += 1
							if hash_from_pos(x, y, z+1) in cache_block:
								counter_update += 1
							if hash_from_pos(x - 1, y, z) in cache_block:
								counter_update += 1
							if hash_from_pos(x + 1, y, z) in cache_block:
								counter_update += 1
							return counter_update == 4

						if check_block_can_generate_geo(block_pos.x, block_pos.y, block_pos.z) and check_block_can_generate_geo(block_pos.x, block_pos.y + 1, block_pos.z):
							update_thread = UpdateCreateGeo(current_layer_block_name, upper_layer_block_name)
							update_thread.run()
							current_update_create_geo_threads[count] = update_thread
							break

			count += 1

	def get_geo_from_blocks(name_geo, upper_name_block, block, upper_block):
		array_has_geo = np.empty((17, 2, 17), np.int8)
		array_has_geo[:, 0, :] = block
		array_has_geo[:, 1, :] = upper_block

		array_mats = np.empty((17, 2, 17), np.int8)
		array_mats[:, 0, :] = cache_block_mat[name_geo]
		array_mats[:, 1, :] = cache_block_mat[upper_name_block]

		return geometry_iso.create_iso(array_has_geo, 17, 2, 17, array_mats, 0.5, mats_path, name_geo)

	while not input.key_press(gs.InputDevice.KeyEscape):
		render.clear()

		dt_sec = clock.update()
		fps.update_and_apply_to_node(cam, dt_sec)
		light_cam.transform.SetPosition(fps.pos)

		# pos -> blocks dans lequel on peux se deplacer
		pos.x = fps.pos.x // 16
		pos.y = fps.pos.y // scale_unit_y
		pos.z = fps.pos.z // 16

		#
		if pos.y > old_pos.y:
			for i in range(len(layers) - 1):
				layers[i] = layers[i + 1]
			layers[-1] = Layer()
		elif pos.y < old_pos.y:
			for i in range(len(layers) - 1, 0, -1):
				layers[i] = layers[i - 1]
			layers[0] = Layer()

		old_pos = gs.Vector3(pos)

		#
		block_fetched, block_drawn, props_drawn = 0, 0, 0

		for i, layer in enumerate(layers):
			layer.update(pos + gs.Vector3(0, i - len(layers) // 2, 0))
			layer.fill()
			layer.draw()

		get_cache_block_needed()
		update_geo_block()

		# update unit draw
		if not unit_list_thread.is_alive():
			for unit in unit_list_thread.unit_list.value:
				scn.renderable_system.DrawGeometry(dwarf_geo, gs.Matrix4.TranslationMatrix(gs.Vector3(map_info.block_size_x*16 - unit.pos_x+16, (unit.pos_z+0.3)*scale_unit_y, unit.pos_y)))
			unit_list_thread.run()

		render.text2d(0, 45, "FPS: %.2fHZ - BLOCK FETCHED: %d - BLOCK DRAWN: %d - PROPS DRAWN: %d" % (1 / dt_sec, block_fetched, block_drawn, props_drawn), color=gs.Color.Red)
		render.text2d(0, 25, "FPS.X = %f, FPS.Z = %f" % (fps.pos.x, fps.pos.z), color=gs.Color.Red)
		render.text2d(0, 5, "POS.X = %f, POS.Y = %f, POS.Z = %f" % (pos.x, pos.y, pos.z), color=gs.Color.Red)

		scene.update_scene(scn, dt_sec)
		render.flip()

finally:
	close_socket()

