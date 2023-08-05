# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = [
    'GetNetworkAclsResult',
    'AwaitableGetNetworkAclsResult',
    'get_network_acls',
    'get_network_acls_output',
]

@pulumi.output_type
class GetNetworkAclsResult:
    """
    A collection of values returned by getNetworkAcls.
    """
    def __init__(__self__, filters=None, id=None, ids=None, tags=None, vpc_id=None):
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if vpc_id and not isinstance(vpc_id, str):
            raise TypeError("Expected argument 'vpc_id' to be a str")
        pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetNetworkAclsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ids(self) -> Sequence[str]:
        """
        A list of all the network ACL ids found. This data source will fail if none are found.
        """
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[str]:
        return pulumi.get(self, "vpc_id")


class AwaitableGetNetworkAclsResult(GetNetworkAclsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNetworkAclsResult(
            filters=self.filters,
            id=self.id,
            ids=self.ids,
            tags=self.tags,
            vpc_id=self.vpc_id)


def get_network_acls(filters: Optional[Sequence[pulumi.InputType['GetNetworkAclsFilterArgs']]] = None,
                     tags: Optional[Mapping[str, str]] = None,
                     vpc_id: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNetworkAclsResult:
    """
    ## Example Usage

    The following shows outputing all network ACL ids in a vpc.

    ```python
    import pulumi
    import pulumi_aws as aws

    example_network_acls = aws.ec2.get_network_acls(vpc_id=var["vpc_id"])
    pulumi.export("example", example_network_acls.ids)
    ```

    The following example retrieves a list of all network ACL ids in a VPC with a custom
    tag of `Tier` set to a value of "Private".

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.ec2.get_network_acls(vpc_id=var["vpc_id"],
        tags={
            "Tier": "Private",
        })
    ```

    The following example retrieves a network ACL id in a VPC which associated
    with specific subnet.

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.ec2.get_network_acls(vpc_id=var["vpc_id"],
        filters=[aws.ec2.GetNetworkAclsFilterArgs(
            name="association.subnet-id",
            values=[aws_subnet["test"]["id"]],
        )])
    ```


    :param Sequence[pulumi.InputType['GetNetworkAclsFilterArgs']] filters: Custom filter block as described below.
    :param Mapping[str, str] tags: A map of tags, each pair of which must exactly match
           a pair on the desired network ACLs.
    :param str vpc_id: The VPC ID that you want to filter from.
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['tags'] = tags
    __args__['vpcId'] = vpc_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:ec2/getNetworkAcls:getNetworkAcls', __args__, opts=opts, typ=GetNetworkAclsResult).value

    return AwaitableGetNetworkAclsResult(
        filters=__ret__.filters,
        id=__ret__.id,
        ids=__ret__.ids,
        tags=__ret__.tags,
        vpc_id=__ret__.vpc_id)


@_utilities.lift_output_func(get_network_acls)
def get_network_acls_output(filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetNetworkAclsFilterArgs']]]]] = None,
                            tags: Optional[pulumi.Input[Optional[Mapping[str, str]]]] = None,
                            vpc_id: Optional[pulumi.Input[Optional[str]]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNetworkAclsResult]:
    """
    ## Example Usage

    The following shows outputing all network ACL ids in a vpc.

    ```python
    import pulumi
    import pulumi_aws as aws

    example_network_acls = aws.ec2.get_network_acls(vpc_id=var["vpc_id"])
    pulumi.export("example", example_network_acls.ids)
    ```

    The following example retrieves a list of all network ACL ids in a VPC with a custom
    tag of `Tier` set to a value of "Private".

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.ec2.get_network_acls(vpc_id=var["vpc_id"],
        tags={
            "Tier": "Private",
        })
    ```

    The following example retrieves a network ACL id in a VPC which associated
    with specific subnet.

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.ec2.get_network_acls(vpc_id=var["vpc_id"],
        filters=[aws.ec2.GetNetworkAclsFilterArgs(
            name="association.subnet-id",
            values=[aws_subnet["test"]["id"]],
        )])
    ```


    :param Sequence[pulumi.InputType['GetNetworkAclsFilterArgs']] filters: Custom filter block as described below.
    :param Mapping[str, str] tags: A map of tags, each pair of which must exactly match
           a pair on the desired network ACLs.
    :param str vpc_id: The VPC ID that you want to filter from.
    """
    ...
