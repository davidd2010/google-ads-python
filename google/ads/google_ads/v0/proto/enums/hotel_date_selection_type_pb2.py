# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/enums/hotel_date_selection_type.proto

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
  name='google/ads/googleads_v0/proto/enums/hotel_date_selection_type.proto',
  package='google.ads.googleads.v0.enums',
  syntax='proto3',
  serialized_pb=_b('\nCgoogle/ads/googleads_v0/proto/enums/hotel_date_selection_type.proto\x12\x1dgoogle.ads.googleads.v0.enums\"~\n\x1aHotelDateSelectionTypeEnum\"`\n\x16HotelDateSelectionType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x15\n\x11\x44\x45\x46\x41ULT_SELECTION\x10\x32\x12\x11\n\rUSER_SELECTED\x10\x33\x42\xcc\x01\n!com.google.ads.googleads.v0.enumsB\x1bHotelDateSelectionTypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v0/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V0.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V0\\Enumsb\x06proto3')
)



_HOTELDATESELECTIONTYPEENUM_HOTELDATESELECTIONTYPE = _descriptor.EnumDescriptor(
  name='HotelDateSelectionType',
  full_name='google.ads.googleads.v0.enums.HotelDateSelectionTypeEnum.HotelDateSelectionType',
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
      name='DEFAULT_SELECTION', index=2, number=50,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USER_SELECTED', index=3, number=51,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=132,
  serialized_end=228,
)
_sym_db.RegisterEnumDescriptor(_HOTELDATESELECTIONTYPEENUM_HOTELDATESELECTIONTYPE)


_HOTELDATESELECTIONTYPEENUM = _descriptor.Descriptor(
  name='HotelDateSelectionTypeEnum',
  full_name='google.ads.googleads.v0.enums.HotelDateSelectionTypeEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _HOTELDATESELECTIONTYPEENUM_HOTELDATESELECTIONTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=102,
  serialized_end=228,
)

_HOTELDATESELECTIONTYPEENUM_HOTELDATESELECTIONTYPE.containing_type = _HOTELDATESELECTIONTYPEENUM
DESCRIPTOR.message_types_by_name['HotelDateSelectionTypeEnum'] = _HOTELDATESELECTIONTYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HotelDateSelectionTypeEnum = _reflection.GeneratedProtocolMessageType('HotelDateSelectionTypeEnum', (_message.Message,), dict(
  DESCRIPTOR = _HOTELDATESELECTIONTYPEENUM,
  __module__ = 'google.ads.googleads_v0.proto.enums.hotel_date_selection_type_pb2'
  ,
  __doc__ = """Container for enum describing possible hotel date selection types
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.enums.HotelDateSelectionTypeEnum)
  ))
_sym_db.RegisterMessage(HotelDateSelectionTypeEnum)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n!com.google.ads.googleads.v0.enumsB\033HotelDateSelectionTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v0/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V0.Enums\312\002\035Google\\Ads\\GoogleAds\\V0\\Enums'))
# @@protoc_insertion_point(module_scope)
