"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import data_room_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

global___DataRoomStatus = DataRoomStatus
class _DataRoomStatus(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[DataRoomStatus.V], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    Active = DataRoomStatus.V(0)
    Stopped = DataRoomStatus.V(1)
class DataRoomStatus(metaclass=_DataRoomStatus):
    V = typing.NewType('V', builtins.int)
Active = DataRoomStatus.V(0)
Stopped = DataRoomStatus.V(1)

class GcgRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    EXECUTECOMPUTEREQUEST_FIELD_NUMBER: builtins.int
    CREATEDATAROOMREQUEST_FIELD_NUMBER: builtins.int
    PUBLISHDATASETTODATAROOMREQUEST_FIELD_NUMBER: builtins.int
    RETRIEVEDATAROOMREQUEST_FIELD_NUMBER: builtins.int
    RETRIEVEAUDITLOGREQUEST_FIELD_NUMBER: builtins.int
    RETRIEVEDATAROOMSTATUSREQUEST_FIELD_NUMBER: builtins.int
    UPDATEDATAROOMSTATUSREQUEST_FIELD_NUMBER: builtins.int
    RETRIEVEPUBLISHEDDATASETSREQUEST_FIELD_NUMBER: builtins.int
    REMOVEPUBLISHEDDATASETREQUEST_FIELD_NUMBER: builtins.int
    JOBSTATUSREQUEST_FIELD_NUMBER: builtins.int
    GETRESULTSREQUEST_FIELD_NUMBER: builtins.int

    @property
    def executeComputeRequest(self) -> global___ExecuteComputeRequest: ...

    @property
    def createDataRoomRequest(self) -> global___CreateDataRoomRequest: ...

    @property
    def publishDatasetToDataRoomRequest(self) -> global___PublishDatasetToDataRoomRequest: ...

    @property
    def retrieveDataRoomRequest(self) -> global___RetrieveDataRoomRequest: ...

    @property
    def retrieveAuditLogRequest(self) -> global___RetrieveAuditLogRequest: ...

    @property
    def retrieveDataRoomStatusRequest(self) -> global___RetrieveDataRoomStatusRequest: ...

    @property
    def updateDataRoomStatusRequest(self) -> global___UpdateDataRoomStatusRequest: ...

    @property
    def retrievePublishedDatasetsRequest(self) -> global___RetrievePublishedDatasetsRequest: ...

    @property
    def removePublishedDatasetRequest(self) -> global___RemovePublishedDatasetRequest: ...

    @property
    def jobStatusRequest(self) -> global___JobStatusRequest: ...

    @property
    def getResultsRequest(self) -> global___GetResultsRequest: ...

    def __init__(self,
        *,
        executeComputeRequest : typing.Optional[global___ExecuteComputeRequest] = ...,
        createDataRoomRequest : typing.Optional[global___CreateDataRoomRequest] = ...,
        publishDatasetToDataRoomRequest : typing.Optional[global___PublishDatasetToDataRoomRequest] = ...,
        retrieveDataRoomRequest : typing.Optional[global___RetrieveDataRoomRequest] = ...,
        retrieveAuditLogRequest : typing.Optional[global___RetrieveAuditLogRequest] = ...,
        retrieveDataRoomStatusRequest : typing.Optional[global___RetrieveDataRoomStatusRequest] = ...,
        updateDataRoomStatusRequest : typing.Optional[global___UpdateDataRoomStatusRequest] = ...,
        retrievePublishedDatasetsRequest : typing.Optional[global___RetrievePublishedDatasetsRequest] = ...,
        removePublishedDatasetRequest : typing.Optional[global___RemovePublishedDatasetRequest] = ...,
        jobStatusRequest : typing.Optional[global___JobStatusRequest] = ...,
        getResultsRequest : typing.Optional[global___GetResultsRequest] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"createDataRoomRequest",b"createDataRoomRequest",u"executeComputeRequest",b"executeComputeRequest",u"gcg_request",b"gcg_request",u"getResultsRequest",b"getResultsRequest",u"jobStatusRequest",b"jobStatusRequest",u"publishDatasetToDataRoomRequest",b"publishDatasetToDataRoomRequest",u"removePublishedDatasetRequest",b"removePublishedDatasetRequest",u"retrieveAuditLogRequest",b"retrieveAuditLogRequest",u"retrieveDataRoomRequest",b"retrieveDataRoomRequest",u"retrieveDataRoomStatusRequest",b"retrieveDataRoomStatusRequest",u"retrievePublishedDatasetsRequest",b"retrievePublishedDatasetsRequest",u"updateDataRoomStatusRequest",b"updateDataRoomStatusRequest"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"createDataRoomRequest",b"createDataRoomRequest",u"executeComputeRequest",b"executeComputeRequest",u"gcg_request",b"gcg_request",u"getResultsRequest",b"getResultsRequest",u"jobStatusRequest",b"jobStatusRequest",u"publishDatasetToDataRoomRequest",b"publishDatasetToDataRoomRequest",u"removePublishedDatasetRequest",b"removePublishedDatasetRequest",u"retrieveAuditLogRequest",b"retrieveAuditLogRequest",u"retrieveDataRoomRequest",b"retrieveDataRoomRequest",u"retrieveDataRoomStatusRequest",b"retrieveDataRoomStatusRequest",u"retrievePublishedDatasetsRequest",b"retrievePublishedDatasetsRequest",u"updateDataRoomStatusRequest",b"updateDataRoomStatusRequest"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"gcg_request",b"gcg_request"]) -> typing_extensions.Literal["executeComputeRequest","createDataRoomRequest","publishDatasetToDataRoomRequest","retrieveDataRoomRequest","retrieveAuditLogRequest","retrieveDataRoomStatusRequest","updateDataRoomStatusRequest","retrievePublishedDatasetsRequest","removePublishedDatasetRequest","jobStatusRequest","getResultsRequest"]: ...
