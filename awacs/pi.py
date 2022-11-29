# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Performance Insights"
prefix = "pi"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


DescribeDimensionKeys = Action("DescribeDimensionKeys")
GetDimensionKeyDetails = Action("GetDimensionKeyDetails")
GetResourceMetadata = Action("GetResourceMetadata")
GetResourceMetrics = Action("GetResourceMetrics")
ListAvailableResourceDimensions = Action("ListAvailableResourceDimensions")
ListAvailableResourceMetrics = Action("ListAvailableResourceMetrics")
