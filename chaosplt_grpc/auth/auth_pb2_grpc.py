# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import auth_pb2 as auth_dot_auth__pb2


class AuthServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Create = channel.unary_unary(
        '/chaosplatform.auth.AuthService/Create',
        request_serializer=auth_dot_auth__pb2.CreateRequest.SerializeToString,
        response_deserializer=auth_dot_auth__pb2.CreateReply.FromString,
        )
    self.Delete = channel.unary_unary(
        '/chaosplatform.auth.AuthService/Delete',
        request_serializer=auth_dot_auth__pb2.DeleteRequest.SerializeToString,
        response_deserializer=auth_dot_auth__pb2.DeleteReply.FromString,
        )
    self.Get = channel.unary_unary(
        '/chaosplatform.auth.AuthService/Get',
        request_serializer=auth_dot_auth__pb2.GetRequest.SerializeToString,
        response_deserializer=auth_dot_auth__pb2.GetReply.FromString,
        )
    self.GetByName = channel.unary_unary(
        '/chaosplatform.auth.AuthService/GetByName',
        request_serializer=auth_dot_auth__pb2.GetByUserNameRequest.SerializeToString,
        response_deserializer=auth_dot_auth__pb2.GetByUserNameReply.FromString,
        )
    self.GetByUser = channel.unary_unary(
        '/chaosplatform.auth.AuthService/GetByUser',
        request_serializer=auth_dot_auth__pb2.GetByUserRequest.SerializeToString,
        response_deserializer=auth_dot_auth__pb2.GetByUserReply.FromString,
        )


class AuthServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Create(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Delete(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Get(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetByName(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetByUser(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AuthServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=auth_dot_auth__pb2.CreateRequest.FromString,
          response_serializer=auth_dot_auth__pb2.CreateReply.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=auth_dot_auth__pb2.DeleteRequest.FromString,
          response_serializer=auth_dot_auth__pb2.DeleteReply.SerializeToString,
      ),
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=auth_dot_auth__pb2.GetRequest.FromString,
          response_serializer=auth_dot_auth__pb2.GetReply.SerializeToString,
      ),
      'GetByName': grpc.unary_unary_rpc_method_handler(
          servicer.GetByName,
          request_deserializer=auth_dot_auth__pb2.GetByUserNameRequest.FromString,
          response_serializer=auth_dot_auth__pb2.GetByUserNameReply.SerializeToString,
      ),
      'GetByUser': grpc.unary_unary_rpc_method_handler(
          servicer.GetByUser,
          request_deserializer=auth_dot_auth__pb2.GetByUserRequest.FromString,
          response_serializer=auth_dot_auth__pb2.GetByUserReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'chaosplatform.auth.AuthService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
