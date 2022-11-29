# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Pinpoint"
prefix = "mobiletargeting"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateApp = Action("CreateApp")
CreateCampaign = Action("CreateCampaign")
CreateEmailTemplate = Action("CreateEmailTemplate")
CreateExportJob = Action("CreateExportJob")
CreateImportJob = Action("CreateImportJob")
CreateInAppTemplate = Action("CreateInAppTemplate")
CreateJourney = Action("CreateJourney")
CreatePushTemplate = Action("CreatePushTemplate")
CreateRecommenderConfiguration = Action("CreateRecommenderConfiguration")
CreateSegment = Action("CreateSegment")
CreateSmsTemplate = Action("CreateSmsTemplate")
CreateVoiceTemplate = Action("CreateVoiceTemplate")
DeleteAdmChannel = Action("DeleteAdmChannel")
DeleteApnsChannel = Action("DeleteApnsChannel")
DeleteApnsSandboxChannel = Action("DeleteApnsSandboxChannel")
DeleteApnsVoipChannel = Action("DeleteApnsVoipChannel")
DeleteApnsVoipSandboxChannel = Action("DeleteApnsVoipSandboxChannel")
DeleteApp = Action("DeleteApp")
DeleteBaiduChannel = Action("DeleteBaiduChannel")
DeleteCampaign = Action("DeleteCampaign")
DeleteEmailChannel = Action("DeleteEmailChannel")
DeleteEmailTemplate = Action("DeleteEmailTemplate")
DeleteEndpoint = Action("DeleteEndpoint")
DeleteEventStream = Action("DeleteEventStream")
DeleteGcmChannel = Action("DeleteGcmChannel")
DeleteInAppTemplate = Action("DeleteInAppTemplate")
DeleteJourney = Action("DeleteJourney")
DeletePushTemplate = Action("DeletePushTemplate")
DeleteRecommenderConfiguration = Action("DeleteRecommenderConfiguration")
DeleteSegment = Action("DeleteSegment")
DeleteSmsChannel = Action("DeleteSmsChannel")
DeleteSmsTemplate = Action("DeleteSmsTemplate")
DeleteUserEndpoints = Action("DeleteUserEndpoints")
DeleteVoiceChannel = Action("DeleteVoiceChannel")
DeleteVoiceTemplate = Action("DeleteVoiceTemplate")
GetAdmChannel = Action("GetAdmChannel")
GetApnsChannel = Action("GetApnsChannel")
GetApnsSandboxChannel = Action("GetApnsSandboxChannel")
GetApnsVoipChannel = Action("GetApnsVoipChannel")
GetApnsVoipSandboxChannel = Action("GetApnsVoipSandboxChannel")
GetApp = Action("GetApp")
GetApplicationDateRangeKpi = Action("GetApplicationDateRangeKpi")
GetApplicationSettings = Action("GetApplicationSettings")
GetApps = Action("GetApps")
GetBaiduChannel = Action("GetBaiduChannel")
GetCampaign = Action("GetCampaign")
GetCampaignActivities = Action("GetCampaignActivities")
GetCampaignDateRangeKpi = Action("GetCampaignDateRangeKpi")
GetCampaignVersion = Action("GetCampaignVersion")
GetCampaignVersions = Action("GetCampaignVersions")
GetCampaigns = Action("GetCampaigns")
GetChannels = Action("GetChannels")
GetEmailChannel = Action("GetEmailChannel")
GetEmailTemplate = Action("GetEmailTemplate")
GetEndpoint = Action("GetEndpoint")
GetEventStream = Action("GetEventStream")
GetExportJob = Action("GetExportJob")
GetExportJobs = Action("GetExportJobs")
GetGcmChannel = Action("GetGcmChannel")
GetImportJob = Action("GetImportJob")
GetImportJobs = Action("GetImportJobs")
GetInAppMessages = Action("GetInAppMessages")
GetInAppTemplate = Action("GetInAppTemplate")
GetJourney = Action("GetJourney")
GetJourneyDateRangeKpi = Action("GetJourneyDateRangeKpi")
GetJourneyExecutionActivityMetrics = Action("GetJourneyExecutionActivityMetrics")
GetJourneyExecutionMetrics = Action("GetJourneyExecutionMetrics")
GetPushTemplate = Action("GetPushTemplate")
GetRecommenderConfiguration = Action("GetRecommenderConfiguration")
GetRecommenderConfigurations = Action("GetRecommenderConfigurations")
GetReports = Action("GetReports")
GetSegment = Action("GetSegment")
GetSegmentExportJobs = Action("GetSegmentExportJobs")
GetSegmentImportJobs = Action("GetSegmentImportJobs")
GetSegmentVersion = Action("GetSegmentVersion")
GetSegmentVersions = Action("GetSegmentVersions")
GetSegments = Action("GetSegments")
GetSmsChannel = Action("GetSmsChannel")
GetSmsTemplate = Action("GetSmsTemplate")
GetUserEndpoints = Action("GetUserEndpoints")
GetVoiceChannel = Action("GetVoiceChannel")
GetVoiceTemplate = Action("GetVoiceTemplate")
ListJourneys = Action("ListJourneys")
ListTagsForResource = Action("ListTagsForResource")
ListTemplateVersions = Action("ListTemplateVersions")
ListTemplates = Action("ListTemplates")
PhoneNumberValidate = Action("PhoneNumberValidate")
PutEventStream = Action("PutEventStream")
PutEvents = Action("PutEvents")
RemoveAttributes = Action("RemoveAttributes")
SendMessages = Action("SendMessages")
SendOTPMessage = Action("SendOTPMessage")
SendUsersMessages = Action("SendUsersMessages")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAdmChannel = Action("UpdateAdmChannel")
UpdateApnsChannel = Action("UpdateApnsChannel")
UpdateApnsSandboxChannel = Action("UpdateApnsSandboxChannel")
UpdateApnsVoipChannel = Action("UpdateApnsVoipChannel")
UpdateApnsVoipSandboxChannel = Action("UpdateApnsVoipSandboxChannel")
UpdateApplicationSettings = Action("UpdateApplicationSettings")
UpdateBaiduChannel = Action("UpdateBaiduChannel")
UpdateCampaign = Action("UpdateCampaign")
UpdateEmailChannel = Action("UpdateEmailChannel")
UpdateEmailTemplate = Action("UpdateEmailTemplate")
UpdateEndpoint = Action("UpdateEndpoint")
UpdateEndpointsBatch = Action("UpdateEndpointsBatch")
UpdateGcmChannel = Action("UpdateGcmChannel")
UpdateInAppTemplate = Action("UpdateInAppTemplate")
UpdateJourney = Action("UpdateJourney")
UpdateJourneyState = Action("UpdateJourneyState")
UpdatePushTemplate = Action("UpdatePushTemplate")
UpdateRecommenderConfiguration = Action("UpdateRecommenderConfiguration")
UpdateSegment = Action("UpdateSegment")
UpdateSmsChannel = Action("UpdateSmsChannel")
UpdateSmsTemplate = Action("UpdateSmsTemplate")
UpdateTemplateActiveVersion = Action("UpdateTemplateActiveVersion")
UpdateVoiceChannel = Action("UpdateVoiceChannel")
UpdateVoiceTemplate = Action("UpdateVoiceTemplate")
VerifyOTPMessage = Action("VerifyOTPMessage")
