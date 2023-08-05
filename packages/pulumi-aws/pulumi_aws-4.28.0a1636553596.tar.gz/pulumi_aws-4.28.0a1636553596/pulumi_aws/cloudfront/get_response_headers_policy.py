# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetResponseHeadersPolicyResult',
    'AwaitableGetResponseHeadersPolicyResult',
    'get_response_headers_policy',
    'get_response_headers_policy_output',
]

@pulumi.output_type
class GetResponseHeadersPolicyResult:
    """
    A collection of values returned by getResponseHeadersPolicy.
    """
    def __init__(__self__, comment=None, cors_configs=None, custom_headers_configs=None, etag=None, id=None, name=None, security_headers_configs=None):
        if comment and not isinstance(comment, str):
            raise TypeError("Expected argument 'comment' to be a str")
        pulumi.set(__self__, "comment", comment)
        if cors_configs and not isinstance(cors_configs, list):
            raise TypeError("Expected argument 'cors_configs' to be a list")
        pulumi.set(__self__, "cors_configs", cors_configs)
        if custom_headers_configs and not isinstance(custom_headers_configs, list):
            raise TypeError("Expected argument 'custom_headers_configs' to be a list")
        pulumi.set(__self__, "custom_headers_configs", custom_headers_configs)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if security_headers_configs and not isinstance(security_headers_configs, list):
            raise TypeError("Expected argument 'security_headers_configs' to be a list")
        pulumi.set(__self__, "security_headers_configs", security_headers_configs)

    @property
    @pulumi.getter
    def comment(self) -> str:
        """
        A comment to describe the response headers policy. The comment cannot be longer than 128 characters.
        """
        return pulumi.get(self, "comment")

    @property
    @pulumi.getter(name="corsConfigs")
    def cors_configs(self) -> Sequence['outputs.GetResponseHeadersPolicyCorsConfigResult']:
        """
        A configuration for a set of HTTP response headers that are used for Cross-Origin Resource Sharing (CORS). See Cors Config for more information.
        """
        return pulumi.get(self, "cors_configs")

    @property
    @pulumi.getter(name="customHeadersConfigs")
    def custom_headers_configs(self) -> Sequence['outputs.GetResponseHeadersPolicyCustomHeadersConfigResult']:
        """
        Object that contains an attribute `items` that contains a list of Custom Headers See Custom Header for more information.
        """
        return pulumi.get(self, "custom_headers_configs")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        The current version of the response headers policy.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="securityHeadersConfigs")
    def security_headers_configs(self) -> Sequence['outputs.GetResponseHeadersPolicySecurityHeadersConfigResult']:
        """
        A configuration for a set of security-related HTTP response headers. See Security Headers Config for more information.
        """
        return pulumi.get(self, "security_headers_configs")


class AwaitableGetResponseHeadersPolicyResult(GetResponseHeadersPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetResponseHeadersPolicyResult(
            comment=self.comment,
            cors_configs=self.cors_configs,
            custom_headers_configs=self.custom_headers_configs,
            etag=self.etag,
            id=self.id,
            name=self.name,
            security_headers_configs=self.security_headers_configs)


def get_response_headers_policy(id: Optional[str] = None,
                                name: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetResponseHeadersPolicyResult:
    """
    Use this data source to retrieve information about a CloudFront cache policy.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.cloudfront.get_response_headers_policy(name="example-policy")
    ```


    :param str id: The identifier for the response headers policy.
    :param str name: A unique name to identify the response headers policy.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:cloudfront/getResponseHeadersPolicy:getResponseHeadersPolicy', __args__, opts=opts, typ=GetResponseHeadersPolicyResult).value

    return AwaitableGetResponseHeadersPolicyResult(
        comment=__ret__.comment,
        cors_configs=__ret__.cors_configs,
        custom_headers_configs=__ret__.custom_headers_configs,
        etag=__ret__.etag,
        id=__ret__.id,
        name=__ret__.name,
        security_headers_configs=__ret__.security_headers_configs)


@_utilities.lift_output_func(get_response_headers_policy)
def get_response_headers_policy_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                                       name: Optional[pulumi.Input[Optional[str]]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetResponseHeadersPolicyResult]:
    """
    Use this data source to retrieve information about a CloudFront cache policy.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.cloudfront.get_response_headers_policy(name="example-policy")
    ```


    :param str id: The identifier for the response headers policy.
    :param str name: A unique name to identify the response headers policy.
    """
    ...
