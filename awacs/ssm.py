# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = 'AWS Systems Manager'
prefix = 'ssm'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AddTagsToResource = Action('AddTagsToResource')
CancelCommand = Action('CancelCommand')
CancelMaintenanceWindowExecution = \
    Action('CancelMaintenanceWindowExecution')
CreateActivation = Action('CreateActivation')
CreateAssociation = Action('CreateAssociation')
CreateAssociationBatch = Action('CreateAssociationBatch')
CreateDocument = Action('CreateDocument')
CreateMaintenanceWindow = Action('CreateMaintenanceWindow')
CreateOpsItem = Action('CreateOpsItem')
CreateOpsMetadata = Action('CreateOpsMetadata')
CreatePatchBaseline = Action('CreatePatchBaseline')
CreateResourceDataSync = Action('CreateResourceDataSync')
DeleteActivation = Action('DeleteActivation')
DeleteAssociation = Action('DeleteAssociation')
DeleteDocument = Action('DeleteDocument')
DeleteInventory = Action('DeleteInventory')
DeleteMaintenanceWindow = Action('DeleteMaintenanceWindow')
DeleteOpsMetadata = Action('DeleteOpsMetadata')
DeleteParameter = Action('DeleteParameter')
DeleteParameters = Action('DeleteParameters')
DeletePatchBaseline = Action('DeletePatchBaseline')
DeleteResourceDataSync = Action('DeleteResourceDataSync')
DeregisterManagedInstance = Action('DeregisterManagedInstance')
DeregisterPatchBaselineForPatchGroup = \
    Action('DeregisterPatchBaselineForPatchGroup')
DeregisterTargetFromMaintenanceWindow = \
    Action('DeregisterTargetFromMaintenanceWindow')
DeregisterTaskFromMaintenanceWindow = \
    Action('DeregisterTaskFromMaintenanceWindow')
DescribeActivations = Action('DescribeActivations')
DescribeAssociation = Action('DescribeAssociation')
DescribeAssociationExecutionTargets = \
    Action('DescribeAssociationExecutionTargets')
DescribeAssociationExecutions = Action('DescribeAssociationExecutions')
DescribeAutomationExecutions = Action('DescribeAutomationExecutions')
DescribeAutomationStepExecutions = \
    Action('DescribeAutomationStepExecutions')
DescribeAvailablePatches = Action('DescribeAvailablePatches')
DescribeDocument = Action('DescribeDocument')
DescribeDocumentParameters = Action('DescribeDocumentParameters')
DescribeDocumentPermission = Action('DescribeDocumentPermission')
DescribeEffectiveInstanceAssociations = \
    Action('DescribeEffectiveInstanceAssociations')
DescribeEffectivePatchesForPatchBaseline = \
    Action('DescribeEffectivePatchesForPatchBaseline')
DescribeInstanceAssociationsStatus = \
    Action('DescribeInstanceAssociationsStatus')
DescribeInstanceInformation = Action('DescribeInstanceInformation')
DescribeInstancePatchStates = Action('DescribeInstancePatchStates')
DescribeInstancePatchStatesForPatchGroup = \
    Action('DescribeInstancePatchStatesForPatchGroup')
DescribeInstancePatches = Action('DescribeInstancePatches')
DescribeInstanceProperties = Action('DescribeInstanceProperties')
DescribeInventoryDeletions = Action('DescribeInventoryDeletions')
DescribeMaintenanceWindowExecutionTaskInvocations = \
    Action('DescribeMaintenanceWindowExecutionTaskInvocations')
DescribeMaintenanceWindowExecutionTasks = \
    Action('DescribeMaintenanceWindowExecutionTasks')
DescribeMaintenanceWindowExecutions = \
    Action('DescribeMaintenanceWindowExecutions')
DescribeMaintenanceWindowSchedule = \
    Action('DescribeMaintenanceWindowSchedule')
DescribeMaintenanceWindowTargets = \
    Action('DescribeMaintenanceWindowTargets')
DescribeMaintenanceWindowTasks = Action('DescribeMaintenanceWindowTasks')
DescribeMaintenanceWindows = Action('DescribeMaintenanceWindows')
DescribeMaintenanceWindowsForTarget = \
    Action('DescribeMaintenanceWindowsForTarget')
DescribeOpsItems = Action('DescribeOpsItems')
DescribeParameters = Action('DescribeParameters')
DescribePatchBaselines = Action('DescribePatchBaselines')
DescribePatchGroupState = Action('DescribePatchGroupState')
DescribePatchGroups = Action('DescribePatchGroups')
DescribePatchProperties = Action('DescribePatchProperties')
DescribeSessions = Action('DescribeSessions')
GetAutomationExecution = Action('GetAutomationExecution')
GetCalendarState = Action('GetCalendarState')
GetCommandInvocation = Action('GetCommandInvocation')
GetConnectionStatus = Action('GetConnectionStatus')
GetDefaultPatchBaseline = Action('GetDefaultPatchBaseline')
GetDeployablePatchSnapshotForInstance = \
    Action('GetDeployablePatchSnapshotForInstance')