global___GcgRequest = GcgRequest

class GcgResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    FAILURE_FIELD_NUMBER: builtins.int
    EXECUTECOMPUTERESPONSE_FIELD_NUMBER: builtins.int
    CREATEDATAROOMRESPONSE_FIELD_NUMBER: builtins.int
    PUBLISHDATASETTODATAROOMRESPONSE_FIELD_NUMBER: builtins.int
    RETRIEVEDATAROOMRESPONSE_FIELD_NUMBER: builtins.int
    RETRIEVEAUDITLOGRESPONSE_FIELD_NUMBER: builtins.int
    RETRIEVEDATAROOMSTATUSRESPONSE_FIELD_NUMBER: builtins.int
    UPDATEDATAROOMSTATUSRESPONSE_FIELD_NUMBER: builtins.int
    RETRIEVEPUBLISHEDDATASETSRESPONSE_FIELD_NUMBER: builtins.int
    REMOVEPUBLISHEDDATASETRESPONSE_FIELD_NUMBER: builtins.int
    JOBSTATUSRESPONSE_FIELD_NUMBER: builtins.int
    GETRESULTSRESPONSECHUNK_FIELD_NUMBER: builtins.int
    failure: typing.Text = ...

    @property
    def executeComputeResponse(self) -> global___ExecuteComputeResponse: ...

    @property
    def createDataRoomResponse(self) -> global___CreateDataRoomResponse: ...

    @property
    def publishDatasetToDataRoomResponse(self) -> global___PublishDatasetToDataRoomResponse: ...

    @property
    def retrieveDataRoomResponse(self) -> global___RetrieveDataRoomResponse: ...

    @property
    def retrieveAuditLogResponse(self) -> global___RetrieveAuditLogResponse: ...

    @property
    def retrieveDataRoomStatusResponse(self) -> global___RetrieveDataRoomStatusResponse: ...

    @property
    def updateDataRoomStatusResponse(self) -> global___UpdateDataRoomStatusResponse: ...

    @property
    def retrievePublishedDatasetsResponse(self) -> global___RetrievePublishedDatasetsResponse: ...

    @property
    def removePublishedDatasetResponse(self) -> global___RemovePublishedDatasetResponse: ...

    @property
    def jobStatusResponse(self) -> global___JobStatusResponse: ...

    @property
    def getResultsResponseChunk(self) -> global___GetResultsResponseChunk: ...

    def __init__(self,
        *,
        failure : typing.Text = ...,
        executeComputeResponse : typing.Optional[global___ExecuteComputeResponse] = ...,
        createDataRoomResponse : typing.Optional[global___CreateDataRoomResponse] = ...,
        publishDatasetToDataRoomResponse : typing.Optional[global___PublishDatasetToDataRoomResponse] = ...,
        retrieveDataRoomResponse : typing.Optional[global___RetrieveDataRoomResponse] = ...,
        retrieveAuditLogResponse : typing.Optional[global___RetrieveAuditLogResponse] = ...,
        retrieveDataRoomStatusResponse : typing.Optional[global___RetrieveDataRoomStatusResponse] = ...,
        updateDataRoomStatusResponse : typing.Optional[global___UpdateDataRoomStatusResponse] = ...,
        retrievePublishedDatasetsResponse : typing.Optional[global___RetrievePublishedDatasetsResponse] = ...,
        removePublishedDatasetResponse : typing.Optional[global___RemovePublishedDatasetResponse] = ...,
        jobStatusResponse : typing.Optional[global___JobStatusResponse] = ...,
        getResultsResponseChunk : typing.Optional[global___GetResultsResponseChunk] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"createDataRoomResponse",b"createDataRoomResponse",u"executeComputeResponse",b"executeComputeResponse",u"failure",b"failure",u"gcg_response",b"gcg_response",u"getResultsResponseChunk",b"getResultsResponseChunk",u"jobStatusResponse",b"jobStatusResponse",u"publishDatasetToDataRoomResponse",b"publishDatasetToDataRoomResponse",u"removePublishedDatasetResponse",b"removePublishedDatasetResponse",u"retrieveAuditLogResponse",b"retrieveAuditLogResponse",u"retrieveDataRoomResponse",b"retrieveDataRoomResponse",u"retrieveDataRoomStatusResponse",b"retrieveDataRoomStatusResponse",u"retrievePublishedDatasetsResponse",b"retrievePublishedDatasetsResponse",u"updateDataRoomStatusResponse",b"updateDataRoomStatusResponse"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"createDataRoomResponse",b"createDataRoomResponse",u"executeComputeResponse",b"executeComputeResponse",u"failure",b"failure",u"gcg_response",b"gcg_response",u"getResultsResponseChunk",b"getResultsResponseChunk",u"jobStatusResponse",b"jobStatusResponse",u"publishDatasetToDataRoomResponse",b"publishDatasetToDataRoomResponse",u"removePublishedDatasetResponse",b"removePublishedDatasetResponse",u"retrieveAuditLogResponse",b"retrieveAuditLogResponse",u"retrieveDataRoomResponse",b"retrieveDataRoomResponse",u"retrieveDataRoomStatusResponse",b"retrieveDataRoomStatusResponse",u"retrievePublishedDatasetsResponse",b"retrievePublishedDatasetsResponse",u"updateDataRoomStatusResponse",b"updateDataRoomStatusResponse"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"gcg_response",b"gcg_response"]) -> typing_extensions.Literal["failure","executeComputeResponse","createDataRoomResponse","publishDatasetToDataRoomResponse","retrieveDataRoomResponse","retrieveAuditLogResponse","retrieveDataRoomStatusResponse","updateDataRoomStatusResponse","retrievePublishedDatasetsResponse","removePublishedDatasetResponse","jobStatusResponse","getResultsResponseChunk"]: ...
