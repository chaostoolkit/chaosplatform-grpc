# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: organization/organization.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='organization/organization.proto',
  package='chaoshub.organization',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1forganization/organization.proto\x12\x15\x63haoshub.organization\" \n\x04User\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"9\n\x0cOrganization\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07user_id\x18\x03 \x01(\t\".\n\rCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\"H\n\x0b\x43reateReply\x12\x39\n\x0corganization\x18\x02 \x01(\x0b\x32#.chaoshub.organization.Organization\"M\n\x10TerminateRequest\x12\x39\n\x0corganization\x18\x01 \x01(\x0b\x32#.chaoshub.organization.Organization\"\x10\n\x0eTerminateReply\"=\n\x10GetByUserRequest\x12)\n\x04user\x18\x01 \x01(\x0b\x32\x1b.chaoshub.organization.User\"L\n\x0eGetByUserReply\x12:\n\rorganizations\x18\x01 \x03(\x0b\x32#.chaoshub.organization.Organization\",\n\x0bSaveRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\"\x17\n\tSaveReply\x12\n\n\x02id\x18\x01 \x01(\t\"J\n\rRemoveRequest\x12\x39\n\x0corganization\x18\x01 \x01(\x0b\x32#.chaoshub.organization.Organization\"\r\n\x0bRemoveReply\"\x19\n\x0bLoadRequest\x12\n\n\x02id\x18\x01 \x01(\t\"F\n\tLoadReply\x12\x39\n\x0corganization\x18\x01 \x01(\x0b\x32#.chaoshub.organization.Organization\"\x1e\n\x0fLoadManyRequest\x12\x0b\n\x03ids\x18\x01 \x03(\t\"J\n\rLoadManyReply\x12\x39\n\x0corganization\x18\x01 \x03(\x0b\x32#.chaoshub.organization.Organization2\x9d\x02\n\x13OrganizationService\x12R\n\x06\x43reate\x12$.chaoshub.organization.CreateRequest\x1a\".chaoshub.organization.CreateReply\x12X\n\x06\x44\x65lete\x12\'.chaoshub.organization.TerminateRequest\x1a%.chaoshub.organization.TerminateReply\x12X\n\x06\x42yUser\x12\'.chaoshub.organization.GetByUserRequest\x1a%.chaoshub.organization.GetByUserReply2\xe6\x02\n\x1aOrganizationStorageService\x12L\n\x04Save\x12\".chaoshub.organization.SaveRequest\x1a .chaoshub.organization.SaveReply\x12R\n\x06Remove\x12$.chaoshub.organization.RemoveRequest\x1a\".chaoshub.organization.RemoveReply\x12L\n\x04Load\x12\".chaoshub.organization.LoadRequest\x1a .chaoshub.organization.LoadReply\x12X\n\x08LoadMany\x12&.chaoshub.organization.LoadManyRequest\x1a$.chaoshub.organization.LoadManyReplyb\x06proto3')
)




_USER = _descriptor.Descriptor(
  name='User',
  full_name='chaoshub.organization.User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='chaoshub.organization.User.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='chaoshub.organization.User.name', index=1,
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
  serialized_start=58,
  serialized_end=90,
)


_ORGANIZATION = _descriptor.Descriptor(
  name='Organization',
  full_name='chaoshub.organization.Organization',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='chaoshub.organization.Organization.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='chaoshub.organization.Organization.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='chaoshub.organization.Organization.user_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=92,
  serialized_end=149,
)


_CREATEREQUEST = _descriptor.Descriptor(
  name='CreateRequest',
  full_name='chaoshub.organization.CreateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='chaoshub.organization.CreateRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='chaoshub.organization.CreateRequest.user_id', index=1,
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
  serialized_start=151,
  serialized_end=197,
)


_CREATEREPLY = _descriptor.Descriptor(
  name='CreateReply',
  full_name='chaoshub.organization.CreateReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='organization', full_name='chaoshub.organization.CreateReply.organization', index=0,
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
  serialized_start=199,
  serialized_end=271,
)


_TERMINATEREQUEST = _descriptor.Descriptor(
  name='TerminateRequest',
  full_name='chaoshub.organization.TerminateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='organization', full_name='chaoshub.organization.TerminateRequest.organization', index=0,
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
  serialized_start=273,
  serialized_end=350,
)


