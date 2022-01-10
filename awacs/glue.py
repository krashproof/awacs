# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Glue"
prefix = "glue"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


BatchCreatePartition = Action("BatchCreatePartition")
BatchDeleteConnection = Action("BatchDeleteConnection")
BatchDeletePartition = Action("BatchDeletePartition")
BatchDeleteTable = Action("BatchDeleteTable")
BatchDeleteTableVersion = Action("BatchDeleteTableVersion")
BatchGetCrawlers = Action("BatchGetCrawlers")
BatchGetDevEndpoints = Action("BatchGetDevEndpoints")
BatchGetJobs = Action("BatchGetJobs")
BatchGetPartition = Action("BatchGetPartition")
BatchGetTriggers = Action("BatchGetTriggers")
BatchGetWorkflows = Action("BatchGetWorkflows")
BatchStopJobRun = Action("BatchStopJobRun")
BatchUpdatePartition = Action("BatchUpdatePartition")
CancelMLTaskRun = Action("CancelMLTaskRun")
CancelStatement = Action("CancelStatement")
CheckSchemaVersionValidity = Action("CheckSchemaVersionValidity")
CreateClassifier = Action("CreateClassifier")
CreateConnection = Action("CreateConnection")
CreateCrawler = Action("CreateCrawler")
CreateDatabase = Action("CreateDatabase")
CreateDevEndpoint = Action("CreateDevEndpoint")
CreateJob = Action("CreateJob")
CreateMLTransform = Action("CreateMLTransform")
CreatePartition = Action("CreatePartition")
CreatePartitionIndex = Action("CreatePartitionIndex")
CreateRegistry = Action("CreateRegistry")
CreateSchema = Action("CreateSchema")
CreateScript = Action("CreateScript")
CreateSecurityConfiguration = Action("CreateSecurityConfiguration")
CreateSession = Action("CreateSession")
CreateTable = Action("CreateTable")
CreateTrigger = Action("CreateTrigger")
CreateUserDefinedFunction = Action("CreateUserDefinedFunction")
CreateWorkflow = Action("CreateWorkflow")
DeleteClassifier = Action("DeleteClassifier")
DeleteColumnStatisticsForPartition = Action("DeleteColumnStatisticsForPartition")
DeleteColumnStatisticsForTable = Action("DeleteColumnStatisticsForTable")
DeleteConnection = Action("DeleteConnection")
DeleteCrawler = Action("DeleteCrawler")
DeleteDatabase = Action("DeleteDatabase")
DeleteDevEndpoint = Action("DeleteDevEndpoint")
DeleteJob = Action("DeleteJob")
DeleteMLTransform = Action("DeleteMLTransform")
DeletePartition = Action("DeletePartition")
DeletePartitionIndex = Action("DeletePartitionIndex")
DeleteRegistry = Action("DeleteRegistry")
DeleteResourcePolicy = Action("DeleteResourcePolicy")
DeleteSchema = Action("DeleteSchema")
DeleteSchemaVersions = Action("DeleteSchemaVersions")
DeleteSecurityConfiguration = Action("DeleteSecurityConfiguration")
DeleteSession = Action("DeleteSession")
DeleteTable = Action("DeleteTable")
DeleteTableVersion = Action("DeleteTableVersion")
DeleteTrigger = Action("DeleteTrigger")
DeleteUserDefinedFunction = Action("DeleteUserDefinedFunction")
DeleteWorkflow = Action("DeleteWorkflow")
GetCatalogImportStatus = Action("GetCatalogImportStatus")
GetClassifier = Action("GetClassifier")
GetClassifiers = Action("GetClassifiers")
GetColumnStatisticsForPartition = Action("GetColumnStatisticsForPartition")
GetColumnStatisticsForTable = Action("GetColumnStatisticsForTable")
GetConnection = Action("GetConnection")
GetConnections = Action("GetConnections")
GetCrawler = Action("GetCrawler")
GetCrawlerMetrics = Action("GetCrawlerMetrics")
GetCrawlers = Action("GetCrawlers")
GetDataCatalogEncryptionSettings = Action("GetDataCatalogEncryptionSettings")
GetDatabase = Action("GetDatabase")
GetDatabases = Action("GetDatabases")
GetDataflowGraph = Action("GetDataflowGraph")
GetDevEndpoint = Action("GetDevEndpoint")
GetDevEndpoints = Action("GetDevEndpoints")
GetJob = Action("GetJob")
GetJobBookmark = Action("GetJobBookmark")
GetJobRun = Action("GetJobRun")
GetJobRuns = Action("GetJobRuns")
GetJobs = Action("GetJobs")
GetMLTaskRun = Action("GetMLTaskRun")
GetMLTaskRuns = Action("GetMLTaskRuns")
GetMLTransform = Action("GetMLTransform")
GetMLTransforms = Action("GetMLTransforms")
GetMapping = Action("GetMapping")
GetPartition = Action("GetPartition")
GetPartitions = Action("GetPartitions")
GetPlan = Action("GetPlan")
GetRegistry = Action("GetRegistry")
GetResourcePolicies = Action("GetResourcePolicies")
GetResourcePolicy = Action("GetResourcePolicy")
GetSchema = Action("GetSchema")
GetSchemaByDefinition = Action("GetSchemaByDefinition")
GetSchemaVersion = Action("GetSchemaVersion")
GetSchemaVersionsDiff = Action("GetSchemaVersionsDiff")
GetSecurityConfiguration = Action("GetSecurityConfiguration")
GetSecurityConfigurations = Action("GetSecurityConfigurations")
GetSession = Action("GetSession")
GetStatement = Action("GetStatement")
GetTable = Action("GetTable")
GetTableVersion = Action("GetTableVersion")
GetTableVersions = Action("GetTableVersions")
GetTables = Action("GetTables")
GetTags = Action("GetTags")
GetTrigger = Action("GetTrigger")
GetTriggers = Action("GetTriggers")
GetUserDefinedFunction = Action("GetUserDefinedFunction")
GetUserDefinedFunctions = Action("GetUserDefinedFunctions")
GetWorkflow = Action("GetWorkflow")
GetWorkflowRun = Action("GetWorkflowRun")
GetWorkflowRunProperties = Action("GetWorkflowRunProperties")
GetWorkflowRuns = Action("GetWorkflowRuns")
ImportCatalogToGlue = Action("ImportCatalogToGlue")
ListCrawlers = Action("ListCrawlers")
ListDevEndpoints = Action("ListDevEndpoints")
ListJobs = Action("ListJobs")
ListMLTransforms = Action("ListMLTransforms")
ListRegistries = Action("ListRegistries")
ListSchemaVersions = Action("ListSchemaVersions")
ListSchemas = Action("ListSchemas")
ListSessions = Action("ListSessions")
ListStatements = Action("ListStatements")
ListTriggers = Action("ListTriggers")
ListWorkflows = Action("ListWorkflows")
NotifyEvent = Action("NotifyEvent")
PutDataCatalogEncryptionSettings = Action("PutDataCatalogEncryptionSettings")
PutResourcePolicy = Action("PutResourcePolicy")
PutSchemaVersionMetadata = Action("PutSchemaVersionMetadata")
PutWorkflowRunProperties = Action("PutWorkflowRunProperties")
QuerySchemaVersionMetadata = Action("QuerySchemaVersionMetadata")
RegisterSchemaVersion = Action("RegisterSchemaVersion")
RemoveSchemaVersionMetadata = Action("RemoveSchemaVersionMetadata")
ResetJobBookmark = Action("ResetJobBookmark")
ResumeWorkflowRun = Action("ResumeWorkflowRun")
RunStatement = Action("RunStatement")
SearchTables = Action("SearchTables")
StartCrawler = Action("StartCrawler")
StartCrawlerSchedule = Action("StartCrawlerSchedule")
StartExportLabelsTaskRun = Action("StartExportLabelsTaskRun")
StartImportLabelsTaskRun = Action("StartImportLabelsTaskRun")
StartJobRun = Action("StartJobRun")
StartMLEvaluationTaskRun = Action("StartMLEvaluationTaskRun")
StartMLLabelingSetGenerationTaskRun = Action("StartMLLabelingSetGenerationTaskRun")
StartTrigger = Action("StartTrigger")
StartWorkflowRun = Action("StartWorkflowRun")
StopCrawler = Action("StopCrawler")
StopCrawlerSchedule = Action("StopCrawlerSchedule")
StopSession = Action("StopSession")
StopTrigger = Action("StopTrigger")
StopWorkflowRun = Action("StopWorkflowRun")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateClassifier = Action("UpdateClassifier")
UpdateColumnStatisticsForPartition = Action("UpdateColumnStatisticsForPartition")
UpdateColumnStatisticsForTable = Action("UpdateColumnStatisticsForTable")
UpdateConnection = Action("UpdateConnection")
UpdateCrawler = Action("UpdateCrawler")
UpdateCrawlerSchedule = Action("UpdateCrawlerSchedule")
UpdateDatabase = Action("UpdateDatabase")
UpdateDevEndpoint = Action("UpdateDevEndpoint")
UpdateJob = Action("UpdateJob")
UpdateMLTransform = Action("UpdateMLTransform")
UpdatePartition = Action("UpdatePartition")
UpdateRegistry = Action("UpdateRegistry")
UpdateSchema = Action("UpdateSchema")
UpdateTable = Action("UpdateTable")
UpdateTrigger = Action("UpdateTrigger")
UpdateUserDefinedFunction = Action("UpdateUserDefinedFunction")
UpdateWorkflow = Action("UpdateWorkflow")
UseMLTransforms = Action("UseMLTransforms")