global___GcgResponse = GcgResponse

class CreateDataRoomRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DATAROOM_FIELD_NUMBER: builtins.int
    SCOPE_FIELD_NUMBER: builtins.int
    scope: builtins.bytes = ...

    @property
    def dataRoom(self) -> data_room_pb2.DataRoom: ...

    def __init__(self,
        *,
        dataRoom : typing.Optional[data_room_pb2.DataRoom] = ...,
        scope : builtins.bytes = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"dataRoom",b"dataRoom"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"dataRoom",b"dataRoom",u"scope",b"scope"]) -> None: ...
global___CreateDataRoomRequest = CreateDataRoomRequest

class CreateDataRoomResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DATAROOMID_FIELD_NUMBER: builtins.int
    DATAROOMVALIDATIONERROR_FIELD_NUMBER: builtins.int
    dataRoomId: builtins.bytes = ...

    @property
    def dataRoomValidationError(self) -> global___DataRoomValidationError: ...

    def __init__(self,
        *,
        dataRoomId : builtins.bytes = ...,
        dataRoomValidationError : typing.Optional[global___DataRoomValidationError] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"create_data_room_response",b"create_data_room_response",u"dataRoomId",b"dataRoomId",u"dataRoomValidationError",b"dataRoomValidationError"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"create_data_room_response",b"create_data_room_response",u"dataRoomId",b"dataRoomId",u"dataRoomValidationError",b"dataRoomValidationError"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"create_data_room_response",b"create_data_room_response"]) -> typing_extensions.Literal["dataRoomId","dataRoomValidationError"]: ...
