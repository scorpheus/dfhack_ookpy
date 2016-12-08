__author__ = 'scorpheus'

from dfhack_connect import *
import gs
import threading
from collections import OrderedDict
import random


plus = gs.GetPlus()
geos = None

map_info = None
tile_type_list = None
material_list = None
building_geos = None
tile_geos = None
dwarf_geo = None
cube_geo_big_block = None
mats_path = ["empty.mat", "floor.mat", "magma.mat", "rock.mat", "water.mat", "tree.mat", "floor.mat", "floor.mat"]

scale_unit_y = 1.0
visible_area_length = 15


def from_world_to_dfworld(new_pos):
	return gs.Vector3(new_pos.x, new_pos.z, new_pos.y)


def from_dfworld_to_world(new_pos):
	return gs.Vector3(new_pos.x, new_pos.z, new_pos.y)


size_big_block = gs.Vector3(16 * 1, 3, 16 * 1)
array_world_big_block = {}


cache_block = {}


class building_type():
	NONE = -1
	Chair, Bed, Table, Coffin, FarmPlot, Furnace, TradeDepot, Shop, Door, Floodgate, Box, Weaponrack, \
	Armorstand, Workshop, Cabinet, Statue, WindowGlass, WindowGem, Well, Bridge, RoadDirt, RoadPaved, SiegeEngine, \
	Trap, AnimalTrap, Support, ArcheryTarget, Chain, Cage, Stockpile, Civzone, Weapon, Wagon, ScrewPump, \
	Construction, Hatch, GrateWall, GrateFloor, BarsVertical, BarsFloor, GearAssembly, AxleHorizontal, AxleVertical, \
	WaterWheel, Windmill, TractionBench, Slab, Nest, NestBox, Hive, Rollers = range(51)


def hash_from_pos(x, y, z):
	return x + y * 2048 + z * 2048**2


def setup():
	global map_info, tile_type_list, material_list, tile_geos, geos, building_geos, dwarf_geo, cube_geo_big_block

	connect_socket()
	handshake()
	# dfversion = get_df_version()
	map_info = get_map_info()
	reset_map_hashes()

	# get once to use after (material list is huge)
	tile_type_list = get_tiletype_list()
	# material_list = get_material_list()

	# dwarf_geo = plus.CreateGeometry(plus.CreateCube(0.1, 0.6, 0.1, "iso.mat"))
	dwarf_geo = plus.LoadGeometry("minecraft_assets/default_dwarf/default_dwarf.geo")
	cube_geo_big_block = plus.CreateGeometry(plus.CreateCube(size_big_block.x, size_big_block.y*0.5*scale_unit_y, size_big_block.z, "iso.mat"))


	geos = [plus.LoadGeometry("environment_kit_inca/stone_high_03.geo"), plus.LoadGeometry("environment_kit_inca/stone_high_01.geo")]
	building_geos = {building_type.Chair: None, building_type.Bed: None,
					 building_type.Table: {'g': plus.LoadGeometry("environment_kit/geo-table.geo"), 'o': gs.Matrix4.Identity},
					 building_type.Coffin: None, building_type.FarmPlot: None, building_type.Furnace: None,
					 building_type.TradeDepot: None, building_type.Shop: None,
					 building_type.Door: {'g': plus.LoadGeometry("environment_kit/geo-door.geo"), 'o': gs.Matrix4.Identity},
					 building_type.Floodgate: None,
					 building_type.Box: {'g': plus.LoadGeometry("environment_kit_inca/chest_top.geo"), 'o': gs.Matrix4.Identity},
					 building_type.Weaponrack: None,
					 building_type.Armorstand: None, building_type.Workshop: None,
					 building_type.Cabinet: {'g': plus.LoadGeometry("environment_kit/geo-bookshelf.geo"), 'o': gs.Matrix4.Identity},
					 building_type.Statue: {'g': plus.LoadGeometry("environment_kit/geo-greece_column.geo"), 'o': gs.Matrix4.RotationMatrix(gs.Vector3(-1.57, 0, 0))},
					 building_type.WindowGlass: None, building_type.WindowGem: None,
					 building_type.Well: None, building_type.Bridge: None, building_type.RoadDirt: None,
					 building_type.RoadPaved: None, building_type.SiegeEngine: None, building_type.Trap: None,
					 building_type.AnimalTrap: None, building_type.Support: None, building_type.ArcheryTarget: None,
					 building_type.Chain: None, building_type.Cage: None, building_type.Stockpile: None,
					 building_type.Civzone: None,
					 building_type.Weapon: None, building_type.Wagon: None, building_type.ScrewPump: None,
					 building_type.Construction: {'g': plus.LoadGeometry("environment_kit/geo-egypt_wall.geo"), 'o': gs.Matrix4.Identity},
					 building_type.Hatch: None, building_type.GrateWall: None, building_type.GrateFloor: None,
					 building_type.BarsVertical: None,
					 building_type.BarsFloor: None, building_type.GearAssembly: None,
					 building_type.AxleHorizontal: None, building_type.AxleVertical: None,
					 building_type.WaterWheel: None, building_type.Windmill: None, building_type.TractionBench: None,
					 building_type.Slab: None, building_type.Nest: None, building_type.NestBox: None,
					 building_type.Hive: None, building_type.Rollers: None}

	# precompile material
	tile_geos = []
	for mat in mats_path:
		tile_geos.append(plus.CreateGeometry(plus.CreateCube(0.8, 0.8*scale_unit_y, 0.8, mat)))


