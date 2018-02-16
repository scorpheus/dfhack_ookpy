# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rename.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='rename.proto',
  package='dfproto',
  syntax='proto2',
  serialized_pb=_b('\n\x0crename.proto\x12\x07\x64\x66proto\"B\n\rRenameSquadIn\x12\x10\n\x08squad_id\x18\x01 \x02(\x05\x12\x10\n\x08nickname\x18\x02 \x01(\t\x12\r\n\x05\x61lias\x18\x03 \x01(\t\"E\n\x0cRenameUnitIn\x12\x0f\n\x07unit_id\x18\x01 \x02(\x05\x12\x10\n\x08nickname\x18\x02 \x01(\t\x12\x12\n\nprofession\x18\x03 \x01(\t\"5\n\x10RenameBuildingIn\x12\x13\n\x0b\x62uilding_id\x18\x01 \x02(\x05\x12\x0c\n\x04name\x18\x02 \x01(\tB\x02H\x03')
)




_RENAMESQUADIN = _descriptor.Descriptor(
  name='RenameSquadIn',
  full_name='dfproto.RenameSquadIn',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='squad_id', full_name='dfproto.RenameSquadIn.squad_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nickname', full_name='dfproto.RenameSquadIn.nickname', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='alias', full_name='dfproto.RenameSquadIn.alias', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=91,
)


_RENAMEUNITIN = _descriptor.Descriptor(
  name='RenameUnitIn',
  full_name='dfproto.RenameUnitIn',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unit_id', full_name='dfproto.RenameUnitIn.unit_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nickname', full_name='dfproto.RenameUnitIn.nickname', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='profession', full_name='dfproto.RenameUnitIn.profession', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=93,
  serialized_end=162,
)


_RENAMEBUILDINGIN = _descriptor.Descriptor(
  name='RenameBuildingIn',
  full_name='dfproto.RenameBuildingIn',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='building_id', full_name='dfproto.RenameBuildingIn.building_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='dfproto.RenameBuildingIn.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=164,
  serialized_end=217,
)

DESCRIPTOR.message_types_by_name['RenameSquadIn'] = _RENAMESQUADIN
DESCRIPTOR.message_types_by_name['RenameUnitIn'] = _RENAMEUNITIN
DESCRIPTOR.message_types_by_name['RenameBuildingIn'] = _RENAMEBUILDINGIN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RenameSquadIn = _reflection.GeneratedProtocolMessageType('RenameSquadIn', (_message.Message,), dict(
  DESCRIPTOR = _RENAMESQUADIN,
  __module__ = 'rename_pb2'
  # @@protoc_insertion_point(class_scope:dfproto.RenameSquadIn)
  ))
_sym_db.RegisterMessage(RenameSquadIn)

RenameUnitIn = _reflection.GeneratedProtocolMessageType('RenameUnitIn', (_message.Message,), dict(
  DESCRIPTOR = _RENAMEUNITIN,
  __module__ = 'rename_pb2'
  # @@protoc_insertion_point(class_scope:dfproto.RenameUnitIn)
  ))
_sym_db.RegisterMessage(RenameUnitIn)

RenameBuildingIn = _reflection.GeneratedProtocolMessageType('RenameBuildingIn', (_message.Message,), dict(
  DESCRIPTOR = _RENAMEBUILDINGIN,
  __module__ = 'rename_pb2'
  # @@protoc_insertion_point(class_scope:dfproto.RenameBuildingIn)
  ))
_sym_db.RegisterMessage(RenameBuildingIn)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\003'))
# @@protoc_insertion_point(module_scope)