global___CreateDataRoomResponse = CreateDataRoomResponse

class DataRoomValidationError(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    MESSAGE_FIELD_NUMBER: builtins.int
    COMPUTENODEINDEX_FIELD_NUMBER: builtins.int
    COLUMNINDEX_FIELD_NUMBER: builtins.int
    TABLEINDEX_FIELD_NUMBER: builtins.int
    USERPERMISSIONINDEX_FIELD_NUMBER: builtins.int
    PERMISSIONINDEX_FIELD_NUMBER: builtins.int
    ATTESTATIONSPECIFICATIONINDEX_FIELD_NUMBER: builtins.int
    AUTHENTICATIONMETHODINDEX_FIELD_NUMBER: builtins.int
    message: typing.Text = ...
    computeNodeIndex: builtins.int = ...
    columnIndex: builtins.int = ...
    tableIndex: builtins.int = ...
    userPermissionIndex: builtins.int = ...
    permissionIndex: builtins.int = ...
    attestationSpecificationIndex: builtins.int = ...
    authenticationMethodIndex: builtins.int = ...

    def __init__(self,
        *,
        message : typing.Text = ...,
        computeNodeIndex : builtins.int = ...,
        columnIndex : builtins.int = ...,
        tableIndex : builtins.int = ...,
        userPermissionIndex : builtins.int = ...,
        permissionIndex : builtins.int = ...,
        attestationSpecificationIndex : builtins.int = ...,
        authenticationMethodIndex : builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"_attestationSpecificationIndex",b"_attestationSpecificationIndex",u"_authenticationMethodIndex",b"_authenticationMethodIndex",u"_columnIndex",b"_columnIndex",u"_computeNodeIndex",b"_computeNodeIndex",u"_permissionIndex",b"_permissionIndex",u"_tableIndex",b"_tableIndex",u"_userPermissionIndex",b"_userPermissionIndex",u"attestationSpecificationIndex",b"attestationSpecificationIndex",u"authenticationMethodIndex",b"authenticationMethodIndex",u"columnIndex",b"columnIndex",u"computeNodeIndex",b"computeNodeIndex",u"permissionIndex",b"permissionIndex",u"tableIndex",b"tableIndex",u"userPermissionIndex",b"userPermissionIndex"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"_attestationSpecificationIndex",b"_attestationSpecificationIndex",u"_authenticationMethodIndex",b"_authenticationMethodIndex",u"_columnIndex",b"_columnIndex",u"_computeNodeIndex",b"_computeNodeIndex",u"_permissionIndex",b"_permissionIndex",u"_tableIndex",b"_tableIndex",u"_userPermissionIndex",b"_userPermissionIndex",u"attestationSpecificationIndex",b"attestationSpecificationIndex",u"authenticationMethodIndex",b"authenticationMethodIndex",u"columnIndex",b"columnIndex",u"computeNodeIndex",b"computeNodeIndex",u"message",b"message",u"permissionIndex",b"permissionIndex",u"tableIndex",b"tableIndex",u"userPermissionIndex",b"userPermissionIndex"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"_attestationSpecificationIndex",b"_attestationSpecificationIndex"]) -> typing_extensions.Literal["attestationSpecificationIndex"]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"_authenticationMethodIndex",b"_authenticationMethodIndex"]) -> typing_extensions.Literal["authenticationMethodIndex"]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"_columnIndex",b"_columnIndex"]) -> typing_extensions.Literal["columnIndex"]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"_computeNodeIndex",b"_computeNodeIndex"]) -> typing_extensions.Literal["computeNodeIndex"]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"_permissionIndex",b"_permissionIndex"]) -> typing_extensions.Literal["permissionIndex"]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"_tableIndex",b"_tableIndex"]) -> typing_extensions.Literal["tableIndex"]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"_userPermissionIndex",b"_userPermissionIndex"]) -> typing_extensions.Literal["userPermissionIndex"]: ...