def parse_block(fresh_block, big_block):
	world_block_pos = from_dfworld_to_world(gs.Vector3(fresh_block.map_x, fresh_block.map_y, fresh_block.map_z))

	x, z = 0, 0
	for tile, magma, water, material in zip(fresh_block.tiles, fresh_block.magma, fresh_block.water, fresh_block.materials):
		if tile != 0:
			type = tile_type_list.tiletype_list[tile]

			# choose a material
			block_mat = 0
			if magma > 0:
				block_mat = 2
			elif water > 0:
				block_mat = 4
			elif type.shape == remote_fortress.FLOOR:
				block_mat = 1
			elif type.shape == remote_fortress.RAMP:
				block_mat = 6
			elif type.shape == remote_fortress.RAMP_TOP:
				block_mat = 7
			elif type.shape == remote_fortress.BOULDER:
				block_mat = 3
				# array_props.append((gs.Vector3(block_pos.x*16 + x, block_pos.y, block_pos.z*16 + z), 0))
			elif type.shape == remote_fortress.PEBBLES:
				block_mat = 3
				# array_props.append((gs.Vector3(block_pos.x*16 + x, block_pos.y, block_pos.z*16 + z), 1))
			elif type.shape == remote_fortress.WALL or type.shape == remote_fortress.FORTIFICATION:
				block_mat = 3
			# if type.material == remote_fortress.PLANT:
			# 	block_mat = 2
			elif type.shape == remote_fortress.SHRUB or type.shape == remote_fortress.SAPLING:
				block_mat = 1

			if type.material == remote_fortress.TREE_MATERIAL or type.shape == remote_fortress.TRUNK_BRANCH or\
				type.shape == remote_fortress.TWIG:
				block_mat = 5

			# if it's not air, add it to draw it
			tile_pos = gs.Vector3(world_block_pos.x + x, world_block_pos.y, world_block_pos.z + z)
			id_tile = hash_from_pos(tile_pos.x, tile_pos.y, tile_pos.z)
			if block_mat != 0:
				# big_block["blocks"][id_tile] = {"m": gs.Matrix4.TranslationMatrix(tile_pos), "mat": block_mat} # perfect grid
				big_block["blocks"][id_tile] = {"m": gs.Matrix4.TransformationMatrix(tile_pos, gs.Vector3(random.random()*0.2-0.1, random.random()*0.2-0.1, random.random()*0.2-0.1)), "mat": block_mat} # with rumble
			else:
				if id_tile in big_block["blocks"]:
					del big_block["blocks"][id_tile]

			# add props
			# if building != -1:
			# 	array_building.append((gs.Vector3(block_pos.x*16 + x, block_pos.y, block_pos.z*16 + z), building))

		x += 1
		if x > 15:
			x = 0
			z += 1


