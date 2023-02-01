# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS CloudTrail"
prefix = "cloudtrail"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddTags = Action("AddTags")
CancelQuery = Action("CancelQuery")
CreateEventDataStore = Action("CreateEventDataStore")
CreateServiceLinkedChannel = Action("CreateServiceLinkedChannel")
CreateTrail = Action("CreateTrail")
DeleteEventDataStore = Action("DeleteEventDataStore")
DeleteServiceLinkedChannel = Action("DeleteServiceLinkedChannel")
DeleteTrail = Action("DeleteTrail")
DeregisterOrganizationDelegatedAdmin = Action("DeregisterOrganizationDelegatedAdmin")
DescribeQuery = Action("DescribeQuery")
DescribeTrails = Action("DescribeTrails")
GetChannel = Action("GetChannel")
GetEventDataStore = Action("GetEventDataStore")
GetEventSelectors = Action("GetEventSelectors")
GetImport = Action("GetImport")
GetInsightSelectors = Action("GetInsightSelectors")
GetQueryResults = Action("GetQueryResults")
GetServiceLinkedChannel = Action("GetServiceLinkedChannel")
GetTrail = Action("GetTrail")
GetTrailStatus = Action("GetTrailStatus")
ListChannels = Action("ListChannels")
ListEventDataStores = Action("ListEventDataStores")
ListImportFailures = Action("ListImportFailures")
ListImports = Action("ListImports")
ListPublicKeys = Action("ListPublicKeys")
ListQueries = Action("ListQueries")
ListServiceLinkedChannels = Action("ListServiceLinkedChannels")
ListTags = Action("ListTags")
ListTrails = Action("ListTrails")
LookupEvents = Action("LookupEvents")
PutEventSelectors = Action("PutEventSelectors")
PutInsightSelectors = Action("PutInsightSelectors")
RegisterOrganizationDelegatedAdmin = Action("RegisterOrganizationDelegatedAdmin")
RemoveTags = Action("RemoveTags")
RestoreEventDataStore = Action("RestoreEventDataStore")
StartImport = Action("StartImport")
StartLogging = Action("StartLogging")
StartQuery = Action("StartQuery")
StopImport = Action("StopImport")
StopLogging = Action("StopLogging")
UpdateEventDataStore = Action("UpdateEventDataStore")
UpdateServiceLinkedChannel = Action("UpdateServiceLinkedChannel")
UpdateTrail = Action("UpdateTrail")
