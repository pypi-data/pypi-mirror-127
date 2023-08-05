# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: github.com/metaprov/modelaapi/services/modelpipeline/v1/modelpipeline.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from github.com.metaprov.modelaapi.pkg.apis.training.v1alpha1 import generated_pb2 as github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_training_dot_v1alpha1_dot_generated__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='github.com/metaprov/modelaapi/services/modelpipeline/v1/modelpipeline.proto',
  package='github.com.metaprov.modelaapi.services.modelpipeline.v1',
  syntax='proto3',
  serialized_options=b'Z7github.com/metaprov/modelaapi/services/modelpipeline/v1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nKgithub.com/metaprov/modelaapi/services/modelpipeline/v1/modelpipeline.proto\x12\x37github.com.metaprov.modelaapi.services.modelpipeline.v1\x1a\x1cgoogle/api/annotations.proto\x1aHgithub.com/metaprov/modelaapi/pkg/apis/training/v1alpha1/generated.proto\"\xcd\x01\n\x19ListModelPipelinesRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12n\n\x06labels\x18\x03 \x03(\x0b\x32^.github.com.metaprov.modelaapi.services.modelpipeline.v1.ListModelPipelinesRequest.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"x\n\x1aListModelPipelinesResponse\x12Z\n\x05items\x18\x01 \x01(\x0b\x32K.github.com.metaprov.modelaapi.pkg.apis.training.v1alpha1.ModelPipelineList\"\x17\n\x15ModelPipelineResponse\"s\n\x1a\x43reateModelPipelineRequest\x12U\n\x04item\x18\x01 \x01(\x0b\x32G.github.com.metaprov.modelaapi.pkg.apis.training.v1alpha1.ModelPipeline\"\x1d\n\x1b\x43reateModelPipelineResponse\"s\n\x1aUpdateModelPipelineRequest\x12U\n\x04item\x18\x01 \x01(\x0b\x32G.github.com.metaprov.modelaapi.pkg.apis.training.v1alpha1.ModelPipeline\"\x1d\n\x1bUpdateModelPipelineResponse\":\n\x17GetModelPipelineRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x7f\n\x18GetModelPipelineResponse\x12U\n\x04item\x18\x01 \x01(\x0b\x32G.github.com.metaprov.modelaapi.pkg.apis.training.v1alpha1.ModelPipeline\x12\x0c\n\x04yaml\x18\x02 \x01(\t\"=\n\x1a\x44\x65leteModelPipelineRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x1d\n\x1b\x44\x65leteModelPipelineResponse\"p\n\x17RunModelPipelineRequest\x12U\n\x04item\x18\x01 \x01(\x0b\x32G.github.com.metaprov.modelaapi.pkg.apis.training.v1alpha1.ModelPipeline\"\x1a\n\x18RunModelPipelineResponse\"\x1c\n\x1aPauseModelPipelineResponse\"<\n\x19PauseModelPipelineRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x1d\n\x1bResumeModelPipelineResponse\"=\n\x1aResumeModelPipelineRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t2\xa1\x0f\n\x14ModelPipelineService\x12\xe3\x01\n\x12ListModelPipelines\x12R.github.com.metaprov.modelaapi.services.modelpipeline.v1.ListModelPipelinesRequest\x1aS.github.com.metaprov.modelaapi.services.modelpipeline.v1.ListModelPipelinesResponse\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/api/v1alpha1/modelpipelines\x12\xe9\x01\n\x13\x43reateModelPipeline\x12S.github.com.metaprov.modelaapi.services.modelpipeline.v1.CreateModelPipelineRequest\x1aT.github.com.metaprov.modelaapi.services.modelpipeline.v1.CreateModelPipelineResponse\"\'\x82\xd3\xe4\x93\x02!\"\x1c/api/v1alpha1/modelpipelines:\x01*\x12\xe4\x01\n\x10GetModelPipeline\x12P.github.com.metaprov.modelaapi.services.modelpipeline.v1.GetModelPipelineRequest\x1aQ.github.com.metaprov.modelaapi.services.modelpipeline.v1.GetModelPipelineResponse\"+\x82\xd3\xe4\x93\x02%\x12#/api/v1alpha1/modelpipelines/{name}\x12\x87\x02\n\x13UpdateModelPipeline\x12S.github.com.metaprov.modelaapi.services.modelpipeline.v1.UpdateModelPipelineRequest\x1aT.github.com.metaprov.modelaapi.services.modelpipeline.v1.UpdateModelPipelineResponse\"E\x82\xd3\xe4\x93\x02?\x1a:/api/v1alpha1/modelpipelines/{modelpipeline.metadata.name}:\x01*\x12\xfe\x01\n\x13\x44\x65leteModelPipeline\x12S.github.com.metaprov.modelaapi.services.modelpipeline.v1.DeleteModelPipelineRequest\x1aT.github.com.metaprov.modelaapi.services.modelpipeline.v1.DeleteModelPipelineResponse\"<\x82\xd3\xe4\x93\x02\x36*4/api/v1/modelpipelines/{modelpipeline.metadata.name}\x12\xee\x01\n\x10RunModelPipeline\x12P.github.com.metaprov.modelaapi.services.modelpipeline.v1.RunModelPipelineRequest\x1aQ.github.com.metaprov.modelaapi.services.modelpipeline.v1.RunModelPipelineResponse\"5\x82\xd3\xe4\x93\x02/\"-/api/v1/modelpipelines/{namespace}/{name}:run\x12\xe6\x01\n\x12PauseModelPipeline\x12R.github.com.metaprov.modelaapi.services.modelpipeline.v1.PauseModelPipelineRequest\x1aS.github.com.metaprov.modelaapi.services.modelpipeline.v1.PauseModelPipelineResponse\"\'\x82\xd3\xe4\x93\x02!\"\x1f/v1/modelpipelines/{name}:pause\x12\xea\x01\n\x13ResumeModelPipeline\x12S.github.com.metaprov.modelaapi.services.modelpipeline.v1.ResumeModelPipelineRequest\x1aT.github.com.metaprov.modelaapi.services.modelpipeline.v1.ResumeModelPipelineResponse\"(\x82\xd3\xe4\x93\x02\"\" /v1/modelpipelines/{name}:resumeB9Z7github.com/metaprov/modelaapi/services/modelpipeline/v1b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_training_dot_v1alpha1_dot_generated__pb2.DESCRIPTOR,])