_TERMINATEREPLY = _descriptor.Descriptor(
  name='TerminateReply',
  full_name='chaoshub.organization.TerminateReply',
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
  serialized_start=352,
  serialized_end=368,
)


_GETBYUSERREQUEST = _descriptor.Descriptor(
  name='GetByUserRequest',
  full_name='chaoshub.organization.GetByUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='chaoshub.organization.GetByUserRequest.user', index=0,
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
  serialized_start=370,
  serialized_end=431,
)


_GETBYUSERREPLY = _descriptor.Descriptor(
  name='GetByUserReply',
  full_name='chaoshub.organization.GetByUserReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='organizations', full_name='chaoshub.organization.GetByUserReply.organizations', index=0,
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
  serialized_start=433,
  serialized_end=509,
)


_SAVEREQUEST = _descriptor.Descriptor(
  name='SaveRequest',
  full_name='chaoshub.organization.SaveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='chaoshub.organization.SaveRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='chaoshub.organization.SaveRequest.user_id', index=1,
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
  serialized_start=511,
  serialized_end=555,
)


_SAVEREPLY = _descriptor.Descriptor(
  name='SaveReply',
  full_name='chaoshub.organization.SaveReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='chaoshub.organization.SaveReply.id', index=0,
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
  serialized_start=557,
  serialized_end=580,
)


_REMOVEREQUEST = _descriptor.Descriptor(
  name='RemoveRequest',
  full_name='chaoshub.organization.RemoveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='organization', full_name='chaoshub.organization.RemoveRequest.organization', index=0,
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
  serialized_start=582,
  serialized_end=656,
)


_REMOVEREPLY = _descriptor.Descriptor(
  name='RemoveReply',
  full_name='chaoshub.organization.RemoveReply',
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
  serialized_start=658,
  serialized_end=671,
)


_LOADREQUEST = _descriptor.Descriptor(
  name='LoadRequest',
  full_name='chaoshub.organization.LoadRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='chaoshub.organization.LoadRequest.id', index=0,
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
  serialized_start=673,
  serialized_end=698,
)


_LOADREPLY = _descriptor.Descriptor(
  name='LoadReply',
  full_name='chaoshub.organization.LoadReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='organization', full_name='chaoshub.organization.LoadReply.organization', index=0,
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
  serialized_start=700,
  serialized_end=770,
)


_LOADMANYREQUEST = _descriptor.Descriptor(
  name='LoadManyRequest',
  full_name='chaoshub.organization.LoadManyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ids', full_name='chaoshub.organization.LoadManyRequest.ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=772,
  serialized_end=802,
)


_LOADMANYREPLY = _descriptor.Descriptor(
  name='LoadManyReply',
  full_name='chaoshub.organization.LoadManyReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='organization', full_name='chaoshub.organization.LoadManyReply.organization', index=0,
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
  serialized_start=804,
  serialized_end=878,
)

_CREATEREPLY.fields_by_name['organization'].message_type = _ORGANIZATION
_TERMINATEREQUEST.fields_by_name['organization'].message_type = _ORGANIZATION
_GETBYUSERREQUEST.fields_by_name['user'].message_type = _USER
_GETBYUSERREPLY.fields_by_name['organizations'].message_type = _ORGANIZATION
_REMOVEREQUEST.fields_by_name['organization'].message_type = _ORGANIZATION
_LOADREPLY.fields_by_name['organization'].message_type = _ORGANIZATION
_LOADMANYREPLY.fields_by_name['organization'].message_type = _ORGANIZATION
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['Organization'] = _ORGANIZATION
DESCRIPTOR.message_types_by_name['CreateRequest'] = _CREATEREQUEST
DESCRIPTOR.message_types_by_name['CreateReply'] = _CREATEREPLY
DESCRIPTOR.message_types_by_name['TerminateRequest'] = _TERMINATEREQUEST
DESCRIPTOR.message_types_by_name['TerminateReply'] = _TERMINATEREPLY
DESCRIPTOR.message_types_by_name['GetByUserRequest'] = _GETBYUSERREQUEST
DESCRIPTOR.message_types_by_name['GetByUserReply'] = _GETBYUSERREPLY
DESCRIPTOR.message_types_by_name['SaveRequest'] = _SAVEREQUEST
DESCRIPTOR.message_types_by_name['SaveReply'] = _SAVEREPLY
DESCRIPTOR.message_types_by_name['RemoveRequest'] = _REMOVEREQUEST
DESCRIPTOR.message_types_by_name['RemoveReply'] = _REMOVEREPLY
DESCRIPTOR.message_types_by_name['LoadRequest'] = _LOADREQUEST
DESCRIPTOR.message_types_by_name['LoadReply'] = _LOADREPLY
DESCRIPTOR.message_types_by_name['LoadManyRequest'] = _LOADMANYREQUEST
DESCRIPTOR.message_types_by_name['LoadManyReply'] = _LOADMANYREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), dict(
  DESCRIPTOR = _USER,
  __module__ = 'organization.organization_pb2'
  # @@protoc_insertion_point(class_scope:chaoshub.organization.User)
  ))