global___DataRoomValidationError = DataRoomValidationError

class PublishDatasetToDataRoomRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DATASETHASH_FIELD_NUMBER: builtins.int
    DATAROOMID_FIELD_NUMBER: builtins.int
    LEAFNAME_FIELD_NUMBER: builtins.int
    ENCRYPTIONKEY_FIELD_NUMBER: builtins.int
    SCOPE_FIELD_NUMBER: builtins.int
    datasetHash: builtins.bytes = ...
    dataRoomId: builtins.bytes = ...
    leafName: typing.Text = ...
    encryptionKey: builtins.bytes = ...
    scope: builtins.bytes = ...

    def __init__(self,
        *,
        datasetHash : builtins.bytes = ...,
        dataRoomId : builtins.bytes = ...,
        leafName : typing.Text = ...,
        encryptionKey : builtins.bytes = ...,
        scope : builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"dataRoomId",b"dataRoomId",u"datasetHash",b"datasetHash",u"encryptionKey",b"encryptionKey",u"leafName",b"leafName",u"scope",b"scope"]) -> None: ...
global___PublishDatasetToDataRoomRequest = PublishDatasetToDataRoomRequest

class PublishDatasetToDataRoomResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

    def __init__(self,
        ) -> None: ...
global___PublishDatasetToDataRoomResponse = PublishDatasetToDataRoomResponse

class ExecuteComputeRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DATAROOMID_FIELD_NUMBER: builtins.int
    COMPUTENODENAMES_FIELD_NUMBER: builtins.int
    ISDRYRUN_FIELD_NUMBER: builtins.int
    SCOPE_FIELD_NUMBER: builtins.int
    dataRoomId: builtins.bytes = ...
    computeNodeNames: google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text] = ...
    isDryRun: builtins.bool = ...
    scope: builtins.bytes = ...

    def __init__(self,
        *,
        dataRoomId : builtins.bytes = ...,
        computeNodeNames : typing.Optional[typing.Iterable[typing.Text]] = ...,
        isDryRun : builtins.bool = ...,
        scope : builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"computeNodeNames",b"computeNodeNames",u"dataRoomId",b"dataRoomId",u"isDryRun",b"isDryRun",u"scope",b"scope"]) -> None: ...
global___ExecuteComputeRequest = ExecuteComputeRequest

class ExecuteComputeResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    JOBID_FIELD_NUMBER: builtins.int
    jobId: builtins.bytes = ...

    def __init__(self,
        *,
        jobId : builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"jobId",b"jobId"]) -> None: ...
global___ExecuteComputeResponse = ExecuteComputeResponse

class JobStatusRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    JOBID_FIELD_NUMBER: builtins.int
    jobId: builtins.bytes = ...

    def __init__(self,
        *,
        jobId : builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"jobId",b"jobId"]) -> None: ...
