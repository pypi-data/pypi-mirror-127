# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ExternalKeyArgs', 'ExternalKey']

@pulumi.input_type
class ExternalKeyArgs:
    def __init__(__self__, *,
                 bypass_policy_lockout_safety_check: Optional[pulumi.Input[bool]] = None,
                 deletion_window_in_days: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 key_material_base64: Optional[pulumi.Input[str]] = None,
                 multi_region: Optional[pulumi.Input[bool]] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 valid_to: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ExternalKey resource.
        :param pulumi.Input[bool] bypass_policy_lockout_safety_check: Specifies whether to disable the policy lockout check performed when creating or updating the key's policy. Setting this value to `true` increases the risk that the key becomes unmanageable. For more information, refer to the scenario in the [Default Key Policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default-allow-root-enable-iam) section in the AWS Key Management Service Developer Guide. Defaults to `false`.
        :param pulumi.Input[int] deletion_window_in_days: Duration in days after which the key is deleted after destruction of the resource. Must be between `7` and `30` days. Defaults to `30`.
        :param pulumi.Input[str] description: Description of the key.
        :param pulumi.Input[bool] enabled: Specifies whether the key is enabled. Keys pending import can only be `false`. Imported keys default to `true` unless expired.
        :param pulumi.Input[str] key_material_base64: Base64 encoded 256-bit symmetric encryption key material to import. The CMK is permanently associated with this key material. The same key material can be reimported, but you cannot import different key material.
        :param pulumi.Input[bool] multi_region: Indicates whether the KMS key is a multi-Region (`true`) or regional (`false`) key. Defaults to `false`.
        :param pulumi.Input[str] policy: A key policy JSON document. If you do not provide a key policy, AWS KMS attaches a default key policy to the CMK.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A key-value map of tags to assign to the key. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[str] valid_to: Time at which the imported key material expires. When the key material expires, AWS KMS deletes the key material and the CMK becomes unusable. If not specified, key material does not expire. Valid values: [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) (`YYYY-MM-DDTHH:MM:SSZ`)
        """
        if bypass_policy_lockout_safety_check is not None:
            pulumi.set(__self__, "bypass_policy_lockout_safety_check", bypass_policy_lockout_safety_check)
        if deletion_window_in_days is not None:
            pulumi.set(__self__, "deletion_window_in_days", deletion_window_in_days)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if key_material_base64 is not None:
            pulumi.set(__self__, "key_material_base64", key_material_base64)
        if multi_region is not None:
            pulumi.set(__self__, "multi_region", multi_region)
        if policy is not None:
            pulumi.set(__self__, "policy", policy)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if valid_to is not None:
            pulumi.set(__self__, "valid_to", valid_to)

    @property
    @pulumi.getter(name="bypassPolicyLockoutSafetyCheck")
    def bypass_policy_lockout_safety_check(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether to disable the policy lockout check performed when creating or updating the key's policy. Setting this value to `true` increases the risk that the key becomes unmanageable. For more information, refer to the scenario in the [Default Key Policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default-allow-root-enable-iam) section in the AWS Key Management Service Developer Guide. Defaults to `false`.
        """
        return pulumi.get(self, "bypass_policy_lockout_safety_check")

    @bypass_policy_lockout_safety_check.setter
    def bypass_policy_lockout_safety_check(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "bypass_policy_lockout_safety_check", value)

    @property
    @pulumi.getter(name="deletionWindowInDays")
    def deletion_window_in_days(self) -> Optional[pulumi.Input[int]]:
        """
        Duration in days after which the key is deleted after destruction of the resource. Must be between `7` and `30` days. Defaults to `30`.
        """
        return pulumi.get(self, "deletion_window_in_days")

    @deletion_window_in_days.setter
    def deletion_window_in_days(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "deletion_window_in_days", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the key.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether the key is enabled. Keys pending import can only be `false`. Imported keys default to `true` unless expired.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="keyMaterialBase64")
    def key_material_base64(self) -> Optional[pulumi.Input[str]]:
        """
        Base64 encoded 256-bit symmetric encryption key material to import. The CMK is permanently associated with this key material. The same key material can be reimported, but you cannot import different key material.
        """
        return pulumi.get(self, "key_material_base64")

    @key_material_base64.setter
    def key_material_base64(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_material_base64", value)

    @property
    @pulumi.getter(name="multiRegion")
    def multi_region(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether the KMS key is a multi-Region (`true`) or regional (`false`) key. Defaults to `false`.
        """
        return pulumi.get(self, "multi_region")

    @multi_region.setter
    def multi_region(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "multi_region", value)

    @property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[str]]:
        """
        A key policy JSON document. If you do not provide a key policy, AWS KMS attaches a default key policy to the CMK.
        """
        return pulumi.get(self, "policy")

    @policy.setter
    def policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A key-value map of tags to assign to the key. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="validTo")
    def valid_to(self) -> Optional[pulumi.Input[str]]:
        """
        Time at which the imported key material expires. When the key material expires, AWS KMS deletes the key material and the CMK becomes unusable. If not specified, key material does not expire. Valid values: [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) (`YYYY-MM-DDTHH:MM:SSZ`)
        """
        return pulumi.get(self, "valid_to")

    @valid_to.setter
    def valid_to(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "valid_to", value)


@pulumi.input_type
class _ExternalKeyState:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[str]] = None,
                 bypass_policy_lockout_safety_check: Optional[pulumi.Input[bool]] = None,
                 deletion_window_in_days: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 expiration_model: Optional[pulumi.Input[str]] = None,
                 key_material_base64: Optional[pulumi.Input[str]] = None,
                 key_state: Optional[pulumi.Input[str]] = None,
                 key_usage: Optional[pulumi.Input[str]] = None,
                 multi_region: Optional[pulumi.Input[bool]] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 valid_to: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ExternalKey resources.
        :param pulumi.Input[str] arn: The Amazon Resource Name (ARN) of the key.
        :param pulumi.Input[bool] bypass_policy_lockout_safety_check: Specifies whether to disable the policy lockout check performed when creating or updating the key's policy. Setting this value to `true` increases the risk that the key becomes unmanageable. For more information, refer to the scenario in the [Default Key Policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default-allow-root-enable-iam) section in the AWS Key Management Service Developer Guide. Defaults to `false`.
        :param pulumi.Input[int] deletion_window_in_days: Duration in days after which the key is deleted after destruction of the resource. Must be between `7` and `30` days. Defaults to `30`.
        :param pulumi.Input[str] description: Description of the key.
        :param pulumi.Input[bool] enabled: Specifies whether the key is enabled. Keys pending import can only be `false`. Imported keys default to `true` unless expired.
        :param pulumi.Input[str] expiration_model: Whether the key material expires. Empty when pending key material import, otherwise `KEY_MATERIAL_EXPIRES` or `KEY_MATERIAL_DOES_NOT_EXPIRE`.
        :param pulumi.Input[str] key_material_base64: Base64 encoded 256-bit symmetric encryption key material to import. The CMK is permanently associated with this key material. The same key material can be reimported, but you cannot import different key material.
        :param pulumi.Input[str] key_state: The state of the CMK.
        :param pulumi.Input[str] key_usage: The cryptographic operations for which you can use the CMK.
        :param pulumi.Input[bool] multi_region: Indicates whether the KMS key is a multi-Region (`true`) or regional (`false`) key. Defaults to `false`.
        :param pulumi.Input[str] policy: A key policy JSON document. If you do not provide a key policy, AWS KMS attaches a default key policy to the CMK.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A key-value map of tags to assign to the key. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        :param pulumi.Input[str] valid_to: Time at which the imported key material expires. When the key material expires, AWS KMS deletes the key material and the CMK becomes unusable. If not specified, key material does not expire. Valid values: [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) (`YYYY-MM-DDTHH:MM:SSZ`)
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if bypass_policy_lockout_safety_check is not None:
            pulumi.set(__self__, "bypass_policy_lockout_safety_check", bypass_policy_lockout_safety_check)
        if deletion_window_in_days is not None:
            pulumi.set(__self__, "deletion_window_in_days", deletion_window_in_days)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if expiration_model is not None:
            pulumi.set(__self__, "expiration_model", expiration_model)
        if key_material_base64 is not None:
            pulumi.set(__self__, "key_material_base64", key_material_base64)
        if key_state is not None:
            pulumi.set(__self__, "key_state", key_state)
        if key_usage is not None:
            pulumi.set(__self__, "key_usage", key_usage)
        if multi_region is not None:
            pulumi.set(__self__, "multi_region", multi_region)
        if policy is not None:
            pulumi.set(__self__, "policy", policy)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)
        if valid_to is not None:
            pulumi.set(__self__, "valid_to", valid_to)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon Resource Name (ARN) of the key.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter(name="bypassPolicyLockoutSafetyCheck")
    def bypass_policy_lockout_safety_check(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether to disable the policy lockout check performed when creating or updating the key's policy. Setting this value to `true` increases the risk that the key becomes unmanageable. For more information, refer to the scenario in the [Default Key Policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default-allow-root-enable-iam) section in the AWS Key Management Service Developer Guide. Defaults to `false`.
        """
        return pulumi.get(self, "bypass_policy_lockout_safety_check")

    @bypass_policy_lockout_safety_check.setter
    def bypass_policy_lockout_safety_check(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "bypass_policy_lockout_safety_check", value)

    @property
    @pulumi.getter(name="deletionWindowInDays")
    def deletion_window_in_days(self) -> Optional[pulumi.Input[int]]:
        """
        Duration in days after which the key is deleted after destruction of the resource. Must be between `7` and `30` days. Defaults to `30`.
        """
        return pulumi.get(self, "deletion_window_in_days")

    @deletion_window_in_days.setter
    def deletion_window_in_days(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "deletion_window_in_days", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the key.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether the key is enabled. Keys pending import can only be `false`. Imported keys default to `true` unless expired.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="expirationModel")
    def expiration_model(self) -> Optional[pulumi.Input[str]]:
        """
        Whether the key material expires. Empty when pending key material import, otherwise `KEY_MATERIAL_EXPIRES` or `KEY_MATERIAL_DOES_NOT_EXPIRE`.
        """
        return pulumi.get(self, "expiration_model")

    @expiration_model.setter
    def expiration_model(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expiration_model", value)

    @property
    @pulumi.getter(name="keyMaterialBase64")
    def key_material_base64(self) -> Optional[pulumi.Input[str]]:
        """
        Base64 encoded 256-bit symmetric encryption key material to import. The CMK is permanently associated with this key material. The same key material can be reimported, but you cannot import different key material.
        """
        return pulumi.get(self, "key_material_base64")

    @key_material_base64.setter
    def key_material_base64(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_material_base64", value)

    @property
    @pulumi.getter(name="keyState")
    def key_state(self) -> Optional[pulumi.Input[str]]:
        """
        The state of the CMK.
        """
        return pulumi.get(self, "key_state")

    @key_state.setter
    def key_state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_state", value)

    @property
    @pulumi.getter(name="keyUsage")
    def key_usage(self) -> Optional[pulumi.Input[str]]:
        """
        The cryptographic operations for which you can use the CMK.
        """
        return pulumi.get(self, "key_usage")

    @key_usage.setter
    def key_usage(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_usage", value)

    @property
    @pulumi.getter(name="multiRegion")
    def multi_region(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether the KMS key is a multi-Region (`true`) or regional (`false`) key. Defaults to `false`.
        """
        return pulumi.get(self, "multi_region")

    @multi_region.setter
    def multi_region(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "multi_region", value)

    @property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[str]]:
        """
        A key policy JSON document. If you do not provide a key policy, AWS KMS attaches a default key policy to the CMK.
        """
        return pulumi.get(self, "policy")

    @policy.setter
    def policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A key-value map of tags to assign to the key. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
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
    @pulumi.getter(name="validTo")
    def valid_to(self) -> Optional[pulumi.Input[str]]:
        """
        Time at which the imported key material expires. When the key material expires, AWS KMS deletes the key material and the CMK becomes unusable. If not specified, key material does not expire. Valid values: [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) (`YYYY-MM-DDTHH:MM:SSZ`)
        """
        return pulumi.get(self, "valid_to")

    @valid_to.setter
    def valid_to(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "valid_to", value)


class ExternalKey(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bypass_policy_lockout_safety_check: Optional[pulumi.Input[bool]] = None,
                 deletion_window_in_days: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 key_material_base64: Optional[pulumi.Input[str]] = None,
                 multi_region: Optional[pulumi.Input[bool]] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 valid_to: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a KMS Customer Master Key that uses external key material. To instead manage a KMS Customer Master Key where AWS automatically generates and potentially rotates key material, see the `kms.Key` resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.kms.ExternalKey("example", description="KMS EXTERNAL for AMI encryption")
        ```

        ## Import

        KMS External Keys can be imported using the `id`, e.g.,

        ```sh
         $ pulumi import aws:kms/externalKey:ExternalKey a arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] bypass_policy_lockout_safety_check: Specifies whether to disable the policy lockout check performed when creating or updating the key's policy. Setting this value to `true` increases the risk that the key becomes unmanageable. For more information, refer to the scenario in the [Default Key Policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default-allow-root-enable-iam) section in the AWS Key Management Service Developer Guide. Defaults to `false`.
        :param pulumi.Input[int] deletion_window_in_days: Duration in days after which the key is deleted after destruction of the resource. Must be between `7` and `30` days. Defaults to `30`.
        :param pulumi.Input[str] description: Description of the key.
        :param pulumi.Input[bool] enabled: Specifies whether the key is enabled. Keys pending import can only be `false`. Imported keys default to `true` unless expired.
        :param pulumi.Input[str] key_material_base64: Base64 encoded 256-bit symmetric encryption key material to import. The CMK is permanently associated with this key material. The same key material can be reimported, but you cannot import different key material.
        :param pulumi.Input[bool] multi_region: Indicates whether the KMS key is a multi-Region (`true`) or regional (`false`) key. Defaults to `false`.
        :param pulumi.Input[str] policy: A key policy JSON document. If you do not provide a key policy, AWS KMS attaches a default key policy to the CMK.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A key-value map of tags to assign to the key. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[str] valid_to: Time at which the imported key material expires. When the key material expires, AWS KMS deletes the key material and the CMK becomes unusable. If not specified, key material does not expire. Valid values: [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) (`YYYY-MM-DDTHH:MM:SSZ`)
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ExternalKeyArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a KMS Customer Master Key that uses external key material. To instead manage a KMS Customer Master Key where AWS automatically generates and potentially rotates key material, see the `kms.Key` resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.kms.ExternalKey("example", description="KMS EXTERNAL for AMI encryption")
        ```

        ## Import

        KMS External Keys can be imported using the `id`, e.g.,

        ```sh
         $ pulumi import aws:kms/externalKey:ExternalKey a arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab
        ```

        :param str resource_name: The name of the resource.
        :param ExternalKeyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ExternalKeyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bypass_policy_lockout_safety_check: Optional[pulumi.Input[bool]] = None,
                 deletion_window_in_days: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 key_material_base64: Optional[pulumi.Input[str]] = None,
                 multi_region: Optional[pulumi.Input[bool]] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 valid_to: Optional[pulumi.Input[str]] = None,
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
            __props__ = ExternalKeyArgs.__new__(ExternalKeyArgs)

            __props__.__dict__["bypass_policy_lockout_safety_check"] = bypass_policy_lockout_safety_check
            __props__.__dict__["deletion_window_in_days"] = deletion_window_in_days
            __props__.__dict__["description"] = description
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["key_material_base64"] = key_material_base64
            __props__.__dict__["multi_region"] = multi_region
            __props__.__dict__["policy"] = policy
            __props__.__dict__["tags"] = tags
            __props__.__dict__["valid_to"] = valid_to
            __props__.__dict__["arn"] = None
            __props__.__dict__["expiration_model"] = None
            __props__.__dict__["key_state"] = None
            __props__.__dict__["key_usage"] = None
            __props__.__dict__["tags_all"] = None
        super(ExternalKey, __self__).__init__(
            'aws:kms/externalKey:ExternalKey',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            bypass_policy_lockout_safety_check: Optional[pulumi.Input[bool]] = None,
            deletion_window_in_days: Optional[pulumi.Input[int]] = None,
            description: Optional[pulumi.Input[str]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            expiration_model: Optional[pulumi.Input[str]] = None,
            key_material_base64: Optional[pulumi.Input[str]] = None,
            key_state: Optional[pulumi.Input[str]] = None,
            key_usage: Optional[pulumi.Input[str]] = None,
            multi_region: Optional[pulumi.Input[bool]] = None,
            policy: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            valid_to: Optional[pulumi.Input[str]] = None) -> 'ExternalKey':
        """
        Get an existing ExternalKey resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The Amazon Resource Name (ARN) of the key.
        :param pulumi.Input[bool] bypass_policy_lockout_safety_check: Specifies whether to disable the policy lockout check performed when creating or updating the key's policy. Setting this value to `true` increases the risk that the key becomes unmanageable. For more information, refer to the scenario in the [Default Key Policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default-allow-root-enable-iam) section in the AWS Key Management Service Developer Guide. Defaults to `false`.
        :param pulumi.Input[int] deletion_window_in_days: Duration in days after which the key is deleted after destruction of the resource. Must be between `7` and `30` days. Defaults to `30`.
        :param pulumi.Input[str] description: Description of the key.
        :param pulumi.Input[bool] enabled: Specifies whether the key is enabled. Keys pending import can only be `false`. Imported keys default to `true` unless expired.
        :param pulumi.Input[str] expiration_model: Whether the key material expires. Empty when pending key material import, otherwise `KEY_MATERIAL_EXPIRES` or `KEY_MATERIAL_DOES_NOT_EXPIRE`.
        :param pulumi.Input[str] key_material_base64: Base64 encoded 256-bit symmetric encryption key material to import. The CMK is permanently associated with this key material. The same key material can be reimported, but you cannot import different key material.
        :param pulumi.Input[str] key_state: The state of the CMK.
        :param pulumi.Input[str] key_usage: The cryptographic operations for which you can use the CMK.
        :param pulumi.Input[bool] multi_region: Indicates whether the KMS key is a multi-Region (`true`) or regional (`false`) key. Defaults to `false`.
        :param pulumi.Input[str] policy: A key policy JSON document. If you do not provide a key policy, AWS KMS attaches a default key policy to the CMK.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A key-value map of tags to assign to the key. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        :param pulumi.Input[str] valid_to: Time at which the imported key material expires. When the key material expires, AWS KMS deletes the key material and the CMK becomes unusable. If not specified, key material does not expire. Valid values: [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) (`YYYY-MM-DDTHH:MM:SSZ`)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ExternalKeyState.__new__(_ExternalKeyState)

        __props__.__dict__["arn"] = arn
        __props__.__dict__["bypass_policy_lockout_safety_check"] = bypass_policy_lockout_safety_check
        __props__.__dict__["deletion_window_in_days"] = deletion_window_in_days
        __props__.__dict__["description"] = description
        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["expiration_model"] = expiration_model
        __props__.__dict__["key_material_base64"] = key_material_base64
        __props__.__dict__["key_state"] = key_state
        __props__.__dict__["key_usage"] = key_usage
        __props__.__dict__["multi_region"] = multi_region
        __props__.__dict__["policy"] = policy
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        __props__.__dict__["valid_to"] = valid_to
        return ExternalKey(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the key.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="bypassPolicyLockoutSafetyCheck")
    def bypass_policy_lockout_safety_check(self) -> pulumi.Output[Optional[bool]]:
        """
        Specifies whether to disable the policy lockout check performed when creating or updating the key's policy. Setting this value to `true` increases the risk that the key becomes unmanageable. For more information, refer to the scenario in the [Default Key Policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default-allow-root-enable-iam) section in the AWS Key Management Service Developer Guide. Defaults to `false`.
        """
        return pulumi.get(self, "bypass_policy_lockout_safety_check")

    @property
    @pulumi.getter(name="deletionWindowInDays")
    def deletion_window_in_days(self) -> pulumi.Output[Optional[int]]:
        """
        Duration in days after which the key is deleted after destruction of the resource. Must be between `7` and `30` days. Defaults to `30`.
        """
        return pulumi.get(self, "deletion_window_in_days")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the key.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[bool]:
        """
        Specifies whether the key is enabled. Keys pending import can only be `false`. Imported keys default to `true` unless expired.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="expirationModel")
    def expiration_model(self) -> pulumi.Output[str]:
        """
        Whether the key material expires. Empty when pending key material import, otherwise `KEY_MATERIAL_EXPIRES` or `KEY_MATERIAL_DOES_NOT_EXPIRE`.
        """
        return pulumi.get(self, "expiration_model")

    @property
    @pulumi.getter(name="keyMaterialBase64")
    def key_material_base64(self) -> pulumi.Output[Optional[str]]:
        """
        Base64 encoded 256-bit symmetric encryption key material to import. The CMK is permanently associated with this key material. The same key material can be reimported, but you cannot import different key material.
        """
        return pulumi.get(self, "key_material_base64")

    @property
    @pulumi.getter(name="keyState")
    def key_state(self) -> pulumi.Output[str]:
        """
        The state of the CMK.
        """
        return pulumi.get(self, "key_state")

    @property
    @pulumi.getter(name="keyUsage")
    def key_usage(self) -> pulumi.Output[str]:
        """
        The cryptographic operations for which you can use the CMK.
        """
        return pulumi.get(self, "key_usage")

    @property
    @pulumi.getter(name="multiRegion")
    def multi_region(self) -> pulumi.Output[bool]:
        """
        Indicates whether the KMS key is a multi-Region (`true`) or regional (`false`) key. Defaults to `false`.
        """
        return pulumi.get(self, "multi_region")

    @property
    @pulumi.getter
    def policy(self) -> pulumi.Output[str]:
        """
        A key policy JSON document. If you do not provide a key policy, AWS KMS attaches a default key policy to the CMK.
        """
        return pulumi.get(self, "policy")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A key-value map of tags to assign to the key. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, str]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        return pulumi.get(self, "tags_all")

    @property
    @pulumi.getter(name="validTo")
    def valid_to(self) -> pulumi.Output[Optional[str]]:
        """
        Time at which the imported key material expires. When the key material expires, AWS KMS deletes the key material and the CMK becomes unusable. If not specified, key material does not expire. Valid values: [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) (`YYYY-MM-DDTHH:MM:SSZ`)
        """
        return pulumi.get(self, "valid_to")

