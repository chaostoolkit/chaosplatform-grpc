# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: workspace/workspace.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='workspace/workspace.proto',
  package='chaosplatform.workspace',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x19workspace/workspace.proto\x12\x17\x63haosplatform.workspace\" \n\x04User\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"%\n\tWorkspace\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x1d\n\rCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"D\n\x0b\x43reateReply\x12\x35\n\tworkspace\x18\x02 \x01(\x0b\x32\".chaosplatform.workspace.Workspace\"F\n\rDeleteRequest\x12\x35\n\tworkspace\x18\x01 \x01(\x0b\x32\".chaosplatform.workspace.Workspace\"\r\n\x0b\x44\x65leteReply\"#\n\x10GetByUserRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"H\n\x0eGetByUserReply\x12\x36\n\nworkspaces\x18\x01 \x03(\x0b\x32\".chaosplatform.workspace.Workspace2\xa0\x02\n\x10WorkspaceService\x12V\n\x06\x43reate\x12&.chaosplatform.workspace.CreateRequest\x1a$.chaosplatform.workspace.CreateReply\x12V\n\x06\x44\x65lete\x12&.chaosplatform.workspace.DeleteRequest\x1a$.chaosplatform.workspace.DeleteReply\x12\\\n\x06\x42yUser\x12).chaosplatform.workspace.GetByUserRequest\x1a\'.chaosplatform.workspace.GetByUserReplyb\x06proto3')
)




_USER = _descriptor.Descriptor(
  name='User',
  full_name='chaosplatform.workspace.User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='chaosplatform.workspace.User.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='chaosplatform.workspace.User.name', index=1,
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
  serialized_start=54,
  serialized_end=86,
)


_WORKSPACE = _descriptor.Descriptor(
  name='Workspace',
  full_name='chaosplatform.workspace.Workspace',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='chaosplatform.workspace.Workspace.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='chaosplatform.workspace.Workspace.name', index=1,
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
  serialized_start=88,
  serialized_end=125,
)


_CREATEREQUEST = _descriptor.Descriptor(
  name='CreateRequest',
  full_name='chaosplatform.workspace.CreateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='chaosplatform.workspace.CreateRequest.name', index=0,
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
  serialized_start=127,
  serialized_end=156,
)


_CREATEREPLY = _descriptor.Descriptor(
  name='CreateReply',
  full_name='chaosplatform.workspace.CreateReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='workspace', full_name='chaosplatform.workspace.CreateReply.workspace', index=0,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=158,
  serialized_end=226,
)


_DELETEREQUEST = _descriptor.Descriptor(
  name='DeleteRequest',
  full_name='chaosplatform.workspace.DeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='workspace', full_name='chaosplatform.workspace.DeleteRequest.workspace', index=0,
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
  serialized_start=228,
  serialized_end=298,
)


_DELETEREPLY = _descriptor.Descriptor(
  name='DeleteReply',
  full_name='chaosplatform.workspace.DeleteReply',
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
  serialized_start=300,
  serialized_end=313,
)


_GETBYUSERREQUEST = _descriptor.Descriptor(
  name='GetByUserRequest',
  full_name='chaosplatform.workspace.GetByUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='chaosplatform.workspace.GetByUserRequest.user_id', index=0,
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
  serialized_start=315,
  serialized_end=350,
)


_GETBYUSERREPLY = _descriptor.Descriptor(
  name='GetByUserReply',
  full_name='chaosplatform.workspace.GetByUserReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='workspaces', full_name='chaosplatform.workspace.GetByUserReply.workspaces', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=352,
  serialized_end=424,
)