_LISTMODELPIPELINESREQUEST_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='github.com.metaprov.modelaapi.services.modelpipeline.v1.ListModelPipelinesRequest.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='github.com.metaprov.modelaapi.services.modelpipeline.v1.ListModelPipelinesRequest.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='github.com.metaprov.modelaapi.services.modelpipeline.v1.ListModelPipelinesRequest.LabelsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=401,
  serialized_end=446,
)

_LISTMODELPIPELINESREQUEST = _descriptor.Descriptor(
  name='ListModelPipelinesRequest',
  full_name='github.com.metaprov.modelaapi.services.modelpipeline.v1.ListModelPipelinesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespace', full_name='github.com.metaprov.modelaapi.services.modelpipeline.v1.ListModelPipelinesRequest.namespace', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='github.com.metaprov.modelaapi.services.modelpipeline.v1.ListModelPipelinesRequest.labels', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_LISTMODELPIPELINESREQUEST_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=241,
  serialized_end=446,
)


_LISTMODELPIPELINESRESPONSE = _descriptor.Descriptor(
  name='ListModelPipelinesResponse',
  full_name='github.com.metaprov.modelaapi.services.modelpipeline.v1.ListModelPipelinesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='github.com.metaprov.modelaapi.services.modelpipeline.v1.ListModelPipelinesResponse.items', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=448,
  serialized_end=568,
)


