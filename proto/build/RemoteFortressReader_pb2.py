# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RemoteFortressReader.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
import sys
if sys.version_info >= (3,):
  #some constants that are python2 only
  unicode = str
  long = int
  range = range
  unichr = chr
  def b(s):
    return s.encode("latin-1")
  def u(s):
    return s
else:
  #some constants that are python2 only
  range = xrange
  unicode = unicode
  long = long
  unichr = unichr
  def b(s):
    return s
  # Workaround for standalone backslash
  def u(s):
    return unicode(s.replace(r'\\', r'\\\\'), "unicode_escape")

from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='RemoteFortressReader.proto',
  package='RemoteFortressReader',
  serialized_pb=b('\n\x1aRemoteFortressReader.proto\x12\x14RemoteFortressReader\"\xa6\x02\n\x08Tiletype\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07\x63\x61ption\x18\x03 \x01(\t\x12\x32\n\x05shape\x18\x04 \x01(\x0e\x32#.RemoteFortressReader.TiletypeShape\x12\x36\n\x07special\x18\x05 \x01(\x0e\x32%.RemoteFortressReader.TiletypeSpecial\x12\x38\n\x08material\x18\x06 \x01(\x0e\x32&.RemoteFortressReader.TiletypeMaterial\x12\x36\n\x07variant\x18\x07 \x01(\x0e\x32%.RemoteFortressReader.TiletypeVariant\x12\x11\n\tdirection\x18\x08 \x01(\r\"E\n\x0cTiletypeList\x12\x35\n\rtiletype_list\x18\x01 \x03(\x0b\x32\x1e.RemoteFortressReader.Tiletype\"x\n\x08MapBlock\x12\r\n\x05map_x\x18\x01 \x02(\x05\x12\r\n\x05map_y\x18\x02 \x02(\x05\x12\r\n\x05map_z\x18\x03 \x02(\x05\x12\r\n\x05tiles\x18\x04 \x03(\x05\x12\x30\n\tmaterials\x18\x05 \x03(\x0b\x32\x1d.RemoteFortressReader.MatPair\".\n\x07MatPair\x12\x10\n\x08mat_type\x18\x01 \x02(\x05\x12\x11\n\tmat_index\x18\x02 \x02(\x05\";\n\x0f\x43olorDefinition\x12\x0b\n\x03red\x18\x01 \x02(\x05\x12\r\n\x05green\x18\x02 \x02(\x05\x12\x0c\n\x04\x62lue\x18\x03 \x02(\x05\"\x9b\x01\n\x12MaterialDefinition\x12/\n\x08mat_pair\x18\x01 \x02(\x0b\x32\x1d.RemoteFortressReader.MatPair\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12:\n\x0bstate_color\x18\x04 \x01(\x0b\x32%.RemoteFortressReader.ColorDefinition\"O\n\x0cMaterialList\x12?\n\rmaterial_list\x18\x01 \x03(\x0b\x32(.RemoteFortressReader.MaterialDefinition\"\x7f\n\x0c\x42lockRequest\x12\x15\n\rblocks_needed\x18\x01 \x01(\x05\x12\r\n\x05min_x\x18\x02 \x01(\x05\x12\r\n\x05max_x\x18\x03 \x01(\x05\x12\r\n\x05min_y\x18\x04 \x01(\x05\x12\r\n\x05max_y\x18\x05 \x01(\x05\x12\r\n\x05min_z\x18\x06 \x01(\x05\x12\r\n\x05max_z\x18\x07 \x01(\x05\"]\n\tBlockList\x12\x32\n\nmap_blocks\x18\x01 \x03(\x0b\x32\x1e.RemoteFortressReader.MapBlock\x12\r\n\x05map_x\x18\x02 \x01(\x05\x12\r\n\x05map_y\x18\x03 \x01(\x05\"F\n\x08PlantDef\x12\r\n\x05pos_x\x18\x01 \x02(\x05\x12\r\n\x05pos_y\x18\x02 \x02(\x05\x12\r\n\x05pos_z\x18\x03 \x02(\x05\x12\r\n\x05index\x18\x04 \x02(\x05\"?\n\tPlantList\x12\x32\n\nplant_list\x18\x01 \x03(\x0b\x32\x1e.RemoteFortressReader.PlantDef*\xba\x02\n\rTiletypeShape\x12\x15\n\x08NO_SHAPE\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\t\n\x05\x45MPTY\x10\x00\x12\t\n\x05\x46LOOR\x10\x01\x12\x0b\n\x07\x42OULDER\x10\x02\x12\x0b\n\x07PEBBLES\x10\x03\x12\x08\n\x04WALL\x10\x04\x12\x11\n\rFORTIFICATION\x10\x05\x12\x0c\n\x08STAIR_UP\x10\x06\x12\x0e\n\nSTAIR_DOWN\x10\x07\x12\x10\n\x0cSTAIR_UPDOWN\x10\x08\x12\x08\n\x04RAMP\x10\t\x12\x0c\n\x08RAMP_TOP\x10\n\x12\r\n\tBROOK_BED\x10\x0b\x12\r\n\tBROOK_TOP\x10\x0c\x12\x0e\n\nTREE_SHAPE\x10\r\x12\x0b\n\x07SAPLING\x10\x0e\x12\t\n\x05SHRUB\x10\x0f\x12\x0f\n\x0b\x45NDLESS_PIT\x10\x10\x12\n\n\x06\x42RANCH\x10\x11\x12\x10\n\x0cTRUNK_BRANCH\x10\x12\x12\x08\n\x04TWIG\x10\x13*\xc4\x01\n\x0fTiletypeSpecial\x12\x17\n\nNO_SPECIAL\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\n\n\x06NORMAL\x10\x00\x12\x10\n\x0cRIVER_SOURCE\x10\x01\x12\r\n\tWATERFALL\x10\x02\x12\n\n\x06SMOOTH\x10\x03\x12\x0c\n\x08\x46URROWED\x10\x04\x12\x07\n\x03WET\x10\x05\x12\x08\n\x04\x44\x45\x41\x44\x10\x06\x12\n\n\x06WORN_1\x10\x07\x12\n\n\x06WORN_2\x10\x08\x12\n\n\x06WORN_3\x10\t\x12\t\n\x05TRACK\x10\n\x12\x0f\n\x0bSMOOTH_DEAD\x10\x0b*\x8a\x03\n\x10TiletypeMaterial\x12\x18\n\x0bNO_MATERIAL\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x07\n\x03\x41IR\x10\x00\x12\x08\n\x04SOIL\x10\x01\x12\t\n\x05STONE\x10\x02\x12\x0b\n\x07\x46\x45\x41TURE\x10\x03\x12\x0e\n\nLAVA_STONE\x10\x04\x12\x0b\n\x07MINERAL\x10\x05\x12\x11\n\rFROZEN_LIQUID\x10\x06\x12\x10\n\x0c\x43ONSTRUCTION\x10\x07\x12\x0f\n\x0bGRASS_LIGHT\x10\x08\x12\x0e\n\nGRASS_DARK\x10\t\x12\r\n\tGRASS_DRY\x10\n\x12\x0e\n\nGRASS_DEAD\x10\x0b\x12\t\n\x05PLANT\x10\x0c\x12\x07\n\x03HFS\x10\r\x12\x0c\n\x08\x43\x41MPFIRE\x10\x0e\x12\x08\n\x04\x46IRE\x10\x0f\x12\t\n\x05\x41SHES\x10\x10\x12\t\n\x05MAGMA\x10\x11\x12\r\n\tDRIFTWOOD\x10\x12\x12\x08\n\x04POOL\x10\x13\x12\t\n\x05\x42ROOK\x10\x14\x12\t\n\x05RIVER\x10\x15\x12\x08\n\x04ROOT\x10\x16\x12\x11\n\rTREE_MATERIAL\x10\x17\x12\x0c\n\x08MUSHROOM\x10\x18\x12\x13\n\x0fUNDERWORLD_GATE\x10\x19*V\n\x0fTiletypeVariant\x12\x17\n\nNO_VARIANT\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\t\n\x05VAR_1\x10\x00\x12\t\n\x05VAR_2\x10\x01\x12\t\n\x05VAR_3\x10\x02\x12\t\n\x05VAR_4\x10\x03\x42\x02H\x03'))

