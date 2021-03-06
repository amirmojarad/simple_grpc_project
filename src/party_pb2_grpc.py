# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import party_pb2 as party__pb2


class PartyStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.OpenDoor = channel.unary_unary(
                '/Party/OpenDoor',
                request_serializer=party__pb2.KnockKnockRequest.SerializeToString,
                response_deserializer=party__pb2.OpenReply.FromString,
                )
        self.Hello = channel.unary_unary(
                '/Party/Hello',
                request_serializer=party__pb2.HelloRequest.SerializeToString,
                response_deserializer=party__pb2.HiWelcomeReply.FromString,
                )


class PartyServicer(object):
    """Missing associated documentation comment in .proto file."""

    def OpenDoor(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Hello(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PartyServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'OpenDoor': grpc.unary_unary_rpc_method_handler(
                    servicer.OpenDoor,
                    request_deserializer=party__pb2.KnockKnockRequest.FromString,
                    response_serializer=party__pb2.OpenReply.SerializeToString,
            ),
            'Hello': grpc.unary_unary_rpc_method_handler(
                    servicer.Hello,
                    request_deserializer=party__pb2.HelloRequest.FromString,
                    response_serializer=party__pb2.HiWelcomeReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Party', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Party(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def OpenDoor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Party/OpenDoor',
            party__pb2.KnockKnockRequest.SerializeToString,
            party__pb2.OpenReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Hello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Party/Hello',
            party__pb2.HelloRequest.SerializeToString,
            party__pb2.HiWelcomeReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
