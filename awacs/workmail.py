# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon WorkMail"
prefix = "workmail"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddMembersToGroup = Action("AddMembersToGroup")
AssociateDelegateToResource = Action("AssociateDelegateToResource")
AssociateMemberToGroup = Action("AssociateMemberToGroup")
CancelMailboxExportJob = Action("CancelMailboxExportJob")
CreateAlias = Action("CreateAlias")
CreateGroup = Action("CreateGroup")
CreateInboundMailFlowRule = Action("CreateInboundMailFlowRule")
CreateMailDomain = Action("CreateMailDomain")
CreateMailUser = Action("CreateMailUser")
CreateMobileDeviceAccessRule = Action("CreateMobileDeviceAccessRule")
CreateOrganization = Action("CreateOrganization")
CreateOutboundMailFlowRule = Action("CreateOutboundMailFlowRule")
CreateResource = Action("CreateResource")
CreateSmtpGateway = Action("CreateSmtpGateway")
CreateUser = Action("CreateUser")
DeleteAccessControlRule = Action("DeleteAccessControlRule")
DeleteAlias = Action("DeleteAlias")
DeleteEmailMonitoringConfiguration = Action("DeleteEmailMonitoringConfiguration")
DeleteGroup = Action("DeleteGroup")
DeleteInboundMailFlowRule = Action("DeleteInboundMailFlowRule")
DeleteMailDomain = Action("DeleteMailDomain")
DeleteMailboxPermissions = Action("DeleteMailboxPermissions")
DeleteMobileDevice = Action("DeleteMobileDevice")
DeleteMobileDeviceAccessOverride = Action("DeleteMobileDeviceAccessOverride")
DeleteMobileDeviceAccessRule = Action("DeleteMobileDeviceAccessRule")
DeleteOrganization = Action("DeleteOrganization")
DeleteOutboundMailFlowRule = Action("DeleteOutboundMailFlowRule")
DeleteResource = Action("DeleteResource")
DeleteRetentionPolicy = Action("DeleteRetentionPolicy")
DeleteSmtpGateway = Action("DeleteSmtpGateway")
DeleteUser = Action("DeleteUser")
DeregisterFromWorkMail = Action("DeregisterFromWorkMail")
DeregisterMailDomain = Action("DeregisterMailDomain")
DescribeDirectories = Action("DescribeDirectories")
DescribeEmailMonitoringConfiguration = Action("DescribeEmailMonitoringConfiguration")
DescribeGroup = Action("DescribeGroup")
DescribeInboundDmarcSettings = Action("DescribeInboundDmarcSettings")
DescribeInboundMailFlowRule = Action("DescribeInboundMailFlowRule")
DescribeKmsKeys = Action("DescribeKmsKeys")
DescribeMailDomains = Action("DescribeMailDomains")
DescribeMailGroups = Action("DescribeMailGroups")
DescribeMailUsers = Action("DescribeMailUsers")
DescribeMailboxExportJob = Action("DescribeMailboxExportJob")
DescribeOrganization = Action("DescribeOrganization")
DescribeOrganizations = Action("DescribeOrganizations")
DescribeOutboundMailFlowRule = Action("DescribeOutboundMailFlowRule")
DescribeResource = Action("DescribeResource")
DescribeSmtpGateway = Action("DescribeSmtpGateway")
DescribeUser = Action("DescribeUser")
DisableMailGroups = Action("DisableMailGroups")
DisableMailUsers = Action("DisableMailUsers")
DisassociateDelegateFromResource = Action("DisassociateDelegateFromResource")
DisassociateMemberFromGroup = Action("DisassociateMemberFromGroup")
EnableMailDomain = Action("EnableMailDomain")
EnableMailGroups = Action("EnableMailGroups")
EnableMailUsers = Action("EnableMailUsers")
GetAccessControlEffect = Action("GetAccessControlEffect")
GetDefaultRetentionPolicy = Action("GetDefaultRetentionPolicy")
GetJournalingRules = Action("GetJournalingRules")
GetMailDomain = Action("GetMailDomain")
GetMailDomainDetails = Action("GetMailDomainDetails")
GetMailGroupDetails = Action("GetMailGroupDetails")
GetMailUserDetails = Action("GetMailUserDetails")
GetMailboxDetails = Action("GetMailboxDetails")
GetMobileDeviceAccessEffect = Action("GetMobileDeviceAccessEffect")
GetMobileDeviceAccessOverride = Action("GetMobileDeviceAccessOverride")
GetMobileDeviceDetails = Action("GetMobileDeviceDetails")
GetMobileDevicesForUser = Action("GetMobileDevicesForUser")
GetMobilePolicyDetails = Action("GetMobilePolicyDetails")
ListAccessControlRules = Action("ListAccessControlRules")
ListAliases = Action("ListAliases")
ListGroupMembers = Action("ListGroupMembers")
ListGroups = Action("ListGroups")
ListInboundMailFlowRules = Action("ListInboundMailFlowRules")
ListMailDomains = Action("ListMailDomains")
ListMailboxExportJobs = Action("ListMailboxExportJobs")
ListMailboxPermissions = Action("ListMailboxPermissions")
ListMembersInMailGroup = Action("ListMembersInMailGroup")
ListMobileDeviceAccessOverrides = Action("ListMobileDeviceAccessOverrides")
ListMobileDeviceAccessRules = Action("ListMobileDeviceAccessRules")
ListOrganizations = Action("ListOrganizations")
ListOutboundMailFlowRules = Action("ListOutboundMailFlowRules")
ListResourceDelegates = Action("ListResourceDelegates")
ListResources = Action("ListResources")
ListSmtpGateways = Action("ListSmtpGateways")
ListTagsForResource = Action("ListTagsForResource")
ListUsers = Action("ListUsers")
PutAccessControlRule = Action("PutAccessControlRule")
PutEmailMonitoringConfiguration = Action("PutEmailMonitoringConfiguration")
PutInboundDmarcSettings = Action("PutInboundDmarcSettings")
PutMailboxPermissions = Action("PutMailboxPermissions")
PutMobileDeviceAccessOverride = Action("PutMobileDeviceAccessOverride")
PutRetentionPolicy = Action("PutRetentionPolicy")
RegisterMailDomain = Action("RegisterMailDomain")
RegisterToWorkMail = Action("RegisterToWorkMail")
RemoveMembersFromGroup = Action("RemoveMembersFromGroup")
ResetPassword = Action("ResetPassword")
ResetUserPassword = Action("ResetUserPassword")
SearchMembers = Action("SearchMembers")
SetAdmin = Action("SetAdmin")
SetDefaultMailDomain = Action("SetDefaultMailDomain")
SetJournalingRules = Action("SetJournalingRules")
SetMailGroupDetails = Action("SetMailGroupDetails")
SetMailUserDetails = Action("SetMailUserDetails")
SetMobilePolicyDetails = Action("SetMobilePolicyDetails")
StartMailboxExportJob = Action("StartMailboxExportJob")
TagResource = Action("TagResource")
TestInboundMailFlowRules = Action("TestInboundMailFlowRules")
TestOutboundMailFlowRules = Action("TestOutboundMailFlowRules")
UntagResource = Action("UntagResource")
UpdateDefaultMailDomain = Action("UpdateDefaultMailDomain")
UpdateInboundMailFlowRule = Action("UpdateInboundMailFlowRule")
UpdateMailboxQuota = Action("UpdateMailboxQuota")
UpdateMobileDeviceAccessRule = Action("UpdateMobileDeviceAccessRule")
UpdateOutboundMailFlowRule = Action("UpdateOutboundMailFlowRule")
UpdatePrimaryEmailAddress = Action("UpdatePrimaryEmailAddress")
UpdateResource = Action("UpdateResource")
UpdateSmtpGateway = Action("UpdateSmtpGateway")
WipeMobileDevice = Action("WipeMobileDevice")