_MODELPIPELINERESPONSE = _descriptor.Descriptor(
  name='ModelPipelineResponse',
  full_name='github.com.metaprov.modelaapi.services.modelpipeline.v1.ModelPipelineResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
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
  serialized_start=570,
  serialized_end=593,
)


_CREATEMODELPIPELINEREQUEST = _descriptor.Descriptor(
  name='CreateModelPipelineRequest',
  full_name='github.com.metaprov.modelaapi.services.modelpipeline.v1.CreateModelPipelineRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='github.com.metaprov.modelaapi.services.modelpipeline.v1.CreateModelPipelineRequest.item', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=595,
  serialized_end=710,
)


_CREATEMODELPIPELINERESPONSE = _descriptor.Descriptor(
  name='CreateModelPipelineResponse',
  full_name='github.com.metaprov.modelaapi.services.modelpipeline.v1.CreateModelPipelineResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
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
  serialized_start=712,
  serialized_end=741,
)


_UPDATEMODELPIPELINEREQUEST = _descriptor.Descriptor(
  name='UpdateModelPipelineRequest',
  full_name='github.com.metaprov.modelaapi.services.modelpipeline.v1.UpdateModelPipelineRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='github.com.metaprov.modelaapi.services.modelpipeline.v1.UpdateModelPipelineRequest.item', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=743,
  serialized_end=858,
)


_UPDATEMODELPIPELINERESPONSE = _descriptor.Descriptor(
  name='UpdateModelPipelineResponse',
  full_name='github.com.metaprov.modelaapi.services.modelpipeline.v1.UpdateModelPipelineResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
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
  serialized_start=860,
  serialized_end=889,
)


_GETMODELPIPELINEREQUEST = _descriptor.Descriptor(
  name='GetModelPipelineRequest',
  full_name='github.com.metaprov.modelaapi.services.modelpipeline.v1.GetModelPipelineRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespace', full_name='github.com.metaprov.modelaapi.services.modelpipeline.v1.GetModelPipelineRequest.namespace', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='github.com.metaprov.modelaapi.services.modelpipeline.v1.GetModelPipelineRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=891,
  serialized_end=949,
)


_GETMODELPIPELINERESPONSE = _descriptor.Descriptor(
  name='GetModelPipelineResponse',
  full_name='github.com.metaprov.modelaapi.services.modelpipeline.v1.GetModelPipelineResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='github.com.metaprov.modelaapi.services.modelpipeline.v1.GetModelPipelineResponse.item', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='yaml', full_name='github.com.metaprov.modelaapi.services.modelpipeline.v1.GetModelPipelineResponse.yaml', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=951,
  serialized_end=1078,
)


_DELETEMODELPIPELINEREQUEST = _descriptor.Descriptor(
  name='DeleteModelPipelineRequest',
  full_name='github.com.metaprov.modelaapi.services.modelpipeline.v1.DeleteModelPipelineRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespace', full_name='github.com.metaprov.modelaapi.services.modelpipeline.v1.DeleteModelPipelineRequest.namespace', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='github.com.metaprov.modelaapi.services.modelpipeline.v1.DeleteModelPipelineRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=1080,
  serialized_end=1141,
)


_DELETEMODELPIPELINERESPONSE = _descriptor.Descriptor(
  name='DeleteModelPipelineResponse',
  full_name='github.com.metaprov.modelaapi.services.modelpipeline.v1.DeleteModelPipelineResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
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
  serialized_start=1143,
  serialized_end=1172,
)


_RUNMODELPIPELINEREQUEST = _descriptor.Descriptor(
  name='RunModelPipelineRequest',
  full_name='github.com.metaprov.modelaapi.services.modelpipeline.v1.RunModelPipelineRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='github.com.metaprov.modelaapi.services.modelpipeline.v1.RunModelPipelineRequest.item', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1174,
  serialized_end=1286,
)


