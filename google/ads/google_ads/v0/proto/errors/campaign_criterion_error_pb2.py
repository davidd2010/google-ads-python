# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/errors/campaign_criterion_error.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/errors/campaign_criterion_error.proto',
  package='google.ads.googleads.v0.errors',
  syntax='proto3',
  serialized_pb=_b('\nCgoogle/ads/googleads_v0/proto/errors/campaign_criterion_error.proto\x12\x1egoogle.ads.googleads.v0.errors\"\xf5\x03\n\x1a\x43\x61mpaignCriterionErrorEnum\"\xd6\x03\n\x16\x43\x61mpaignCriterionError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x1a\n\x16\x43ONCRETE_TYPE_REQUIRED\x10\x02\x12\x19\n\x15INVALID_PLACEMENT_URL\x10\x03\x12 \n\x1c\x43\x41NNOT_EXCLUDE_CRITERIA_TYPE\x10\x04\x12\'\n#CANNOT_SET_STATUS_FOR_CRITERIA_TYPE\x10\x05\x12+\n\'CANNOT_SET_STATUS_FOR_EXCLUDED_CRITERIA\x10\x06\x12\x1d\n\x19\x43\x41NNOT_TARGET_AND_EXCLUDE\x10\x07\x12\x17\n\x13TOO_MANY_OPERATIONS\x10\x08\x12-\n)OPERATOR_NOT_SUPPORTED_FOR_CRITERION_TYPE\x10\t\x12\x43\n?SHOPPING_CAMPAIGN_SALES_COUNTRY_NOT_SUPPORTED_FOR_SALES_CHANNEL\x10\n\x12\x1d\n\x19\x43\x41NNOT_ADD_EXISTING_FIELD\x10\x0b\x12$\n CANNOT_UPDATE_NEGATIVE_CRITERION\x10\x0c\x42\xd1\x01\n\"com.google.ads.googleads.v0.errorsB\x1b\x43\x61mpaignCriterionErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V0.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V0\\Errorsb\x06proto3')
)



_CAMPAIGNCRITERIONERRORENUM_CAMPAIGNCRITERIONERROR = _descriptor.EnumDescriptor(
  name='CampaignCriterionError',
  full_name='google.ads.googleads.v0.errors.CampaignCriterionErrorEnum.CampaignCriterionError',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONCRETE_TYPE_REQUIRED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_PLACEMENT_URL', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_EXCLUDE_CRITERIA_TYPE', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_SET_STATUS_FOR_CRITERIA_TYPE', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_SET_STATUS_FOR_EXCLUDED_CRITERIA', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_TARGET_AND_EXCLUDE', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOO_MANY_OPERATIONS', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPERATOR_NOT_SUPPORTED_FOR_CRITERION_TYPE', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHOPPING_CAMPAIGN_SALES_COUNTRY_NOT_SUPPORTED_FOR_SALES_CHANNEL', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_ADD_EXISTING_FIELD', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_UPDATE_NEGATIVE_CRITERION', index=12, number=12,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=135,
  serialized_end=605,
)
_sym_db.RegisterEnumDescriptor(_CAMPAIGNCRITERIONERRORENUM_CAMPAIGNCRITERIONERROR)


_CAMPAIGNCRITERIONERRORENUM = _descriptor.Descriptor(
  name='CampaignCriterionErrorEnum',
  full_name='google.ads.googleads.v0.errors.CampaignCriterionErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CAMPAIGNCRITERIONERRORENUM_CAMPAIGNCRITERIONERROR,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=104,
  serialized_end=605,
)

_CAMPAIGNCRITERIONERRORENUM_CAMPAIGNCRITERIONERROR.containing_type = _CAMPAIGNCRITERIONERRORENUM
DESCRIPTOR.message_types_by_name['CampaignCriterionErrorEnum'] = _CAMPAIGNCRITERIONERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CampaignCriterionErrorEnum = _reflection.GeneratedProtocolMessageType('CampaignCriterionErrorEnum', (_message.Message,), dict(
  DESCRIPTOR = _CAMPAIGNCRITERIONERRORENUM,
  __module__ = 'google.ads.googleads_v0.proto.errors.campaign_criterion_error_pb2'
  ,
  __doc__ = """Container for enum describing possible campaign criterion errors.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.errors.CampaignCriterionErrorEnum)
  ))
_sym_db.RegisterMessage(CampaignCriterionErrorEnum)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\"com.google.ads.googleads.v0.errorsB\033CampaignCriterionErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V0.Errors\312\002\036Google\\Ads\\GoogleAds\\V0\\Errors'))
# @@protoc_insertion_point(module_scope)