_CREATEREPLY.fields_by_name['workspace'].message_type = _WORKSPACE
_DELETEREQUEST.fields_by_name['workspace'].message_type = _WORKSPACE
_GETBYUSERREPLY.fields_by_name['workspaces'].message_type = _WORKSPACE
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['Workspace'] = _WORKSPACE
DESCRIPTOR.message_types_by_name['CreateRequest'] = _CREATEREQUEST
DESCRIPTOR.message_types_by_name['CreateReply'] = _CREATEREPLY
DESCRIPTOR.message_types_by_name['DeleteRequest'] = _DELETEREQUEST
DESCRIPTOR.message_types_by_name['DeleteReply'] = _DELETEREPLY
DESCRIPTOR.message_types_by_name['GetByUserRequest'] = _GETBYUSERREQUEST
DESCRIPTOR.message_types_by_name['GetByUserReply'] = _GETBYUSERREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), dict(
  DESCRIPTOR = _USER,
  __module__ = 'workspace.workspace_pb2'
  # @@protoc_insertion_point(class_scope:chaosplatform.workspace.User)
  ))
_sym_db.RegisterMessage(User)

Workspace = _reflection.GeneratedProtocolMessageType('Workspace', (_message.Message,), dict(
  DESCRIPTOR = _WORKSPACE,
  __module__ = 'workspace.workspace_pb2'
  # @@protoc_insertion_point(class_scope:chaosplatform.workspace.Workspace)
  ))
_sym_db.RegisterMessage(Workspace)

CreateRequest = _reflection.GeneratedProtocolMessageType('CreateRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATEREQUEST,
  __module__ = 'workspace.workspace_pb2'
  # @@protoc_insertion_point(class_scope:chaosplatform.workspace.CreateRequest)
  ))
_sym_db.RegisterMessage(CreateRequest)

CreateReply = _reflection.GeneratedProtocolMessageType('CreateReply', (_message.Message,), dict(
  DESCRIPTOR = _CREATEREPLY,
  __module__ = 'workspace.workspace_pb2'
  # @@protoc_insertion_point(class_scope:chaosplatform.workspace.CreateReply)
  ))
_sym_db.RegisterMessage(CreateReply)

DeleteRequest = _reflection.GeneratedProtocolMessageType('DeleteRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETEREQUEST,
  __module__ = 'workspace.workspace_pb2'
  # @@protoc_insertion_point(class_scope:chaosplatform.workspace.DeleteRequest)
  ))
_sym_db.RegisterMessage(DeleteRequest)

DeleteReply = _reflection.GeneratedProtocolMessageType('DeleteReply', (_message.Message,), dict(
  DESCRIPTOR = _DELETEREPLY,
  __module__ = 'workspace.workspace_pb2'
  # @@protoc_insertion_point(class_scope:chaosplatform.workspace.DeleteReply)
  ))
_sym_db.RegisterMessage(DeleteReply)

GetByUserRequest = _reflection.GeneratedProtocolMessageType('GetByUserRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETBYUSERREQUEST,
  __module__ = 'workspace.workspace_pb2'
  # @@protoc_insertion_point(class_scope:chaosplatform.workspace.GetByUserRequest)
  ))
_sym_db.RegisterMessage(GetByUserRequest)

GetByUserReply = _reflection.GeneratedProtocolMessageType('GetByUserReply', (_message.Message,), dict(
  DESCRIPTOR = _GETBYUSERREPLY,
  __module__ = 'workspace.workspace_pb2'
  # @@protoc_insertion_point(class_scope:chaosplatform.workspace.GetByUserReply)
  ))
_sym_db.RegisterMessage(GetByUserReply)



_WORKSPACESERVICE = _descriptor.ServiceDescriptor(
  name='WorkspaceService',
  full_name='chaosplatform.workspace.WorkspaceService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=427,
  serialized_end=715,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='chaosplatform.workspace.WorkspaceService.Create',
    index=0,
    containing_service=None,
    input_type=_CREATEREQUEST,
    output_type=_CREATEREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='chaosplatform.workspace.WorkspaceService.Delete',
    index=1,
    containing_service=None,
    input_type=_DELETEREQUEST,
    output_type=_DELETEREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ByUser',
    full_name='chaosplatform.workspace.WorkspaceService.ByUser',
    index=2,
    containing_service=None,
    input_type=_GETBYUSERREQUEST,
    output_type=_GETBYUSERREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_WORKSPACESERVICE)

DESCRIPTOR.services_by_name['WorkspaceService'] = _WORKSPACESERVICE

# @@protoc_insertion_point(module_scope)