_RUNMODELPIPELINERESPONSE = _descriptor.Descriptor(
  name='RunModelPipelineResponse',
  full_name='github.com.metaprov.modelaapi.services.modelpipeline.v1.RunModelPipelineResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
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
  serialized_start=1288,
  serialized_end=1314,
)


_PAUSEMODELPIPELINERESPONSE = _descriptor.Descriptor(
  name='PauseModelPipelineResponse',
  full_name='github.com.metaprov.modelaapi.services.modelpipeline.v1.PauseModelPipelineResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
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
  serialized_start=1316,
  serialized_end=1344,
)


_PAUSEMODELPIPELINEREQUEST = _descriptor.Descriptor(
  name='PauseModelPipelineRequest',
  full_name='github.com.metaprov.modelaapi.services.modelpipeline.v1.PauseModelPipelineRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespace', full_name='github.com.metaprov.modelaapi.services.modelpipeline.v1.PauseModelPipelineRequest.namespace', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='github.com.metaprov.modelaapi.services.modelpipeline.v1.PauseModelPipelineRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=1346,
  serialized_end=1406,
)


_RESUMEMODELPIPELINERESPONSE = _descriptor.Descriptor(
  name='ResumeModelPipelineResponse',
  full_name='github.com.metaprov.modelaapi.services.modelpipeline.v1.ResumeModelPipelineResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
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
  serialized_start=1408,
  serialized_end=1437,
)


_RESUMEMODELPIPELINEREQUEST = _descriptor.Descriptor(
  name='ResumeModelPipelineRequest',
  full_name='github.com.metaprov.modelaapi.services.modelpipeline.v1.ResumeModelPipelineRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespace', full_name='github.com.metaprov.modelaapi.services.modelpipeline.v1.ResumeModelPipelineRequest.namespace', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='github.com.metaprov.modelaapi.services.modelpipeline.v1.ResumeModelPipelineRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=1439,
  serialized_end=1500,
)

_LISTMODELPIPELINESREQUEST_LABELSENTRY.containing_type = _LISTMODELPIPELINESREQUEST
_LISTMODELPIPELINESREQUEST.fields_by_name['labels'].message_type = _LISTMODELPIPELINESREQUEST_LABELSENTRY
_LISTMODELPIPELINESRESPONSE.fields_by_name['items'].message_type = github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_training_dot_v1alpha1_dot_generated__pb2._MODELPIPELINELIST
_CREATEMODELPIPELINEREQUEST.fields_by_name['item'].message_type = github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_training_dot_v1alpha1_dot_generated__pb2._MODELPIPELINE
_UPDATEMODELPIPELINEREQUEST.fields_by_name['item'].message_type = github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_training_dot_v1alpha1_dot_generated__pb2._MODELPIPELINE
_GETMODELPIPELINERESPONSE.fields_by_name['item'].message_type = github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_training_dot_v1alpha1_dot_generated__pb2._MODELPIPELINE
_RUNMODELPIPELINEREQUEST.fields_by_name['item'].message_type = github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_training_dot_v1alpha1_dot_generated__pb2._MODELPIPELINE
DESCRIPTOR.message_types_by_name['ListModelPipelinesRequest'] = _LISTMODELPIPELINESREQUEST
DESCRIPTOR.message_types_by_name['ListModelPipelinesResponse'] = _LISTMODELPIPELINESRESPONSE
DESCRIPTOR.message_types_by_name['ModelPipelineResponse'] = _MODELPIPELINERESPONSE
DESCRIPTOR.message_types_by_name['CreateModelPipelineRequest'] = _CREATEMODELPIPELINEREQUEST
DESCRIPTOR.message_types_by_name['CreateModelPipelineResponse'] = _CREATEMODELPIPELINERESPONSE
DESCRIPTOR.message_types_by_name['UpdateModelPipelineRequest'] = _UPDATEMODELPIPELINEREQUEST
DESCRIPTOR.message_types_by_name['UpdateModelPipelineResponse'] = _UPDATEMODELPIPELINERESPONSE
DESCRIPTOR.message_types_by_name['GetModelPipelineRequest'] = _GETMODELPIPELINEREQUEST
DESCRIPTOR.message_types_by_name['GetModelPipelineResponse'] = _GETMODELPIPELINERESPONSE
DESCRIPTOR.message_types_by_name['DeleteModelPipelineRequest'] = _DELETEMODELPIPELINEREQUEST
DESCRIPTOR.message_types_by_name['DeleteModelPipelineResponse'] = _DELETEMODELPIPELINERESPONSE
DESCRIPTOR.message_types_by_name['RunModelPipelineRequest'] = _RUNMODELPIPELINEREQUEST
DESCRIPTOR.message_types_by_name['RunModelPipelineResponse'] = _RUNMODELPIPELINERESPONSE
DESCRIPTOR.message_types_by_name['PauseModelPipelineResponse'] = _PAUSEMODELPIPELINERESPONSE
DESCRIPTOR.message_types_by_name['PauseModelPipelineRequest'] = _PAUSEMODELPIPELINEREQUEST
DESCRIPTOR.message_types_by_name['ResumeModelPipelineResponse'] = _RESUMEMODELPIPELINERESPONSE
DESCRIPTOR.message_types_by_name['ResumeModelPipelineRequest'] = _RESUMEMODELPIPELINEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListModelPipelinesRequest = _reflection.GeneratedProtocolMessageType('ListModelPipelinesRequest', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _LISTMODELPIPELINESREQUEST_LABELSENTRY,
    '__module__' : 'github.com.metaprov.modelaapi.services.modelpipeline.v1.modelpipeline_pb2'
    # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.modelpipeline.v1.ListModelPipelinesRequest.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _LISTMODELPIPELINESREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.modelpipeline.v1.modelpipeline_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.modelpipeline.v1.ListModelPipelinesRequest)
  })