global___JobStatusRequest = JobStatusRequest

class JobStatusResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    COMPLETECOMPUTENODENAMES_FIELD_NUMBER: builtins.int
    completeComputeNodeNames: google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text] = ...

    def __init__(self,
        *,
        completeComputeNodeNames : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"completeComputeNodeNames",b"completeComputeNodeNames"]) -> None: ...
global___JobStatusResponse = JobStatusResponse

class GetResultsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    JOBID_FIELD_NUMBER: builtins.int
    COMPUTENODENAME_FIELD_NUMBER: builtins.int
    jobId: builtins.bytes = ...
    computeNodeName: typing.Text = ...

    def __init__(self,
        *,
        jobId : builtins.bytes = ...,
        computeNodeName : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"computeNodeName",b"computeNodeName",u"jobId",b"jobId"]) -> None: ...
global___GetResultsRequest = GetResultsRequest

class GetResultsResponseChunk(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DATA_FIELD_NUMBER: builtins.int
    data: builtins.bytes = ...

    def __init__(self,
        *,
        data : builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"data",b"data"]) -> None: ...
global___GetResultsResponseChunk = GetResultsResponseChunk

class RetrieveDataRoomRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DATAROOMID_FIELD_NUMBER: builtins.int
    SCOPE_FIELD_NUMBER: builtins.int
    dataRoomId: builtins.bytes = ...
    scope: builtins.bytes = ...

    def __init__(self,
        *,
        dataRoomId : builtins.bytes = ...,
        scope : builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"dataRoomId",b"dataRoomId",u"scope",b"scope"]) -> None: ...
global___RetrieveDataRoomRequest = RetrieveDataRoomRequest

class RetrieveDataRoomResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DATAROOM_FIELD_NUMBER: builtins.int

    @property
    def dataRoom(self) -> data_room_pb2.DataRoom: ...

    def __init__(self,
        *,
        dataRoom : typing.Optional[data_room_pb2.DataRoom] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"dataRoom",b"dataRoom"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"dataRoom",b"dataRoom"]) -> None: ...
global___RetrieveDataRoomResponse = RetrieveDataRoomResponse

class RetrieveAuditLogRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DATAROOMID_FIELD_NUMBER: builtins.int
    SCOPE_FIELD_NUMBER: builtins.int
    dataRoomId: builtins.bytes = ...
    scope: builtins.bytes = ...

    def __init__(self,
        *,
        dataRoomId : builtins.bytes = ...,
        scope : builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"dataRoomId",b"dataRoomId",u"scope",b"scope"]) -> None: ...
global___RetrieveAuditLogRequest = RetrieveAuditLogRequest

class RetrieveAuditLogResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    LOG_FIELD_NUMBER: builtins.int
    log: builtins.bytes = ...

    def __init__(self,
        *,
        log : builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"log",b"log"]) -> None: ...
global___RetrieveAuditLogResponse = RetrieveAuditLogResponse

class RetrieveDataRoomStatusRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DATAROOMID_FIELD_NUMBER: builtins.int
    SCOPE_FIELD_NUMBER: builtins.int
    dataRoomId: builtins.bytes = ...
    scope: builtins.bytes = ...

    def __init__(self,
        *,
        dataRoomId : builtins.bytes = ...,
        scope : builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"dataRoomId",b"dataRoomId",u"scope",b"scope"]) -> None: ...
global___RetrieveDataRoomStatusRequest = RetrieveDataRoomStatusRequest

class RetrieveDataRoomStatusResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    STATUS_FIELD_NUMBER: builtins.int
    status: global___DataRoomStatus.V = ...

    def __init__(self,
        *,
        status : global___DataRoomStatus.V = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"status",b"status"]) -> None: ...
global___RetrieveDataRoomStatusResponse = RetrieveDataRoomStatusResponse

class UpdateDataRoomStatusRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DATAROOMID_FIELD_NUMBER: builtins.int
    SCOPE_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    dataRoomId: builtins.bytes = ...
    scope: builtins.bytes = ...
    status: global___DataRoomStatus.V = ...

    def __init__(self,
        *,
        dataRoomId : builtins.bytes = ...,
        scope : builtins.bytes = ...,
        status : global___DataRoomStatus.V = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"dataRoomId",b"dataRoomId",u"scope",b"scope",u"status",b"status"]) -> None: ...
global___UpdateDataRoomStatusRequest = UpdateDataRoomStatusRequest

class UpdateDataRoomStatusResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

    def __init__(self,
        ) -> None: ...
global___UpdateDataRoomStatusResponse = UpdateDataRoomStatusResponse

class RetrievePublishedDatasetsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DATAROOMID_FIELD_NUMBER: builtins.int
    SCOPE_FIELD_NUMBER: builtins.int
    dataRoomId: builtins.bytes = ...
    scope: builtins.bytes = ...

    def __init__(self,
        *,
        dataRoomId : builtins.bytes = ...,
        scope : builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"dataRoomId",b"dataRoomId",u"scope",b"scope"]) -> None: ...
global___RetrievePublishedDatasetsRequest = RetrievePublishedDatasetsRequest

class PublishedDataset(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    LEAFNAME_FIELD_NUMBER: builtins.int
    USER_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    DATASETHASH_FIELD_NUMBER: builtins.int
    leafName: typing.Text = ...
    user: typing.Text = ...
    timestamp: builtins.int = ...
    datasetHash: builtins.bytes = ...

    def __init__(self,
        *,
        leafName : typing.Text = ...,
        user : typing.Text = ...,
        timestamp : builtins.int = ...,
        datasetHash : builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"datasetHash",b"datasetHash",u"leafName",b"leafName",u"timestamp",b"timestamp",u"user",b"user"]) -> None: ...
global___PublishedDataset = PublishedDataset

class RetrievePublishedDatasetsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PUBLISHEDDATASETS_FIELD_NUMBER: builtins.int

    @property
    def publishedDatasets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PublishedDataset]: ...

    def __init__(self,
        *,
        publishedDatasets : typing.Optional[typing.Iterable[global___PublishedDataset]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"publishedDatasets",b"publishedDatasets"]) -> None: ...
global___RetrievePublishedDatasetsResponse = RetrievePublishedDatasetsResponse

class RemovePublishedDatasetRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DATASETHASH_FIELD_NUMBER: builtins.int
    DATAROOMID_FIELD_NUMBER: builtins.int
    LEAFNAME_FIELD_NUMBER: builtins.int
    SCOPE_FIELD_NUMBER: builtins.int
    datasetHash: builtins.bytes = ...
    dataRoomId: builtins.bytes = ...
    leafName: typing.Text = ...
    scope: builtins.bytes = ...

    def __init__(self,
        *,
        datasetHash : builtins.bytes = ...,
        dataRoomId : builtins.bytes = ...,
        leafName : typing.Text = ...,
        scope : builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"dataRoomId",b"dataRoomId",u"datasetHash",b"datasetHash",u"leafName",b"leafName",u"scope",b"scope"]) -> None: ...
global___RemovePublishedDatasetRequest = RemovePublishedDatasetRequest

class RemovePublishedDatasetResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

    def __init__(self,
        ) -> None: ...
global___RemovePublishedDatasetResponse = RemovePublishedDatasetResponse

class DriverTaskConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NOOP_FIELD_NUMBER: builtins.int

    @property
    def noop(self) -> global___NoopConfig: ...

    def __init__(self,
        *,
        noop : typing.Optional[global___NoopConfig] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"driver_task_config",b"driver_task_config",u"noop",b"noop"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"driver_task_config",b"driver_task_config",u"noop",b"noop"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"driver_task_config",b"driver_task_config"]) -> typing_extensions.Literal["noop"]: ...
global___DriverTaskConfig = DriverTaskConfig

class NoopConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

    def __init__(self,
        ) -> None: ...
global___NoopConfig = NoopConfig
