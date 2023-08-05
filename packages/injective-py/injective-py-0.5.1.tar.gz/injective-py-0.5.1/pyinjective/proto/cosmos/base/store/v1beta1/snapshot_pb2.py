# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/base/store/v1beta1/snapshot.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/base/store/v1beta1/snapshot.proto',
  package='cosmos.base.store.v1beta1',
  syntax='proto3',
  serialized_options=b'Z(github.com/cosmos/cosmos-sdk/store/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n(cosmos/base/store/v1beta1/snapshot.proto\x12\x19\x63osmos.base.store.v1beta1\x1a\x14gogoproto/gogo.proto\"\x9c\x01\n\x0cSnapshotItem\x12=\n\x05store\x18\x01 \x01(\x0b\x32,.cosmos.base.store.v1beta1.SnapshotStoreItemH\x00\x12\x45\n\x04iavl\x18\x02 \x01(\x0b\x32+.cosmos.base.store.v1beta1.SnapshotIAVLItemB\x08\xe2\xde\x1f\x04IAVLH\x00\x42\x06\n\x04item\"!\n\x11SnapshotStoreItem\x12\x0c\n\x04name\x18\x01 \x01(\t\"O\n\x10SnapshotIAVLItem\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c\x12\x0f\n\x07version\x18\x03 \x01(\x03\x12\x0e\n\x06height\x18\x04 \x01(\x05\x42*Z(github.com/cosmos/cosmos-sdk/store/typesb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_SNAPSHOTITEM = _descriptor.Descriptor(
  name='SnapshotItem',
  full_name='cosmos.base.store.v1beta1.SnapshotItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='store', full_name='cosmos.base.store.v1beta1.SnapshotItem.store', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='iavl', full_name='cosmos.base.store.v1beta1.SnapshotItem.iavl', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342\336\037\004IAVL', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='item', full_name='cosmos.base.store.v1beta1.SnapshotItem.item',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=94,
  serialized_end=250,
)


_SNAPSHOTSTOREITEM = _descriptor.Descriptor(
  name='SnapshotStoreItem',
  full_name='cosmos.base.store.v1beta1.SnapshotStoreItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cosmos.base.store.v1beta1.SnapshotStoreItem.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=252,
  serialized_end=285,
)


_SNAPSHOTIAVLITEM = _descriptor.Descriptor(
  name='SnapshotIAVLItem',
  full_name='cosmos.base.store.v1beta1.SnapshotIAVLItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='cosmos.base.store.v1beta1.SnapshotIAVLItem.key', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='cosmos.base.store.v1beta1.SnapshotIAVLItem.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='cosmos.base.store.v1beta1.SnapshotIAVLItem.version', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='cosmos.base.store.v1beta1.SnapshotIAVLItem.height', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=287,
  serialized_end=366,
)

_SNAPSHOTITEM.fields_by_name['store'].message_type = _SNAPSHOTSTOREITEM
_SNAPSHOTITEM.fields_by_name['iavl'].message_type = _SNAPSHOTIAVLITEM
_SNAPSHOTITEM.oneofs_by_name['item'].fields.append(
  _SNAPSHOTITEM.fields_by_name['store'])
_SNAPSHOTITEM.fields_by_name['store'].containing_oneof = _SNAPSHOTITEM.oneofs_by_name['item']
_SNAPSHOTITEM.oneofs_by_name['item'].fields.append(
  _SNAPSHOTITEM.fields_by_name['iavl'])
_SNAPSHOTITEM.fields_by_name['iavl'].containing_oneof = _SNAPSHOTITEM.oneofs_by_name['item']
DESCRIPTOR.message_types_by_name['SnapshotItem'] = _SNAPSHOTITEM
DESCRIPTOR.message_types_by_name['SnapshotStoreItem'] = _SNAPSHOTSTOREITEM
DESCRIPTOR.message_types_by_name['SnapshotIAVLItem'] = _SNAPSHOTIAVLITEM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SnapshotItem = _reflection.GeneratedProtocolMessageType('SnapshotItem', (_message.Message,), {
  'DESCRIPTOR' : _SNAPSHOTITEM,
  '__module__' : 'cosmos.base.store.v1beta1.snapshot_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.store.v1beta1.SnapshotItem)
  })
_sym_db.RegisterMessage(SnapshotItem)

SnapshotStoreItem = _reflection.GeneratedProtocolMessageType('SnapshotStoreItem', (_message.Message,), {
  'DESCRIPTOR' : _SNAPSHOTSTOREITEM,
  '__module__' : 'cosmos.base.store.v1beta1.snapshot_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.store.v1beta1.SnapshotStoreItem)
  })
_sym_db.RegisterMessage(SnapshotStoreItem)

SnapshotIAVLItem = _reflection.GeneratedProtocolMessageType('SnapshotIAVLItem', (_message.Message,), {
  'DESCRIPTOR' : _SNAPSHOTIAVLITEM,
  '__module__' : 'cosmos.base.store.v1beta1.snapshot_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.store.v1beta1.SnapshotIAVLItem)
  })
_sym_db.RegisterMessage(SnapshotIAVLItem)


DESCRIPTOR._options = None
_SNAPSHOTITEM.fields_by_name['iavl']._options = None
# @@protoc_insertion_point(module_scope)