_sym_db.RegisterMessage(ListModelPipelinesRequest)
_sym_db.RegisterMessage(ListModelPipelinesRequest.LabelsEntry)

ListModelPipelinesResponse = _reflection.GeneratedProtocolMessageType('ListModelPipelinesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTMODELPIPELINESRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.modelpipeline.v1.modelpipeline_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.modelpipeline.v1.ListModelPipelinesResponse)
  })
_sym_db.RegisterMessage(ListModelPipelinesResponse)

ModelPipelineResponse = _reflection.GeneratedProtocolMessageType('ModelPipelineResponse', (_message.Message,), {
  'DESCRIPTOR' : _MODELPIPELINERESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.modelpipeline.v1.modelpipeline_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.modelpipeline.v1.ModelPipelineResponse)
  })
_sym_db.RegisterMessage(ModelPipelineResponse)

CreateModelPipelineRequest = _reflection.GeneratedProtocolMessageType('CreateModelPipelineRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEMODELPIPELINEREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.modelpipeline.v1.modelpipeline_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.modelpipeline.v1.CreateModelPipelineRequest)
  })
_sym_db.RegisterMessage(CreateModelPipelineRequest)

CreateModelPipelineResponse = _reflection.GeneratedProtocolMessageType('CreateModelPipelineResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEMODELPIPELINERESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.modelpipeline.v1.modelpipeline_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.modelpipeline.v1.CreateModelPipelineResponse)
  })
_sym_db.RegisterMessage(CreateModelPipelineResponse)

UpdateModelPipelineRequest = _reflection.GeneratedProtocolMessageType('UpdateModelPipelineRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEMODELPIPELINEREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.modelpipeline.v1.modelpipeline_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.modelpipeline.v1.UpdateModelPipelineRequest)
  })
_sym_db.RegisterMessage(UpdateModelPipelineRequest)

UpdateModelPipelineResponse = _reflection.GeneratedProtocolMessageType('UpdateModelPipelineResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEMODELPIPELINERESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.modelpipeline.v1.modelpipeline_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.modelpipeline.v1.UpdateModelPipelineResponse)
  })
