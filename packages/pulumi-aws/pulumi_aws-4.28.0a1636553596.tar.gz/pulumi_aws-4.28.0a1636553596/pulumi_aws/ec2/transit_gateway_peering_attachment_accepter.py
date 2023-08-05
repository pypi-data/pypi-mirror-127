# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['TransitGatewayPeeringAttachmentAccepterArgs', 'TransitGatewayPeeringAttachmentAccepter']

@pulumi.input_type
class TransitGatewayPeeringAttachmentAccepterArgs:
    def __init__(__self__, *,
                 transit_gateway_attachment_id: pulumi.Input[str],
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a TransitGatewayPeeringAttachmentAccepter resource.
        :param pulumi.Input[str] transit_gateway_attachment_id: The ID of the EC2 Transit Gateway Peering Attachment to manage.
        """
        pulumi.set(__self__, "transit_gateway_attachment_id", transit_gateway_attachment_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="transitGatewayAttachmentId")
    def transit_gateway_attachment_id(self) -> pulumi.Input[str]:
        """
        The ID of the EC2 Transit Gateway Peering Attachment to manage.
        """
        return pulumi.get(self, "transit_gateway_attachment_id")

    @transit_gateway_attachment_id.setter
    def transit_gateway_attachment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "transit_gateway_attachment_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _TransitGatewayPeeringAttachmentAccepterState:
    def __init__(__self__, *,
                 peer_account_id: Optional[pulumi.Input[str]] = None,
                 peer_region: Optional[pulumi.Input[str]] = None,
                 peer_transit_gateway_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 transit_gateway_attachment_id: Optional[pulumi.Input[str]] = None,
                 transit_gateway_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering TransitGatewayPeeringAttachmentAccepter resources.
        :param pulumi.Input[str] peer_account_id: Identifier of the AWS account that owns the EC2 TGW peering.
        :param pulumi.Input[str] peer_transit_gateway_id: Identifier of EC2 Transit Gateway to peer with.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        :param pulumi.Input[str] transit_gateway_attachment_id: The ID of the EC2 Transit Gateway Peering Attachment to manage.
        :param pulumi.Input[str] transit_gateway_id: Identifier of EC2 Transit Gateway.
        """
        if peer_account_id is not None:
            pulumi.set(__self__, "peer_account_id", peer_account_id)
        if peer_region is not None:
            pulumi.set(__self__, "peer_region", peer_region)
        if peer_transit_gateway_id is not None:
            pulumi.set(__self__, "peer_transit_gateway_id", peer_transit_gateway_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)
        if transit_gateway_attachment_id is not None:
            pulumi.set(__self__, "transit_gateway_attachment_id", transit_gateway_attachment_id)
        if transit_gateway_id is not None:
            pulumi.set(__self__, "transit_gateway_id", transit_gateway_id)

    @property
    @pulumi.getter(name="peerAccountId")
    def peer_account_id(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier of the AWS account that owns the EC2 TGW peering.
        """
        return pulumi.get(self, "peer_account_id")

    @peer_account_id.setter
    def peer_account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "peer_account_id", value)

    @property
    @pulumi.getter(name="peerRegion")
    def peer_region(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "peer_region")

    @peer_region.setter
    def peer_region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "peer_region", value)

    @property
    @pulumi.getter(name="peerTransitGatewayId")
    def peer_transit_gateway_id(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier of EC2 Transit Gateway to peer with.
        """
        return pulumi.get(self, "peer_transit_gateway_id")

    @peer_transit_gateway_id.setter
    def peer_transit_gateway_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "peer_transit_gateway_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        return pulumi.get(self, "tags_all")

    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags_all", value)

    @property
    @pulumi.getter(name="transitGatewayAttachmentId")
    def transit_gateway_attachment_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the EC2 Transit Gateway Peering Attachment to manage.
        """
        return pulumi.get(self, "transit_gateway_attachment_id")

    @transit_gateway_attachment_id.setter
    def transit_gateway_attachment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "transit_gateway_attachment_id", value)

    @property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier of EC2 Transit Gateway.
        """
        return pulumi.get(self, "transit_gateway_id")

    @transit_gateway_id.setter
    def transit_gateway_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "transit_gateway_id", value)


class TransitGatewayPeeringAttachmentAccepter(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 transit_gateway_attachment_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages the accepter's side of an EC2 Transit Gateway Peering Attachment.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.ec2.TransitGatewayPeeringAttachmentAccepter("example",
            transit_gateway_attachment_id=aws_ec2_transit_gateway_peering_attachment["example"]["id"],
            tags={
                "Name": "Example cross-account attachment",
            })
        ```

        ## Import

        `aws_ec2_transit_gateway_peering_attachment_accepter` can be imported by using the EC2 Transit Gateway Attachment identifier, e.g.,

        ```sh
         $ pulumi import aws:ec2/transitGatewayPeeringAttachmentAccepter:TransitGatewayPeeringAttachmentAccepter example tgw-attach-12345678
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] transit_gateway_attachment_id: The ID of the EC2 Transit Gateway Peering Attachment to manage.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TransitGatewayPeeringAttachmentAccepterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages the accepter's side of an EC2 Transit Gateway Peering Attachment.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.ec2.TransitGatewayPeeringAttachmentAccepter("example",
            transit_gateway_attachment_id=aws_ec2_transit_gateway_peering_attachment["example"]["id"],
            tags={
                "Name": "Example cross-account attachment",
            })
        ```

        ## Import

        `aws_ec2_transit_gateway_peering_attachment_accepter` can be imported by using the EC2 Transit Gateway Attachment identifier, e.g.,

        ```sh
         $ pulumi import aws:ec2/transitGatewayPeeringAttachmentAccepter:TransitGatewayPeeringAttachmentAccepter example tgw-attach-12345678
        ```

        :param str resource_name: The name of the resource.
        :param TransitGatewayPeeringAttachmentAccepterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TransitGatewayPeeringAttachmentAccepterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 transit_gateway_attachment_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = TransitGatewayPeeringAttachmentAccepterArgs.__new__(TransitGatewayPeeringAttachmentAccepterArgs)

            __props__.__dict__["tags"] = tags
            if transit_gateway_attachment_id is None and not opts.urn:
                raise TypeError("Missing required property 'transit_gateway_attachment_id'")
            __props__.__dict__["transit_gateway_attachment_id"] = transit_gateway_attachment_id
            __props__.__dict__["peer_account_id"] = None
            __props__.__dict__["peer_region"] = None
            __props__.__dict__["peer_transit_gateway_id"] = None
            __props__.__dict__["tags_all"] = None
            __props__.__dict__["transit_gateway_id"] = None
        super(TransitGatewayPeeringAttachmentAccepter, __self__).__init__(
            'aws:ec2/transitGatewayPeeringAttachmentAccepter:TransitGatewayPeeringAttachmentAccepter',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            peer_account_id: Optional[pulumi.Input[str]] = None,
            peer_region: Optional[pulumi.Input[str]] = None,
            peer_transit_gateway_id: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            transit_gateway_attachment_id: Optional[pulumi.Input[str]] = None,
            transit_gateway_id: Optional[pulumi.Input[str]] = None) -> 'TransitGatewayPeeringAttachmentAccepter':
        """
        Get an existing TransitGatewayPeeringAttachmentAccepter resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] peer_account_id: Identifier of the AWS account that owns the EC2 TGW peering.
        :param pulumi.Input[str] peer_transit_gateway_id: Identifier of EC2 Transit Gateway to peer with.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        :param pulumi.Input[str] transit_gateway_attachment_id: The ID of the EC2 Transit Gateway Peering Attachment to manage.
        :param pulumi.Input[str] transit_gateway_id: Identifier of EC2 Transit Gateway.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TransitGatewayPeeringAttachmentAccepterState.__new__(_TransitGatewayPeeringAttachmentAccepterState)

        __props__.__dict__["peer_account_id"] = peer_account_id
        __props__.__dict__["peer_region"] = peer_region
        __props__.__dict__["peer_transit_gateway_id"] = peer_transit_gateway_id
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        __props__.__dict__["transit_gateway_attachment_id"] = transit_gateway_attachment_id
        __props__.__dict__["transit_gateway_id"] = transit_gateway_id
        return TransitGatewayPeeringAttachmentAccepter(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="peerAccountId")
    def peer_account_id(self) -> pulumi.Output[str]:
        """
        Identifier of the AWS account that owns the EC2 TGW peering.
        """
        return pulumi.get(self, "peer_account_id")

    @property
    @pulumi.getter(name="peerRegion")
    def peer_region(self) -> pulumi.Output[str]:
        return pulumi.get(self, "peer_region")

    @property
    @pulumi.getter(name="peerTransitGatewayId")
    def peer_transit_gateway_id(self) -> pulumi.Output[str]:
        """
        Identifier of EC2 Transit Gateway to peer with.
        """
        return pulumi.get(self, "peer_transit_gateway_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, str]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        return pulumi.get(self, "tags_all")

    @property
    @pulumi.getter(name="transitGatewayAttachmentId")
    def transit_gateway_attachment_id(self) -> pulumi.Output[str]:
        """
        The ID of the EC2 Transit Gateway Peering Attachment to manage.
        """
        return pulumi.get(self, "transit_gateway_attachment_id")

    @property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> pulumi.Output[str]:
        """
        Identifier of EC2 Transit Gateway.
        """
        return pulumi.get(self, "transit_gateway_id")

