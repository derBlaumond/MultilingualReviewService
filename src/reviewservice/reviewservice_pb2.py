# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: reviewservice.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'reviewservice.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13reviewservice.proto\x12\rreviewservice\"\xe0\x01\n\x06Review\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nproduct_id\x18\x02 \x01(\x05\x12\x0f\n\x07user_id\x18\x03 \x01(\x05\x12\x0e\n\x06rating\x18\x04 \x01(\x05\x12\x0f\n\x07\x63ontent\x18\x05 \x01(\t\x12\x10\n\x08language\x18\x06 \x01(\t\x12=\n\x0ctranslations\x18\x07 \x03(\x0b\x32\'.reviewservice.Review.TranslationsEntry\x1a\x33\n\x11TranslationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"9\n\x10\x41\x64\x64ReviewRequest\x12%\n\x06review\x18\x01 \x01(\x0b\x32\x15.reviewservice.Review\"0\n\x11\x41\x64\x64ReviewResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\"9\n\x11GetReviewsRequest\x12\x12\n\nproduct_id\x18\x01 \x01(\x05\x12\x10\n\x08language\x18\x02 \x01(\t\"<\n\x12GetReviewsResponse\x12&\n\x07reviews\x18\x01 \x03(\x0b\x32\x15.reviewservice.Review2\xb2\x01\n\rReviewService\x12N\n\tAddReview\x12\x1f.reviewservice.AddReviewRequest\x1a .reviewservice.AddReviewResponse\x12Q\n\nGetReviews\x12 .reviewservice.GetReviewsRequest\x1a!.reviewservice.GetReviewsResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'reviewservice_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_REVIEW_TRANSLATIONSENTRY']._loaded_options = None
  _globals['_REVIEW_TRANSLATIONSENTRY']._serialized_options = b'8\001'
  _globals['_REVIEW']._serialized_start=39
  _globals['_REVIEW']._serialized_end=263
  _globals['_REVIEW_TRANSLATIONSENTRY']._serialized_start=212
  _globals['_REVIEW_TRANSLATIONSENTRY']._serialized_end=263
  _globals['_ADDREVIEWREQUEST']._serialized_start=265
  _globals['_ADDREVIEWREQUEST']._serialized_end=322
  _globals['_ADDREVIEWRESPONSE']._serialized_start=324
  _globals['_ADDREVIEWRESPONSE']._serialized_end=372
  _globals['_GETREVIEWSREQUEST']._serialized_start=374
  _globals['_GETREVIEWSREQUEST']._serialized_end=431
  _globals['_GETREVIEWSRESPONSE']._serialized_start=433
  _globals['_GETREVIEWSRESPONSE']._serialized_end=493
  _globals['_REVIEWSERVICE']._serialized_start=496
  _globals['_REVIEWSERVICE']._serialized_end=674
# @@protoc_insertion_point(module_scope)