_sym_db.RegisterMessage(UpdateModelPipelineResponse)

GetModelPipelineRequest = _reflection.GeneratedProtocolMessageType('GetModelPipelineRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETMODELPIPELINEREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.modelpipeline.v1.modelpipeline_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.modelpipeline.v1.GetModelPipelineRequest)
  })
_sym_db.RegisterMessage(GetModelPipelineRequest)

GetModelPipelineResponse = _reflection.GeneratedProtocolMessageType('GetModelPipelineResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETMODELPIPELINERESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.modelpipeline.v1.modelpipeline_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.modelpipeline.v1.GetModelPipelineResponse)
  })
_sym_db.RegisterMessage(GetModelPipelineResponse)

DeleteModelPipelineRequest = _reflection.GeneratedProtocolMessageType('DeleteModelPipelineRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEMODELPIPELINEREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.modelpipeline.v1.modelpipeline_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.modelpipeline.v1.DeleteModelPipelineRequest)
  })
_sym_db.RegisterMessage(DeleteModelPipelineRequest)

DeleteModelPipelineResponse = _reflection.GeneratedProtocolMessageType('DeleteModelPipelineResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEMODELPIPELINERESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.modelpipeline.v1.modelpipeline_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.modelpipeline.v1.DeleteModelPipelineResponse)
  })
_sym_db.RegisterMessage(DeleteModelPipelineResponse)

RunModelPipelineRequest = _reflection.GeneratedProtocolMessageType('RunModelPipelineRequest', (_message.Message,), {
  'DESCRIPTOR' : _RUNMODELPIPELINEREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.modelpipeline.v1.modelpipeline_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.modelpipeline.v1.RunModelPipelineRequest)
  })
_sym_db.RegisterMessage(RunModelPipelineRequest)

RunModelPipelineResponse = _reflection.GeneratedProtocolMessageType('RunModelPipelineResponse', (_message.Message,), {
  'DESCRIPTOR' : _RUNMODELPIPELINERESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.modelpipeline.v1.modelpipeline_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.modelpipeline.v1.RunModelPipelineResponse)
  })
_sym_db.RegisterMessage(RunModelPipelineResponse)

PauseModelPipelineResponse = _reflection.GeneratedProtocolMessageType('PauseModelPipelineResponse', (_message.Message,), {
  'DESCRIPTOR' : _PAUSEMODELPIPELINERESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.modelpipeline.v1.modelpipeline_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.modelpipeline.v1.PauseModelPipelineResponse)
  })
_sym_db.RegisterMessage(PauseModelPipelineResponse)

PauseModelPipelineRequest = _reflection.GeneratedProtocolMessageType('PauseModelPipelineRequest', (_message.Message,), {
  'DESCRIPTOR' : _PAUSEMODELPIPELINEREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.modelpipeline.v1.modelpipeline_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.modelpipeline.v1.PauseModelPipelineRequest)
  })
_sym_db.RegisterMessage(PauseModelPipelineRequest)

ResumeModelPipelineResponse = _reflection.GeneratedProtocolMessageType('ResumeModelPipelineResponse', (_message.Message,), {
  'DESCRIPTOR' : _RESUMEMODELPIPELINERESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.modelpipeline.v1.modelpipeline_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.modelpipeline.v1.ResumeModelPipelineResponse)
  })
_sym_db.RegisterMessage(ResumeModelPipelineResponse)

ResumeModelPipelineRequest = _reflection.GeneratedProtocolMessageType('ResumeModelPipelineRequest', (_message.Message,), {
  'DESCRIPTOR' : _RESUMEMODELPIPELINEREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.modelpipeline.v1.modelpipeline_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.modelpipeline.v1.ResumeModelPipelineRequest)
  })
_sym_db.RegisterMessage(ResumeModelPipelineRequest)


DESCRIPTOR._options = None
_LISTMODELPIPELINESREQUEST_LABELSENTRY._options = None

