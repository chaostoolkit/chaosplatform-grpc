# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: auth/auth.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='auth/auth.proto',
  package='chaoshub.auth',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0f\x61uth/auth.proto\x12\rchaoshub.auth\"e\n\x0b\x41\x63\x63\x65ssToken\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x04 \x01(\t\x12\x15\n\rrefresh_token\x18\x05 \x01(\t\".\n\rCreateRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"8\n\x0b\x43reateReply\x12)\n\x05token\x18\x01 \x01(\x0b\x32\x1a.chaoshub.auth.AccessToken\"\x1b\n\rDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\r\n\x0b\x44\x65leteReply\"Y\n\x0bSaveRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x03 \x01(\t\x12\x15\n\rrefresh_token\x18\x04 \x01(\t\"\x17\n\tSaveReply\x12\n\n\x02id\x18\x01 \x01(\t\"\x1b\n\rRemoveRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\r\n\x0bRemoveReply2\x95\x01\n\x0b\x41uthService\x12\x42\n\x06\x43reate\x12\x1c.chaoshub.auth.CreateRequest\x1a\x1a.chaoshub.auth.CreateReply\x12\x42\n\x06\x44\x65lete\x12\x1c.chaoshub.auth.DeleteRequest\x1a\x1a.chaoshub.auth.DeleteReply2\x96\x01\n\x12\x41uthStorageService\x12<\n\x04Save\x12\x1a.chaoshub.auth.SaveRequest\x1a\x18.chaoshub.auth.SaveReply\x12\x42\n\x06Remove\x12\x1c.chaoshub.auth.RemoveRequest\x1a\x1a.chaoshub.auth.RemoveReplyb\x06proto3')
)




_ACCESSTOKEN = _descriptor.Descriptor(
  name='AccessToken',
  full_name='chaoshub.auth.AccessToken',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='chaoshub.auth.AccessToken.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='chaoshub.auth.AccessToken.user_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='chaoshub.auth.AccessToken.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='access_token', full_name='chaoshub.auth.AccessToken.access_token', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='refresh_token', full_name='chaoshub.auth.AccessToken.refresh_token', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=34,
  serialized_end=135,
)


_CREATEREQUEST = _descriptor.Descriptor(
  name='CreateRequest',
  full_name='chaoshub.auth.CreateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='chaoshub.auth.CreateRequest.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='chaoshub.auth.CreateRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=137,
  serialized_end=183,
)


_CREATEREPLY = _descriptor.Descriptor(
  name='CreateReply',
  full_name='chaoshub.auth.CreateReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='chaoshub.auth.CreateReply.token', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=185,
  serialized_end=241,
)


_DELETEREQUEST = _descriptor.Descriptor(
  name='DeleteRequest',
  full_name='chaoshub.auth.DeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='chaoshub.auth.DeleteRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=243,
  serialized_end=270,
)


_DELETEREPLY = _descriptor.Descriptor(
  name='DeleteReply',
  full_name='chaoshub.auth.DeleteReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=272,
  serialized_end=285,
)


_SAVEREQUEST = _descriptor.Descriptor(
  name='SaveRequest',
  full_name='chaoshub.auth.SaveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='chaoshub.auth.SaveRequest.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='chaoshub.auth.SaveRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='access_token', full_name='chaoshub.auth.SaveRequest.access_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='refresh_token', full_name='chaoshub.auth.SaveRequest.refresh_token', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_end=376,
)


_SAVEREPLY = _descriptor.Descriptor(
  name='SaveReply',
  full_name='chaoshub.auth.SaveReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='chaoshub.auth.SaveReply.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=378,
  serialized_end=401,
)


_REMOVEREQUEST = _descriptor.Descriptor(
  name='RemoveRequest',
  full_name='chaoshub.auth.RemoveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='chaoshub.auth.RemoveRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=403,
  serialized_end=430,
)


_REMOVEREPLY = _descriptor.Descriptor(
  name='RemoveReply',
  full_name='chaoshub.auth.RemoveReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=432,
  serialized_end=445,
)

_CREATEREPLY.fields_by_name['token'].message_type = _ACCESSTOKEN
DESCRIPTOR.message_types_by_name['AccessToken'] = _ACCESSTOKEN
DESCRIPTOR.message_types_by_name['CreateRequest'] = _CREATEREQUEST
DESCRIPTOR.message_types_by_name['CreateReply'] = _CREATEREPLY
DESCRIPTOR.message_types_by_name['DeleteRequest'] = _DELETEREQUEST
DESCRIPTOR.message_types_by_name['DeleteReply'] = _DELETEREPLY
DESCRIPTOR.message_types_by_name['SaveRequest'] = _SAVEREQUEST
DESCRIPTOR.message_types_by_name['SaveReply'] = _SAVEREPLY
DESCRIPTOR.message_types_by_name['RemoveRequest'] = _REMOVEREQUEST
DESCRIPTOR.message_types_by_name['RemoveReply'] = _REMOVEREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AccessToken = _reflection.GeneratedProtocolMessageType('AccessToken', (_message.Message,), dict(
  DESCRIPTOR = _ACCESSTOKEN,
  __module__ = 'auth.auth_pb2'
  # @@protoc_insertion_point(class_scope:chaoshub.auth.AccessToken)
  ))