_sym_db.RegisterMessage(User)

Organization = _reflection.GeneratedProtocolMessageType('Organization', (_message.Message,), dict(
  DESCRIPTOR = _ORGANIZATION,
  __module__ = 'organization.organization_pb2'
  # @@protoc_insertion_point(class_scope:chaoshub.organization.Organization)
  ))
_sym_db.RegisterMessage(Organization)

CreateRequest = _reflection.GeneratedProtocolMessageType('CreateRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATEREQUEST,
  __module__ = 'organization.organization_pb2'
  # @@protoc_insertion_point(class_scope:chaoshub.organization.CreateRequest)
  ))
_sym_db.RegisterMessage(CreateRequest)

CreateReply = _reflection.GeneratedProtocolMessageType('CreateReply', (_message.Message,), dict(
  DESCRIPTOR = _CREATEREPLY,
  __module__ = 'organization.organization_pb2'
  # @@protoc_insertion_point(class_scope:chaoshub.organization.CreateReply)
  ))
_sym_db.RegisterMessage(CreateReply)

TerminateRequest = _reflection.GeneratedProtocolMessageType('TerminateRequest', (_message.Message,), dict(
  DESCRIPTOR = _TERMINATEREQUEST,
  __module__ = 'organization.organization_pb2'
  # @@protoc_insertion_point(class_scope:chaoshub.organization.TerminateRequest)
  ))
_sym_db.RegisterMessage(TerminateRequest)

TerminateReply = _reflection.GeneratedProtocolMessageType('TerminateReply', (_message.Message,), dict(
  DESCRIPTOR = _TERMINATEREPLY,
  __module__ = 'organization.organization_pb2'
  # @@protoc_insertion_point(class_scope:chaoshub.organization.TerminateReply)
  ))
_sym_db.RegisterMessage(TerminateReply)

GetByUserRequest = _reflection.GeneratedProtocolMessageType('GetByUserRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETBYUSERREQUEST,
  __module__ = 'organization.organization_pb2'
  # @@protoc_insertion_point(class_scope:chaoshub.organization.GetByUserRequest)
  ))
_sym_db.RegisterMessage(GetByUserRequest)

GetByUserReply = _reflection.GeneratedProtocolMessageType('GetByUserReply', (_message.Message,), dict(
  DESCRIPTOR = _GETBYUSERREPLY,
  __module__ = 'organization.organization_pb2'
  # @@protoc_insertion_point(class_scope:chaoshub.organization.GetByUserReply)
  ))
_sym_db.RegisterMessage(GetByUserReply)

SaveRequest = _reflection.GeneratedProtocolMessageType('SaveRequest', (_message.Message,), dict(
  DESCRIPTOR = _SAVEREQUEST,
  __module__ = 'organization.organization_pb2'
  # @@protoc_insertion_point(class_scope:chaoshub.organization.SaveRequest)
  ))
_sym_db.RegisterMessage(SaveRequest)

SaveReply = _reflection.GeneratedProtocolMessageType('SaveReply', (_message.Message,), dict(
  DESCRIPTOR = _SAVEREPLY,
  __module__ = 'organization.organization_pb2'
  # @@protoc_insertion_point(class_scope:chaoshub.organization.SaveReply)
  ))
_sym_db.RegisterMessage(SaveReply)

RemoveRequest = _reflection.GeneratedProtocolMessageType('RemoveRequest', (_message.Message,), dict(
  DESCRIPTOR = _REMOVEREQUEST,
  __module__ = 'organization.organization_pb2'
  # @@protoc_insertion_point(class_scope:chaoshub.organization.RemoveRequest)
  ))