_TILETYPESHAPE = _descriptor.EnumDescriptor(
  name='TiletypeShape',
  full_name='RemoteFortressReader.TiletypeShape',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_SHAPE', index=0, number=-1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMPTY', index=1, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLOOR', index=2, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOULDER', index=3, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PEBBLES', index=4, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WALL', index=5, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FORTIFICATION', index=6, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STAIR_UP', index=7, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STAIR_DOWN', index=8, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STAIR_UPDOWN', index=9, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RAMP', index=10, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RAMP_TOP', index=11, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BROOK_BED', index=12, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BROOK_TOP', index=13, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TREE_SHAPE', index=14, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SAPLING', index=15, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHRUB', index=16, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENDLESS_PIT', index=17, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BRANCH', index=18, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRUNK_BRANCH', index=19, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TWIG', index=20, number=19,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1252,
  serialized_end=1566,
)

TiletypeShape = enum_type_wrapper.EnumTypeWrapper(_TILETYPESHAPE)
_TILETYPESPECIAL = _descriptor.EnumDescriptor(
  name='TiletypeSpecial',
  full_name='RemoteFortressReader.TiletypeSpecial',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_SPECIAL', index=0, number=-1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NORMAL', index=1, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RIVER_SOURCE', index=2, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WATERFALL', index=3, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SMOOTH', index=4, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FURROWED', index=5, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WET', index=6, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEAD', index=7, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WORN_1', index=8, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WORN_2', index=9, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WORN_3', index=10, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRACK', index=11, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SMOOTH_DEAD', index=12, number=11,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1569,
  serialized_end=1765,
)

