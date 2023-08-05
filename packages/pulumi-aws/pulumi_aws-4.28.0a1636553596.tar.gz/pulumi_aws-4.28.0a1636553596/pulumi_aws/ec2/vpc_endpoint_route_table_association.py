# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['VpcEndpointRouteTableAssociationArgs', 'VpcEndpointRouteTableAssociation']

@pulumi.input_type
class VpcEndpointRouteTableAssociationArgs:
    def __init__(__self__, *,
                 route_table_id: pulumi.Input[str],
                 vpc_endpoint_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a VpcEndpointRouteTableAssociation resource.
        :param pulumi.Input[str] route_table_id: Identifier of the EC2 Route Table to be associated with the VPC Endpoint.
        :param pulumi.Input[str] vpc_endpoint_id: Identifier of the VPC Endpoint with which the EC2 Route Table will be associated.
        """
        pulumi.set(__self__, "route_table_id", route_table_id)
        pulumi.set(__self__, "vpc_endpoint_id", vpc_endpoint_id)

    @property
    @pulumi.getter(name="routeTableId")
    def route_table_id(self) -> pulumi.Input[str]:
        """
        Identifier of the EC2 Route Table to be associated with the VPC Endpoint.
        """
        return pulumi.get(self, "route_table_id")

    @route_table_id.setter
    def route_table_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "route_table_id", value)

    @property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> pulumi.Input[str]:
        """
        Identifier of the VPC Endpoint with which the EC2 Route Table will be associated.
        """
        return pulumi.get(self, "vpc_endpoint_id")

    @vpc_endpoint_id.setter
    def vpc_endpoint_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "vpc_endpoint_id", value)


@pulumi.input_type
class _VpcEndpointRouteTableAssociationState:
    def __init__(__self__, *,
                 route_table_id: Optional[pulumi.Input[str]] = None,
                 vpc_endpoint_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering VpcEndpointRouteTableAssociation resources.
        :param pulumi.Input[str] route_table_id: Identifier of the EC2 Route Table to be associated with the VPC Endpoint.
        :param pulumi.Input[str] vpc_endpoint_id: Identifier of the VPC Endpoint with which the EC2 Route Table will be associated.
        """
        if route_table_id is not None:
            pulumi.set(__self__, "route_table_id", route_table_id)
        if vpc_endpoint_id is not None:
            pulumi.set(__self__, "vpc_endpoint_id", vpc_endpoint_id)

    @property
    @pulumi.getter(name="routeTableId")
    def route_table_id(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier of the EC2 Route Table to be associated with the VPC Endpoint.
        """
        return pulumi.get(self, "route_table_id")

    @route_table_id.setter
    def route_table_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "route_table_id", value)

    @property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier of the VPC Endpoint with which the EC2 Route Table will be associated.
        """
        return pulumi.get(self, "vpc_endpoint_id")

    @vpc_endpoint_id.setter
    def vpc_endpoint_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpc_endpoint_id", value)


class VpcEndpointRouteTableAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 route_table_id: Optional[pulumi.Input[str]] = None,
                 vpc_endpoint_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a VPC Endpoint Route Table Association

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.ec2.VpcEndpointRouteTableAssociation("example",
            route_table_id=aws_route_table["example"]["id"],
            vpc_endpoint_id=aws_vpc_endpoint["example"]["id"])
        ```

        ## Import

        VPC Endpoint Route Table Associations can be imported using `vpc_endpoint_id` together with `route_table_id`, e.g.,

        ```sh
         $ pulumi import aws:ec2/vpcEndpointRouteTableAssociation:VpcEndpointRouteTableAssociation example vpce-aaaaaaaa/rtb-bbbbbbbb
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] route_table_id: Identifier of the EC2 Route Table to be associated with the VPC Endpoint.
        :param pulumi.Input[str] vpc_endpoint_id: Identifier of the VPC Endpoint with which the EC2 Route Table will be associated.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VpcEndpointRouteTableAssociationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a VPC Endpoint Route Table Association

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.ec2.VpcEndpointRouteTableAssociation("example",
            route_table_id=aws_route_table["example"]["id"],
            vpc_endpoint_id=aws_vpc_endpoint["example"]["id"])
        ```

        ## Import

        VPC Endpoint Route Table Associations can be imported using `vpc_endpoint_id` together with `route_table_id`, e.g.,

        ```sh
         $ pulumi import aws:ec2/vpcEndpointRouteTableAssociation:VpcEndpointRouteTableAssociation example vpce-aaaaaaaa/rtb-bbbbbbbb
        ```

        :param str resource_name: The name of the resource.
        :param VpcEndpointRouteTableAssociationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VpcEndpointRouteTableAssociationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 route_table_id: Optional[pulumi.Input[str]] = None,
                 vpc_endpoint_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VpcEndpointRouteTableAssociationArgs.__new__(VpcEndpointRouteTableAssociationArgs)

            if route_table_id is None and not opts.urn:
                raise TypeError("Missing required property 'route_table_id'")
            __props__.__dict__["route_table_id"] = route_table_id
            if vpc_endpoint_id is None and not opts.urn:
                raise TypeError("Missing required property 'vpc_endpoint_id'")
            __props__.__dict__["vpc_endpoint_id"] = vpc_endpoint_id
        super(VpcEndpointRouteTableAssociation, __self__).__init__(
            'aws:ec2/vpcEndpointRouteTableAssociation:VpcEndpointRouteTableAssociation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            route_table_id: Optional[pulumi.Input[str]] = None,
            vpc_endpoint_id: Optional[pulumi.Input[str]] = None) -> 'VpcEndpointRouteTableAssociation':
        """
        Get an existing VpcEndpointRouteTableAssociation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] route_table_id: Identifier of the EC2 Route Table to be associated with the VPC Endpoint.
        :param pulumi.Input[str] vpc_endpoint_id: Identifier of the VPC Endpoint with which the EC2 Route Table will be associated.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _VpcEndpointRouteTableAssociationState.__new__(_VpcEndpointRouteTableAssociationState)

        __props__.__dict__["route_table_id"] = route_table_id
        __props__.__dict__["vpc_endpoint_id"] = vpc_endpoint_id
        return VpcEndpointRouteTableAssociation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="routeTableId")
    def route_table_id(self) -> pulumi.Output[str]:
        """
        Identifier of the EC2 Route Table to be associated with the VPC Endpoint.
        """
        return pulumi.get(self, "route_table_id")

    @property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> pulumi.Output[str]:
        """
        Identifier of the VPC Endpoint with which the EC2 Route Table will be associated.
        """
        return pulumi.get(self, "vpc_endpoint_id")

