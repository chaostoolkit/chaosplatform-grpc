# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import organization_pb2 as organization_dot_organization__pb2


class OrganizationServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Create = channel.unary_unary(
        '/chaosplatform.organization.OrganizationService/Create',
        request_serializer=organization_dot_organization__pb2.CreateRequest.SerializeToString,
        response_deserializer=organization_dot_organization__pb2.CreateReply.FromString,
        )
    self.Delete = channel.unary_unary(
        '/chaosplatform.organization.OrganizationService/Delete',
        request_serializer=organization_dot_organization__pb2.DeleteRequest.SerializeToString,
        response_deserializer=organization_dot_organization__pb2.DeleteReply.FromString,
        )
    self.ByUser = channel.unary_unary(
        '/chaosplatform.organization.OrganizationService/ByUser',
        request_serializer=organization_dot_organization__pb2.GetByUserRequest.SerializeToString,
        response_deserializer=organization_dot_organization__pb2.GetByUserReply.FromString,
        )


class OrganizationServiceServicer(object):
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

  def ByUser(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_OrganizationServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=organization_dot_organization__pb2.CreateRequest.FromString,
          response_serializer=organization_dot_organization__pb2.CreateReply.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=organization_dot_organization__pb2.DeleteRequest.FromString,
          response_serializer=organization_dot_organization__pb2.DeleteReply.SerializeToString,
      ),
      'ByUser': grpc.unary_unary_rpc_method_handler(
          servicer.ByUser,
          request_deserializer=organization_dot_organization__pb2.GetByUserRequest.FromString,
          response_serializer=organization_dot_organization__pb2.GetByUserReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'chaosplatform.organization.OrganizationService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
