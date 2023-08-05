# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from github.com.metaprov.modelaapi.services.batchpredictord.v1 import batchpredictord_pb2 as github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_batchpredictord_dot_v1_dot_batchpredictord__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class BatchStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.BatchPredict = channel.unary_unary(
                '/github.com.metaprov.modelaapi.services.batchpredictord.v1.Batch/BatchPredict',
                request_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_batchpredictord_dot_v1_dot_batchpredictord__pb2.BatchPredictRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_batchpredictord_dot_v1_dot_batchpredictord__pb2.BatchPredictResponse.FromString,
                )
        self.Shutdown = channel.unary_unary(
                '/github.com.metaprov.modelaapi.services.batchpredictord.v1.Batch/Shutdown',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class BatchServicer(object):
    """Missing associated documentation comment in .proto file."""

    def BatchPredict(self, request, context):
        """Ingest a new dataset to the store, the store creates a new layouts and set of keys
        for the new dataset
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Shutdown(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BatchServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'BatchPredict': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchPredict,
                    request_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_batchpredictord_dot_v1_dot_batchpredictord__pb2.BatchPredictRequest.FromString,
                    response_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_batchpredictord_dot_v1_dot_batchpredictord__pb2.BatchPredictResponse.SerializeToString,
            ),
            'Shutdown': grpc.unary_unary_rpc_method_handler(
                    servicer.Shutdown,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'github.com.metaprov.modelaapi.services.batchpredictord.v1.Batch', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Batch(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def BatchPredict(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/github.com.metaprov.modelaapi.services.batchpredictord.v1.Batch/BatchPredict',
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_batchpredictord_dot_v1_dot_batchpredictord__pb2.BatchPredictRequest.SerializeToString,
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_batchpredictord_dot_v1_dot_batchpredictord__pb2.BatchPredictResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Shutdown(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/github.com.metaprov.modelaapi.services.batchpredictord.v1.Batch/Shutdown',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
