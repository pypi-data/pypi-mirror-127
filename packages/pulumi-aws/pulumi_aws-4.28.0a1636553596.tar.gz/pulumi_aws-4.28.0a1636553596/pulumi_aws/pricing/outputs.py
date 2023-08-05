# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetProductFilterResult',
]

@pulumi.output_type
class GetProductFilterResult(dict):
    def __init__(__self__, *,
                 field: str,
                 value: str):
        """
        :param str field: The product attribute name that you want to filter on.
        :param str value: The product attribute value that you want to filter on.
        """
        pulumi.set(__self__, "field", field)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def field(self) -> str:
        """
        The product attribute name that you want to filter on.
        """
        return pulumi.get(self, "field")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The product attribute value that you want to filter on.
        """
        return pulumi.get(self, "value")