_MODELPIPELINESERVICE = _descriptor.ServiceDescriptor(
  name='ModelPipelineService',
  full_name='github.com.metaprov.modelaapi.services.modelpipeline.v1.ModelPipelineService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1503,
  serialized_end=3456,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListModelPipelines',
    full_name='github.com.metaprov.modelaapi.services.modelpipeline.v1.ModelPipelineService.ListModelPipelines',
    index=0,
    containing_service=None,
    input_type=_LISTMODELPIPELINESREQUEST,
    output_type=_LISTMODELPIPELINESRESPONSE,
    serialized_options=b'\202\323\344\223\002\036\022\034/api/v1alpha1/modelpipelines',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateModelPipeline',
    full_name='github.com.metaprov.modelaapi.services.modelpipeline.v1.ModelPipelineService.CreateModelPipeline',
    index=1,
    containing_service=None,
    input_type=_CREATEMODELPIPELINEREQUEST,
    output_type=_CREATEMODELPIPELINERESPONSE,
    serialized_options=b'\202\323\344\223\002!\"\034/api/v1alpha1/modelpipelines:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetModelPipeline',
    full_name='github.com.metaprov.modelaapi.services.modelpipeline.v1.ModelPipelineService.GetModelPipeline',
    index=2,
    containing_service=None,
    input_type=_GETMODELPIPELINEREQUEST,
    output_type=_GETMODELPIPELINERESPONSE,
    serialized_options=b'\202\323\344\223\002%\022#/api/v1alpha1/modelpipelines/{name}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateModelPipeline',
    full_name='github.com.metaprov.modelaapi.services.modelpipeline.v1.ModelPipelineService.UpdateModelPipeline',
    index=3,
    containing_service=None,
    input_type=_UPDATEMODELPIPELINEREQUEST,
    output_type=_UPDATEMODELPIPELINERESPONSE,
    serialized_options=b'\202\323\344\223\002?\032:/api/v1alpha1/modelpipelines/{modelpipeline.metadata.name}:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteModelPipeline',
    full_name='github.com.metaprov.modelaapi.services.modelpipeline.v1.ModelPipelineService.DeleteModelPipeline',
    index=4,
    containing_service=None,
    input_type=_DELETEMODELPIPELINEREQUEST,
    output_type=_DELETEMODELPIPELINERESPONSE,
    serialized_options=b'\202\323\344\223\0026*4/api/v1/modelpipelines/{modelpipeline.metadata.name}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RunModelPipeline',
    full_name='github.com.metaprov.modelaapi.services.modelpipeline.v1.ModelPipelineService.RunModelPipeline',
    index=5,
    containing_service=None,
    input_type=_RUNMODELPIPELINEREQUEST,
    output_type=_RUNMODELPIPELINERESPONSE,
    serialized_options=b'\202\323\344\223\002/\"-/api/v1/modelpipelines/{namespace}/{name}:run',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='PauseModelPipeline',
    full_name='github.com.metaprov.modelaapi.services.modelpipeline.v1.ModelPipelineService.PauseModelPipeline',
    index=6,
    containing_service=None,
    input_type=_PAUSEMODELPIPELINEREQUEST,
    output_type=_PAUSEMODELPIPELINERESPONSE,
    serialized_options=b'\202\323\344\223\002!\"\037/v1/modelpipelines/{name}:pause',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ResumeModelPipeline',
    full_name='github.com.metaprov.modelaapi.services.modelpipeline.v1.ModelPipelineService.ResumeModelPipeline',
    index=7,
    containing_service=None,
    input_type=_RESUMEMODELPIPELINEREQUEST,
    output_type=_RESUMEMODELPIPELINERESPONSE,
    serialized_options=b'\202\323\344\223\002\"\" /v1/modelpipelines/{name}:resume',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MODELPIPELINESERVICE)

DESCRIPTOR.services_by_name['ModelPipelineService'] = _MODELPIPELINESERVICE

# @@protoc_insertion_point(module_scope)