_sym_db.RegisterMessage(AccessToken)

CreateRequest = _reflection.GeneratedProtocolMessageType('CreateRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATEREQUEST,
  __module__ = 'auth.auth_pb2'
  # @@protoc_insertion_point(class_scope:chaoshub.auth.CreateRequest)
  ))
_sym_db.RegisterMessage(CreateRequest)

CreateReply = _reflection.GeneratedProtocolMessageType('CreateReply', (_message.Message,), dict(
  DESCRIPTOR = _CREATEREPLY,
  __module__ = 'auth.auth_pb2'
  # @@protoc_insertion_point(class_scope:chaoshub.auth.CreateReply)
  ))
_sym_db.RegisterMessage(CreateReply)

DeleteRequest = _reflection.GeneratedProtocolMessageType('DeleteRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETEREQUEST,
  __module__ = 'auth.auth_pb2'
  # @@protoc_insertion_point(class_scope:chaoshub.auth.DeleteRequest)
  ))
_sym_db.RegisterMessage(DeleteRequest)

DeleteReply = _reflection.GeneratedProtocolMessageType('DeleteReply', (_message.Message,), dict(
  DESCRIPTOR = _DELETEREPLY,
  __module__ = 'auth.auth_pb2'
  # @@protoc_insertion_point(class_scope:chaoshub.auth.DeleteReply)
  ))
_sym_db.RegisterMessage(DeleteReply)

SaveRequest = _reflection.GeneratedProtocolMessageType('SaveRequest', (_message.Message,), dict(
  DESCRIPTOR = _SAVEREQUEST,
  __module__ = 'auth.auth_pb2'
  # @@protoc_insertion_point(class_scope:chaoshub.auth.SaveRequest)
  ))
_sym_db.RegisterMessage(SaveRequest)

SaveReply = _reflection.GeneratedProtocolMessageType('SaveReply', (_message.Message,), dict(
  DESCRIPTOR = _SAVEREPLY,
  __module__ = 'auth.auth_pb2'
  # @@protoc_insertion_point(class_scope:chaoshub.auth.SaveReply)
  ))
_sym_db.RegisterMessage(SaveReply)

RemoveRequest = _reflection.GeneratedProtocolMessageType('RemoveRequest', (_message.Message,), dict(
  DESCRIPTOR = _REMOVEREQUEST,
  __module__ = 'auth.auth_pb2'
  # @@protoc_insertion_point(class_scope:chaoshub.auth.RemoveRequest)
  ))
_sym_db.RegisterMessage(RemoveRequest)

RemoveReply = _reflection.GeneratedProtocolMessageType('RemoveReply', (_message.Message,), dict(
  DESCRIPTOR = _REMOVEREPLY,
  __module__ = 'auth.auth_pb2'
  # @@protoc_insertion_point(class_scope:chaoshub.auth.RemoveReply)
  ))
_sym_db.RegisterMessage(RemoveReply)



_AUTHSERVICE = _descriptor.ServiceDescriptor(
  name='AuthService',
  full_name='chaoshub.auth.AuthService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=448,
  serialized_end=597,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='chaoshub.auth.AuthService.Create',
    index=0,
    containing_service=None,
    input_type=_CREATEREQUEST,
    output_type=_CREATEREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='chaoshub.auth.AuthService.Delete',
    index=1,
    containing_service=None,
    input_type=_DELETEREQUEST,
    output_type=_DELETEREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_AUTHSERVICE)

DESCRIPTOR.services_by_name['AuthService'] = _AUTHSERVICE


_AUTHSTORAGESERVICE = _descriptor.ServiceDescriptor(
  name='AuthStorageService',
  full_name='chaoshub.auth.AuthStorageService',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  serialized_start=600,
  serialized_end=750,
  methods=[
  _descriptor.MethodDescriptor(
    name='Save',
    full_name='chaoshub.auth.AuthStorageService.Save',
    index=0,
    containing_service=None,
    input_type=_SAVEREQUEST,
    output_type=_SAVEREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Remove',
    full_name='chaoshub.auth.AuthStorageService.Remove',
    index=1,
    containing_service=None,
    input_type=_REMOVEREQUEST,
    output_type=_REMOVEREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_AUTHSTORAGESERVICE)

DESCRIPTOR.services_by_name['AuthStorageService'] = _AUTHSTORAGESERVICE

# @@protoc_insertion_point(module_scope)