TiletypeSpecial = enum_type_wrapper.EnumTypeWrapper(_TILETYPESPECIAL)
_TILETYPEMATERIAL = _descriptor.EnumDescriptor(
  name='TiletypeMaterial',
  full_name='RemoteFortressReader.TiletypeMaterial',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_MATERIAL', index=0, number=-1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AIR', index=1, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOIL', index=2, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STONE', index=3, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FEATURE', index=4, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LAVA_STONE', index=5, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MINERAL', index=6, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FROZEN_LIQUID', index=7, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONSTRUCTION', index=8, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GRASS_LIGHT', index=9, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GRASS_DARK', index=10, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GRASS_DRY', index=11, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GRASS_DEAD', index=12, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLANT', index=13, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HFS', index=14, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAMPFIRE', index=15, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIRE', index=16, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ASHES', index=17, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAGMA', index=18, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DRIFTWOOD', index=19, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POOL', index=20, number=19,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BROOK', index=21, number=20,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RIVER', index=22, number=21,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROOT', index=23, number=22,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TREE_MATERIAL', index=24, number=23,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MUSHROOM', index=25, number=24,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNDERWORLD_GATE', index=26, number=25,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1768,
  serialized_end=2162,
)

TiletypeMaterial = enum_type_wrapper.EnumTypeWrapper(_TILETYPEMATERIAL)
_TILETYPEVARIANT = _descriptor.EnumDescriptor(
  name='TiletypeVariant',
  full_name='RemoteFortressReader.TiletypeVariant',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_VARIANT', index=0, number=-1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VAR_1', index=1, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VAR_2', index=2, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VAR_3', index=3, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VAR_4', index=4, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2164,
  serialized_end=2250,
)

