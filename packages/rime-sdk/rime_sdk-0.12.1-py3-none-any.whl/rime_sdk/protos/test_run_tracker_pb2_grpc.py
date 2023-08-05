# autogenerated
# mypy: ignore-errors
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from . import test_run_tracker_pb2 as test__run__tracker__pb2


class TestRunTrackerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.TrackOperationTree = channel.unary_unary(
                '/rime.TestRunTracker/TrackOperationTree',
                request_serializer=test__run__tracker__pb2.TrackOperationTreeRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.PublishEvent = channel.unary_unary(
                '/rime.TestRunTracker/PublishEvent',
                request_serializer=test__run__tracker__pb2.PublishEventRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.GetOperationState = channel.unary_unary(
                '/rime.TestRunTracker/GetOperationState',
                request_serializer=test__run__tracker__pb2.GetOperationStateRequest.SerializeToString,
                response_deserializer=test__run__tracker__pb2.GetOperationStateResponse.FromString,
                )


class TestRunTrackerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def TrackOperationTree(self, request, context):
        """Register a new test run with a full tree of test batches and test cases.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PublishEvent(self, request, context):
        """Publish an event about an operation to update its current status.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOperationState(self, request, context):
        """Get an operation's current state based on all published events for it.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TestRunTrackerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'TrackOperationTree': grpc.unary_unary_rpc_method_handler(
                    servicer.TrackOperationTree,
                    request_deserializer=test__run__tracker__pb2.TrackOperationTreeRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'PublishEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.PublishEvent,
                    request_deserializer=test__run__tracker__pb2.PublishEventRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'GetOperationState': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOperationState,
                    request_deserializer=test__run__tracker__pb2.GetOperationStateRequest.FromString,
                    response_serializer=test__run__tracker__pb2.GetOperationStateResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'rime.TestRunTracker', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TestRunTracker(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def TrackOperationTree(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rime.TestRunTracker/TrackOperationTree',
            test__run__tracker__pb2.TrackOperationTreeRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PublishEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rime.TestRunTracker/PublishEvent',
            test__run__tracker__pb2.PublishEventRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOperationState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rime.TestRunTracker/GetOperationState',
            test__run__tracker__pb2.GetOperationStateRequest.SerializeToString,
            test__run__tracker__pb2.GetOperationStateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