def get_viewing_min_max(cam):
	vecs = [cam.GetTransform().GetPosition() + cam.GetTransform().GetWorld().GetX() * visible_area_length + cam.GetTransform().GetWorld().GetY() * visible_area_length - cam.GetTransform().GetWorld().GetZ() * 1,
	        cam.GetTransform().GetPosition() + cam.GetTransform().GetWorld().GetX() * visible_area_length - cam.GetTransform().GetWorld().GetY() * visible_area_length - cam.GetTransform().GetWorld().GetZ() * 1,
	        cam.GetTransform().GetPosition() - cam.GetTransform().GetWorld().GetX() * visible_area_length + cam.GetTransform().GetWorld().GetY() * visible_area_length - cam.GetTransform().GetWorld().GetZ() * 1,
	        cam.GetTransform().GetPosition() - cam.GetTransform().GetWorld().GetX() * visible_area_length - cam.GetTransform().GetWorld().GetY() * visible_area_length - cam.GetTransform().GetWorld().GetZ() * 1,

	        cam.GetTransform().GetPosition() + cam.GetTransform().GetWorld().GetX() * visible_area_length + cam.GetTransform().GetWorld().GetY() * visible_area_length + cam.GetTransform().GetWorld().GetZ() * visible_area_length,
	        cam.GetTransform().GetPosition() + cam.GetTransform().GetWorld().GetX() * visible_area_length - cam.GetTransform().GetWorld().GetY() * visible_area_length + cam.GetTransform().GetWorld().GetZ() * visible_area_length,
	        cam.GetTransform().GetPosition() - cam.GetTransform().GetWorld().GetX() * visible_area_length + cam.GetTransform().GetWorld().GetY() * visible_area_length + cam.GetTransform().GetWorld().GetZ() * visible_area_length,
	        cam.GetTransform().GetPosition() - cam.GetTransform().GetWorld().GetX() * visible_area_length - cam.GetTransform().GetWorld().GetY() * visible_area_length + cam.GetTransform().GetWorld().GetZ() * visible_area_length
	        ]

	def get_min_max(a, b):
		if a < b:
			return a, b
		else:
			return b, a

	pos_min = gs.Vector3(vecs[0])
	pos_max = gs.Vector3(vecs[0])
	for vec in vecs:
		pos_min.x, temp = get_min_max(pos_min.x, vec.x)
		temp, pos_max.x = get_min_max(pos_max.x, vec.x)
		
		pos_min.y, temp = get_min_max(pos_min.y, vec.y)
		temp, pos_max.y = get_min_max(pos_max.y, vec.y)
		
		pos_min.z, temp = get_min_max(pos_min.z, vec.z)
		temp, pos_max.z = get_min_max(pos_max.z, vec.z)

	return pos_min, pos_max


class UpdateBigBlock(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.big_block = None

	def run(self):
		fresh_blocks = get_block_list(from_world_to_dfworld(self.big_block["min"]), from_world_to_dfworld(self.big_block["min"] + size_big_block))
		for fresh_block in fresh_blocks.map_blocks:
			parse_block(fresh_block, self.big_block)
		self.big_block["to_update"] = False

big_block_thread = UpdateBigBlock()


def update_block(cam):
	global big_block_thread

	if not big_block_thread.is_alive():
		p_min, p_max = get_viewing_min_max(cam)

		# grow the array_big_block
		for x in range(int(p_min.x // size_big_block.x) - 1, int(p_max.x // size_big_block.x) + 1):
			for y in range(int(p_min.y // size_big_block.y) - 1, int(p_max.y // size_big_block.y) + 1):
				for z in range(int(p_min.z // size_big_block.z) - 1, int(p_max.z // size_big_block.z) + 1):
					id = hash_from_pos(x, y, z)
					if id not in array_world_big_block:
						array_world_big_block[id] = {"min": gs.Vector3(x, y, z) * size_big_block, "blocks": {}, "to_update": 1, "time": 1000}

		pos_in_front = cam.GetTransform().GetPosition() + cam.GetTransform().GetWorld().GetZ() * 8
		ordered_array_world_big_block = OrderedDict(sorted(array_world_big_block.items(), key=lambda t: ((t[1]["min"].x - pos_in_front.x) // size_big_block.x) ** 2 + ((((t[1]["min"].y - pos_in_front.y) // size_big_block.y)/2) / scale_unit_y) ** 2 + ((t[1]["min"].z - pos_in_front.z) // size_big_block.x) ** 2))

		# find a block to update
		for id, big_block in ordered_array_world_big_block.items():
			if big_block["to_update"] == 1:# and p_min.x < big_block["min"].x < p_max.x and p_min.y < big_block["min"].y < p_max.y and p_min.z < big_block["min"].z < p_max.z:
				big_block["to_update"] = 2

				big_block_thread = UpdateBigBlock()
				big_block_thread.big_block = big_block
				big_block_thread.start()
				break


def draw_block(renderable_system, cam):
	p_min, p_max = get_viewing_min_max(cam)
	count_draw = 0
	# grow the array_big_block
	for x in range(int(p_min.x // size_big_block.x) - 1, int(p_max.x // size_big_block.x) + 1):
		for y in range(int(p_min.y // size_big_block.y) - 1, int(p_max.y // size_big_block.y) + 1):
			for z in range(int(p_min.z // size_big_block.z) - 1, int(p_max.z // size_big_block.z) + 1):
				id = hash_from_pos(x, y, z)
				if id in array_world_big_block:
					big_block = array_world_big_block[id]
					if not big_block["to_update"]:
						for id, block in big_block["blocks"].items():
							renderable_system.DrawGeometry(tile_geos[block["mat"]], block["m"])
							count_draw += 1
						# renderable_system.DrawGeometry(cube_geo_big_block, gs.Matrix4.TranslationMatrix(big_block["min"] + size_big_block * 0.5))
	return count_draw