TiletypeVariant = enum_type_wrapper.EnumTypeWrapper(_TILETYPEVARIANT)
NO_SHAPE = -1
EMPTY = 0
FLOOR = 1
BOULDER = 2
PEBBLES = 3
WALL = 4
FORTIFICATION = 5
STAIR_UP = 6
STAIR_DOWN = 7
STAIR_UPDOWN = 8
RAMP = 9
RAMP_TOP = 10
BROOK_BED = 11
BROOK_TOP = 12
TREE_SHAPE = 13
SAPLING = 14
SHRUB = 15
ENDLESS_PIT = 16
BRANCH = 17
TRUNK_BRANCH = 18
TWIG = 19
NO_SPECIAL = -1
NORMAL = 0
RIVER_SOURCE = 1
WATERFALL = 2
SMOOTH = 3
FURROWED = 4
WET = 5
DEAD = 6
WORN_1 = 7
WORN_2 = 8
WORN_3 = 9
TRACK = 10
SMOOTH_DEAD = 11
NO_MATERIAL = -1
AIR = 0
SOIL = 1
STONE = 2
FEATURE = 3
LAVA_STONE = 4
MINERAL = 5
FROZEN_LIQUID = 6
CONSTRUCTION = 7
GRASS_LIGHT = 8
GRASS_DARK = 9
GRASS_DRY = 10
GRASS_DEAD = 11
PLANT = 12
HFS = 13
CAMPFIRE = 14
FIRE = 15
ASHES = 16
MAGMA = 17
DRIFTWOOD = 18
POOL = 19
BROOK = 20
RIVER = 21
ROOT = 22
TREE_MATERIAL = 23
MUSHROOM = 24
UNDERWORLD_GATE = 25
NO_VARIANT = -1
VAR_1 = 0
VAR_2 = 1
VAR_3 = 2
VAR_4 = 3



