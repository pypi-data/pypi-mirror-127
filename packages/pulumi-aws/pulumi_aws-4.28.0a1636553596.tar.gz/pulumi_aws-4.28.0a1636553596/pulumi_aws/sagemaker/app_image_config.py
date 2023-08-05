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

__all__ = ['AppImageConfigArgs', 'AppImageConfig']

@pulumi.input_type
class AppImageConfigArgs:
    def __init__(__self__, *,
                 app_image_config_name: pulumi.Input[str],
                 kernel_gateway_image_config: Optional[pulumi.Input['AppImageConfigKernelGatewayImageConfigArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a AppImageConfig resource.
        :param pulumi.Input[str] app_image_config_name: The name of the App Image Config.
        :param pulumi.Input['AppImageConfigKernelGatewayImageConfigArgs'] kernel_gateway_image_config: The configuration for the file system and kernels in a SageMaker image running as a KernelGateway app. See Kernel Gateway Image Config details below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        """
        pulumi.set(__self__, "app_image_config_name", app_image_config_name)
        if kernel_gateway_image_config is not None:
            pulumi.set(__self__, "kernel_gateway_image_config", kernel_gateway_image_config)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="appImageConfigName")
    def app_image_config_name(self) -> pulumi.Input[str]:
        """
        The name of the App Image Config.
        """
        return pulumi.get(self, "app_image_config_name")

    @app_image_config_name.setter
    def app_image_config_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "app_image_config_name", value)

    @property
    @pulumi.getter(name="kernelGatewayImageConfig")
    def kernel_gateway_image_config(self) -> Optional[pulumi.Input['AppImageConfigKernelGatewayImageConfigArgs']]:
        """
        The configuration for the file system and kernels in a SageMaker image running as a KernelGateway app. See Kernel Gateway Image Config details below.
        """
        return pulumi.get(self, "kernel_gateway_image_config")

    @kernel_gateway_image_config.setter
    def kernel_gateway_image_config(self, value: Optional[pulumi.Input['AppImageConfigKernelGatewayImageConfigArgs']]):
        pulumi.set(self, "kernel_gateway_image_config", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags to assign to the resource. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _AppImageConfigState:
    def __init__(__self__, *,
                 app_image_config_name: Optional[pulumi.Input[str]] = None,
                 arn: Optional[pulumi.Input[str]] = None,
                 kernel_gateway_image_config: Optional[pulumi.Input['AppImageConfigKernelGatewayImageConfigArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering AppImageConfig resources.
        :param pulumi.Input[str] app_image_config_name: The name of the App Image Config.
        :param pulumi.Input[str] arn: The Amazon Resource Name (ARN) assigned by AWS to this App Image Config.
        :param pulumi.Input['AppImageConfigKernelGatewayImageConfigArgs'] kernel_gateway_image_config: The configuration for the file system and kernels in a SageMaker image running as a KernelGateway app. See Kernel Gateway Image Config details below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block).
        """
        if app_image_config_name is not None:
            pulumi.set(__self__, "app_image_config_name", app_image_config_name)
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if kernel_gateway_image_config is not None:
            pulumi.set(__self__, "kernel_gateway_image_config", kernel_gateway_image_config)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)

    @property
    @pulumi.getter(name="appImageConfigName")
    def app_image_config_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the App Image Config.
        """
        return pulumi.get(self, "app_image_config_name")

    @app_image_config_name.setter
    def app_image_config_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "app_image_config_name", value)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon Resource Name (ARN) assigned by AWS to this App Image Config.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter(name="kernelGatewayImageConfig")
    def kernel_gateway_image_config(self) -> Optional[pulumi.Input['AppImageConfigKernelGatewayImageConfigArgs']]:
        """
        The configuration for the file system and kernels in a SageMaker image running as a KernelGateway app. See Kernel Gateway Image Config details below.
        """
        return pulumi.get(self, "kernel_gateway_image_config")

    @kernel_gateway_image_config.setter
    def kernel_gateway_image_config(self, value: Optional[pulumi.Input['AppImageConfigKernelGatewayImageConfigArgs']]):
        pulumi.set(self, "kernel_gateway_image_config", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags to assign to the resource. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block).
        """
        return pulumi.get(self, "tags_all")

    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags_all", value)


class AppImageConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_image_config_name: Optional[pulumi.Input[str]] = None,
                 kernel_gateway_image_config: Optional[pulumi.Input[pulumi.InputType['AppImageConfigKernelGatewayImageConfigArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Provides a Sagemaker App Image Config resource.

        ## Example Usage
        ### Basic usage

        ```python
        import pulumi
        import pulumi_aws as aws

        test = aws.sagemaker.AppImageConfig("test",
            app_image_config_name="example",
            kernel_gateway_image_config=aws.sagemaker.AppImageConfigKernelGatewayImageConfigArgs(
                kernel_spec=aws.sagemaker.AppImageConfigKernelGatewayImageConfigKernelSpecArgs(
                    name="example",
                ),
            ))
        ```
        ### Default File System Config

        ```python
        import pulumi
        import pulumi_aws as aws

        test = aws.sagemaker.AppImageConfig("test",
            app_image_config_name="example",
            kernel_gateway_image_config=aws.sagemaker.AppImageConfigKernelGatewayImageConfigArgs(
                file_system_config=aws.sagemaker.AppImageConfigKernelGatewayImageConfigFileSystemConfigArgs(),
                kernel_spec=aws.sagemaker.AppImageConfigKernelGatewayImageConfigKernelSpecArgs(
                    name="example",
                ),
            ))
        ```

        ## Import

        Sagemaker App Image Configs can be imported using the `name`, e.g.,

        ```sh
         $ pulumi import aws:sagemaker/appImageConfig:AppImageConfig example example
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] app_image_config_name: The name of the App Image Config.
        :param pulumi.Input[pulumi.InputType['AppImageConfigKernelGatewayImageConfigArgs']] kernel_gateway_image_config: The configuration for the file system and kernels in a SageMaker image running as a KernelGateway app. See Kernel Gateway Image Config details below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AppImageConfigArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Sagemaker App Image Config resource.

        ## Example Usage
        ### Basic usage

        ```python
        import pulumi
        import pulumi_aws as aws

        test = aws.sagemaker.AppImageConfig("test",
            app_image_config_name="example",
            kernel_gateway_image_config=aws.sagemaker.AppImageConfigKernelGatewayImageConfigArgs(
                kernel_spec=aws.sagemaker.AppImageConfigKernelGatewayImageConfigKernelSpecArgs(
                    name="example",
                ),
            ))
        ```
        ### Default File System Config

        ```python
        import pulumi
        import pulumi_aws as aws

        test = aws.sagemaker.AppImageConfig("test",
            app_image_config_name="example",
            kernel_gateway_image_config=aws.sagemaker.AppImageConfigKernelGatewayImageConfigArgs(
                file_system_config=aws.sagemaker.AppImageConfigKernelGatewayImageConfigFileSystemConfigArgs(),
                kernel_spec=aws.sagemaker.AppImageConfigKernelGatewayImageConfigKernelSpecArgs(
                    name="example",
                ),
            ))
        ```

        ## Import

        Sagemaker App Image Configs can be imported using the `name`, e.g.,

        ```sh
         $ pulumi import aws:sagemaker/appImageConfig:AppImageConfig example example
        ```

        :param str resource_name: The name of the resource.
        :param AppImageConfigArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AppImageConfigArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_image_config_name: Optional[pulumi.Input[str]] = None,
                 kernel_gateway_image_config: Optional[pulumi.Input[pulumi.InputType['AppImageConfigKernelGatewayImageConfigArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
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
            __props__ = AppImageConfigArgs.__new__(AppImageConfigArgs)

            if app_image_config_name is None and not opts.urn:
                raise TypeError("Missing required property 'app_image_config_name'")
            __props__.__dict__["app_image_config_name"] = app_image_config_name
            __props__.__dict__["kernel_gateway_image_config"] = kernel_gateway_image_config
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["tags_all"] = None
        super(AppImageConfig, __self__).__init__(
            'aws:sagemaker/appImageConfig:AppImageConfig',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            app_image_config_name: Optional[pulumi.Input[str]] = None,
            arn: Optional[pulumi.Input[str]] = None,
            kernel_gateway_image_config: Optional[pulumi.Input[pulumi.InputType['AppImageConfigKernelGatewayImageConfigArgs']]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'AppImageConfig':
        """
        Get an existing AppImageConfig resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] app_image_config_name: The name of the App Image Config.
        :param pulumi.Input[str] arn: The Amazon Resource Name (ARN) assigned by AWS to this App Image Config.
        :param pulumi.Input[pulumi.InputType['AppImageConfigKernelGatewayImageConfigArgs']] kernel_gateway_image_config: The configuration for the file system and kernels in a SageMaker image running as a KernelGateway app. See Kernel Gateway Image Config details below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block).
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AppImageConfigState.__new__(_AppImageConfigState)

        __props__.__dict__["app_image_config_name"] = app_image_config_name
        __props__.__dict__["arn"] = arn
        __props__.__dict__["kernel_gateway_image_config"] = kernel_gateway_image_config
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        return AppImageConfig(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="appImageConfigName")
    def app_image_config_name(self) -> pulumi.Output[str]:
        """
        The name of the App Image Config.
        """
        return pulumi.get(self, "app_image_config_name")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) assigned by AWS to this App Image Config.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="kernelGatewayImageConfig")
    def kernel_gateway_image_config(self) -> pulumi.Output[Optional['outputs.AppImageConfigKernelGatewayImageConfig']]:
        """
        The configuration for the file system and kernels in a SageMaker image running as a KernelGateway app. See Kernel Gateway Image Config details below.
        """
        return pulumi.get(self, "kernel_gateway_image_config")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of tags to assign to the resource. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, str]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block).
        """
        return pulumi.get(self, "tags_all")