_sym_db.RegisterMessage(RemoveRequest)

RemoveReply = _reflection.GeneratedProtocolMessageType('RemoveReply', (_message.Message,), dict(
  DESCRIPTOR = _REMOVEREPLY,
  __module__ = 'organization.organization_pb2'
  # @@protoc_insertion_point(class_scope:chaoshub.organization.RemoveReply)
  ))
_sym_db.RegisterMessage(RemoveReply)

LoadRequest = _reflection.GeneratedProtocolMessageType('LoadRequest', (_message.Message,), dict(
  DESCRIPTOR = _LOADREQUEST,
  __module__ = 'organization.organization_pb2'
  # @@protoc_insertion_point(class_scope:chaoshub.organization.LoadRequest)
  ))
_sym_db.RegisterMessage(LoadRequest)

LoadReply = _reflection.GeneratedProtocolMessageType('LoadReply', (_message.Message,), dict(
  DESCRIPTOR = _LOADREPLY,
  __module__ = 'organization.organization_pb2'
  # @@protoc_insertion_point(class_scope:chaoshub.organization.LoadReply)
  ))
_sym_db.RegisterMessage(LoadReply)

LoadManyRequest = _reflection.GeneratedProtocolMessageType('LoadManyRequest', (_message.Message,), dict(
  DESCRIPTOR = _LOADMANYREQUEST,
  __module__ = 'organization.organization_pb2'
  # @@protoc_insertion_point(class_scope:chaoshub.organization.LoadManyRequest)
  ))
_sym_db.RegisterMessage(LoadManyRequest)

LoadManyReply = _reflection.GeneratedProtocolMessageType('LoadManyReply', (_message.Message,), dict(
  DESCRIPTOR = _LOADMANYREPLY,
  __module__ = 'organization.organization_pb2'
  # @@protoc_insertion_point(class_scope:chaoshub.organization.LoadManyReply)
  ))
_sym_db.RegisterMessage(LoadManyReply)



_ORGANIZATIONSERVICE = _descriptor.ServiceDescriptor(
  name='OrganizationService',
  full_name='chaoshub.organization.OrganizationService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=881,
  serialized_end=1166,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='chaoshub.organization.OrganizationService.Create',
    index=0,
    containing_service=None,
    input_type=_CREATEREQUEST,
    output_type=_CREATEREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='chaoshub.organization.OrganizationService.Delete',
    index=1,
    containing_service=None,
    input_type=_TERMINATEREQUEST,
    output_type=_TERMINATEREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ByUser',
    full_name='chaoshub.organization.OrganizationService.ByUser',
    index=2,
    containing_service=None,
    input_type=_GETBYUSERREQUEST,
    output_type=_GETBYUSERREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ORGANIZATIONSERVICE)

DESCRIPTOR.services_by_name['OrganizationService'] = _ORGANIZATIONSERVICE


_ORGANIZATIONSTORAGESERVICE = _descriptor.ServiceDescriptor(
  name='OrganizationStorageService',
  full_name='chaoshub.organization.OrganizationStorageService',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  serialized_start=1169,
  serialized_end=1527,
  methods=[
  _descriptor.MethodDescriptor(
    name='Save',
    full_name='chaoshub.organization.OrganizationStorageService.Save',
    index=0,
    containing_service=None,
    input_type=_SAVEREQUEST,
    output_type=_SAVEREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Remove',
    full_name='chaoshub.organization.OrganizationStorageService.Remove',
    index=1,
    containing_service=None,
    input_type=_REMOVEREQUEST,
    output_type=_REMOVEREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Load',
    full_name='chaoshub.organization.OrganizationStorageService.Load',
    index=2,
    containing_service=None,
    input_type=_LOADREQUEST,
    output_type=_LOADREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='LoadMany',
    full_name='chaoshub.organization.OrganizationStorageService.LoadMany',
    index=3,
    containing_service=None,
    input_type=_LOADMANYREQUEST,
    output_type=_LOADMANYREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ORGANIZATIONSTORAGESERVICE)

DESCRIPTOR.services_by_name['OrganizationStorageService'] = _ORGANIZATIONSTORAGESERVICE

# @@protoc_insertion_point(module_scope)