GetDocument = Action('GetDocument')
GetInventory = Action('GetInventory')
GetInventorySchema = Action('GetInventorySchema')
GetMaintenanceWindow = Action('GetMaintenanceWindow')
GetMaintenanceWindowExecution = Action('GetMaintenanceWindowExecution')
GetMaintenanceWindowExecutionTask = \
    Action('GetMaintenanceWindowExecutionTask')
GetMaintenanceWindowExecutionTaskInvocation = \
    Action('GetMaintenanceWindowExecutionTaskInvocation')
GetMaintenanceWindowTask = Action('GetMaintenanceWindowTask')
GetManifest = Action('GetManifest')
GetOpsItem = Action('GetOpsItem')
GetOpsMetadata = Action('GetOpsMetadata')
GetOpsSummary = Action('GetOpsSummary')
GetParameter = Action('GetParameter')
GetParameterHistory = Action('GetParameterHistory')
GetParameters = Action('GetParameters')
GetParametersByPath = Action('GetParametersByPath')
GetPatchBaseline = Action('GetPatchBaseline')
GetPatchBaselineForPatchGroup = Action('GetPatchBaselineForPatchGroup')
GetServiceSetting = Action('GetServiceSetting')
LabelParameterVersion = Action('LabelParameterVersion')
ListAssociationVersions = Action('ListAssociationVersions')
ListAssociations = Action('ListAssociations')
ListCommandInvocations = Action('ListCommandInvocations')
ListCommands = Action('ListCommands')
ListComplianceItems = Action('ListComplianceItems')
ListComplianceSummaries = Action('ListComplianceSummaries')
ListDocumentMetadataHistory = Action('ListDocumentMetadataHistory')
ListDocumentVersions = Action('ListDocumentVersions')
ListDocuments = Action('ListDocuments')
ListInstanceAssociations = Action('ListInstanceAssociations')
ListInventoryEntries = Action('ListInventoryEntries')
ListOpsItemEvents = Action('ListOpsItemEvents')
ListOpsMetadata = Action('ListOpsMetadata')
ListResourceComplianceSummaries = \
    Action('ListResourceComplianceSummaries')
ListResourceDataSync = Action('ListResourceDataSync')
ListTagsForResource = Action('ListTagsForResource')
ModifyDocumentPermission = Action('ModifyDocumentPermission')
PutComplianceItems = Action('PutComplianceItems')
PutConfigurePackageResult = Action('PutConfigurePackageResult')
PutInventory = Action('PutInventory')
PutParameter = Action('PutParameter')
RegisterDefaultPatchBaseline = Action('RegisterDefaultPatchBaseline')
RegisterPatchBaselineForPatchGroup = \
    Action('RegisterPatchBaselineForPatchGroup')
RegisterTargetWithMaintenanceWindow = \
    Action('RegisterTargetWithMaintenanceWindow')
RegisterTaskWithMaintenanceWindow = \
    Action('RegisterTaskWithMaintenanceWindow')
RemoveTagsFromResource = Action('RemoveTagsFromResource')
ResetServiceSetting = Action('ResetServiceSetting')
ResumeSession = Action('ResumeSession')
SendAutomationSignal = Action('SendAutomationSignal')
SendCommand = Action('SendCommand')
StartAssociationsOnce = Action('StartAssociationsOnce')
StartAutomationExecution = Action('StartAutomationExecution')
StartChangeRequestExecution = Action('StartChangeRequestExecution')
StartSession = Action('StartSession')
StopAutomationExecution = Action('StopAutomationExecution')
TerminateSession = Action('TerminateSession')
UpdateAssociation = Action('UpdateAssociation')
UpdateAssociationStatus = Action('UpdateAssociationStatus')
UpdateDocument = Action('UpdateDocument')
UpdateDocumentDefaultVersion = Action('UpdateDocumentDefaultVersion')
UpdateDocumentMetadata = Action('UpdateDocumentMetadata')
UpdateInstanceAssociationStatus = \
    Action('UpdateInstanceAssociationStatus')
UpdateInstanceInformation = Action('UpdateInstanceInformation')
UpdateMaintenanceWindow = Action('UpdateMaintenanceWindow')
UpdateMaintenanceWindowTarget = Action('UpdateMaintenanceWindowTarget')
UpdateMaintenanceWindowTask = Action('UpdateMaintenanceWindowTask')
UpdateManagedInstanceRole = Action('UpdateManagedInstanceRole')
UpdateOpsItem = Action('UpdateOpsItem')
UpdateOpsMetadata = Action('UpdateOpsMetadata')
UpdatePatchBaseline = Action('UpdatePatchBaseline')
UpdateResourceDataSync = Action('UpdateResourceDataSync')
UpdateServiceSetting = Action('UpdateServiceSetting')