_TILETYPE = _descriptor.Descriptor(
  name='Tiletype',
  full_name='RemoteFortressReader.Tiletype',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='RemoteFortressReader.Tiletype.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='RemoteFortressReader.Tiletype.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode(b(""), "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='caption', full_name='RemoteFortressReader.Tiletype.caption', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode(b(""), "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shape', full_name='RemoteFortressReader.Tiletype.shape', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='special', full_name='RemoteFortressReader.Tiletype.special', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='material', full_name='RemoteFortressReader.Tiletype.material', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='variant', full_name='RemoteFortressReader.Tiletype.variant', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='direction', full_name='RemoteFortressReader.Tiletype.direction', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=53,
  serialized_end=347,
)


_TILETYPELIST = _descriptor.Descriptor(
  name='TiletypeList',
  full_name='RemoteFortressReader.TiletypeList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tiletype_list', full_name='RemoteFortressReader.TiletypeList.tiletype_list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=349,
  serialized_end=418,
)


_MAPBLOCK = _descriptor.Descriptor(
  name='MapBlock',
  full_name='RemoteFortressReader.MapBlock',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='map_x', full_name='RemoteFortressReader.MapBlock.map_x', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='map_y', full_name='RemoteFortressReader.MapBlock.map_y', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='map_z', full_name='RemoteFortressReader.MapBlock.map_z', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tiles', full_name='RemoteFortressReader.MapBlock.tiles', index=3,
      number=4, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='materials', full_name='RemoteFortressReader.MapBlock.materials', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=420,
  serialized_end=540,
)


_MATPAIR = _descriptor.Descriptor(
  name='MatPair',
  full_name='RemoteFortressReader.MatPair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mat_type', full_name='RemoteFortressReader.MatPair.mat_type', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mat_index', full_name='RemoteFortressReader.MatPair.mat_index', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=542,
  serialized_end=588,
)


_COLORDEFINITION = _descriptor.Descriptor(
  name='ColorDefinition',
  full_name='RemoteFortressReader.ColorDefinition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='red', full_name='RemoteFortressReader.ColorDefinition.red', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='green', full_name='RemoteFortressReader.ColorDefinition.green', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='blue', full_name='RemoteFortressReader.ColorDefinition.blue', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=590,
  serialized_end=649,
)


_MATERIALDEFINITION = _descriptor.Descriptor(
  name='MaterialDefinition',
  full_name='RemoteFortressReader.MaterialDefinition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mat_pair', full_name='RemoteFortressReader.MaterialDefinition.mat_pair', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='RemoteFortressReader.MaterialDefinition.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode(b(""), "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='RemoteFortressReader.MaterialDefinition.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode(b(""), "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state_color', full_name='RemoteFortressReader.MaterialDefinition.state_color', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=652,
  serialized_end=807,
)


_MATERIALLIST = _descriptor.Descriptor(
  name='MaterialList',
  full_name='RemoteFortressReader.MaterialList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='material_list', full_name='RemoteFortressReader.MaterialList.material_list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=809,
  serialized_end=888,
)


_BLOCKREQUEST = _descriptor.Descriptor(
  name='BlockRequest',
  full_name='RemoteFortressReader.BlockRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='blocks_needed', full_name='RemoteFortressReader.BlockRequest.blocks_needed', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_x', full_name='RemoteFortressReader.BlockRequest.min_x', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_x', full_name='RemoteFortressReader.BlockRequest.max_x', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_y', full_name='RemoteFortressReader.BlockRequest.min_y', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_y', full_name='RemoteFortressReader.BlockRequest.max_y', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_z', full_name='RemoteFortressReader.BlockRequest.min_z', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_z', full_name='RemoteFortressReader.BlockRequest.max_z', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=890,
  serialized_end=1017,
)


_BLOCKLIST = _descriptor.Descriptor(
  name='BlockList',
  full_name='RemoteFortressReader.BlockList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='map_blocks', full_name='RemoteFortressReader.BlockList.map_blocks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='map_x', full_name='RemoteFortressReader.BlockList.map_x', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='map_y', full_name='RemoteFortressReader.BlockList.map_y', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1019,
  serialized_end=1112,
)


_PLANTDEF = _descriptor.Descriptor(
  name='PlantDef',
  full_name='RemoteFortressReader.PlantDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pos_x', full_name='RemoteFortressReader.PlantDef.pos_x', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pos_y', full_name='RemoteFortressReader.PlantDef.pos_y', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pos_z', full_name='RemoteFortressReader.PlantDef.pos_z', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='index', full_name='RemoteFortressReader.PlantDef.index', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1114,
  serialized_end=1184,
)


_PLANTLIST = _descriptor.Descriptor(
  name='PlantList',
  full_name='RemoteFortressReader.PlantList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='plant_list', full_name='RemoteFortressReader.PlantList.plant_list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1186,
  serialized_end=1249,
)

_TILETYPE.fields_by_name['shape'].enum_type = _TILETYPESHAPE
_TILETYPE.fields_by_name['special'].enum_type = _TILETYPESPECIAL
_TILETYPE.fields_by_name['material'].enum_type = _TILETYPEMATERIAL
_TILETYPE.fields_by_name['variant'].enum_type = _TILETYPEVARIANT
_TILETYPELIST.fields_by_name['tiletype_list'].message_type = _TILETYPE
_MAPBLOCK.fields_by_name['materials'].message_type = _MATPAIR
_MATERIALDEFINITION.fields_by_name['mat_pair'].message_type = _MATPAIR
_MATERIALDEFINITION.fields_by_name['state_color'].message_type = _COLORDEFINITION
_MATERIALLIST.fields_by_name['material_list'].message_type = _MATERIALDEFINITION
_BLOCKLIST.fields_by_name['map_blocks'].message_type = _MAPBLOCK
_PLANTLIST.fields_by_name['plant_list'].message_type = _PLANTDEF
DESCRIPTOR.message_types_by_name['Tiletype'] = _TILETYPE
DESCRIPTOR.message_types_by_name['TiletypeList'] = _TILETYPELIST
DESCRIPTOR.message_types_by_name['MapBlock'] = _MAPBLOCK
DESCRIPTOR.message_types_by_name['MatPair'] = _MATPAIR
DESCRIPTOR.message_types_by_name['ColorDefinition'] = _COLORDEFINITION
DESCRIPTOR.message_types_by_name['MaterialDefinition'] = _MATERIALDEFINITION
DESCRIPTOR.message_types_by_name['MaterialList'] = _MATERIALLIST
DESCRIPTOR.message_types_by_name['BlockRequest'] = _BLOCKREQUEST
DESCRIPTOR.message_types_by_name['BlockList'] = _BLOCKLIST
DESCRIPTOR.message_types_by_name['PlantDef'] = _PLANTDEF
DESCRIPTOR.message_types_by_name['PlantList'] = _PLANTLIST

Tiletype = _reflection.GeneratedProtocolMessageType('Tiletype', (_message.Message,),
    {
      'DESCRIPTOR': _TILETYPE,
      # @@protoc_insertion_point(class_scope:RemoteFortressReader.Tiletype)
    })

TiletypeList = _reflection.GeneratedProtocolMessageType('TiletypeList', (_message.Message,),
    {
      'DESCRIPTOR': _TILETYPELIST,
      # @@protoc_insertion_point(class_scope:RemoteFortressReader.TiletypeList)
    })

MapBlock = _reflection.GeneratedProtocolMessageType('MapBlock', (_message.Message,),
    {
      'DESCRIPTOR': _MAPBLOCK,
      # @@protoc_insertion_point(class_scope:RemoteFortressReader.MapBlock)
    })

MatPair = _reflection.GeneratedProtocolMessageType('MatPair', (_message.Message,),
    {
      'DESCRIPTOR': _MATPAIR,
      # @@protoc_insertion_point(class_scope:RemoteFortressReader.MatPair)
    })

ColorDefinition = _reflection.GeneratedProtocolMessageType('ColorDefinition', (_message.Message,),
    {
      'DESCRIPTOR': _COLORDEFINITION,
      # @@protoc_insertion_point(class_scope:RemoteFortressReader.ColorDefinition)
    })

MaterialDefinition = _reflection.GeneratedProtocolMessageType('MaterialDefinition', (_message.Message,),
    {
      'DESCRIPTOR': _MATERIALDEFINITION,
      # @@protoc_insertion_point(class_scope:RemoteFortressReader.MaterialDefinition)
    })

MaterialList = _reflection.GeneratedProtocolMessageType('MaterialList', (_message.Message,),
    {
      'DESCRIPTOR': _MATERIALLIST,
      # @@protoc_insertion_point(class_scope:RemoteFortressReader.MaterialList)
    })

BlockRequest = _reflection.GeneratedProtocolMessageType('BlockRequest', (_message.Message,),
    {
      'DESCRIPTOR': _BLOCKREQUEST,
      # @@protoc_insertion_point(class_scope:RemoteFortressReader.BlockRequest)
    })

BlockList = _reflection.GeneratedProtocolMessageType('BlockList', (_message.Message,),
    {
      'DESCRIPTOR': _BLOCKLIST,
      # @@protoc_insertion_point(class_scope:RemoteFortressReader.BlockList)
    })

PlantDef = _reflection.GeneratedProtocolMessageType('PlantDef', (_message.Message,),
    {
      'DESCRIPTOR': _PLANTDEF,
      # @@protoc_insertion_point(class_scope:RemoteFortressReader.PlantDef)
    })

PlantList = _reflection.GeneratedProtocolMessageType('PlantList', (_message.Message,),
    {
      'DESCRIPTOR': _PLANTLIST,
      # @@protoc_insertion_point(class_scope:RemoteFortressReader.PlantList)
    })


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), b('H\003'))
# @@protoc_insertion_point(module_scope)
