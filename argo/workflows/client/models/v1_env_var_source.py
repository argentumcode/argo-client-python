# coding: utf-8

"""
    Argo Server API

    You can get examples of requests and responses by using the CLI with `--gloglevel=9`, e.g. `argo list --gloglevel=9`  # noqa: E501

    The version of the OpenAPI document: v3.0.4
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from argo.workflows.client.configuration import Configuration


class V1EnvVarSource(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'config_map_key_ref': 'V1ConfigMapKeySelector',
        'field_ref': 'V1ObjectFieldSelector',
        'resource_field_ref': 'V1ResourceFieldSelector',
        'secret_key_ref': 'V1SecretKeySelector'
    }

    attribute_map = {
        'config_map_key_ref': 'configMapKeyRef',
        'field_ref': 'fieldRef',
        'resource_field_ref': 'resourceFieldRef',
        'secret_key_ref': 'secretKeyRef'
    }

    def __init__(self, config_map_key_ref=None, field_ref=None, resource_field_ref=None, secret_key_ref=None, local_vars_configuration=None):  # noqa: E501
        """V1EnvVarSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._config_map_key_ref = None
        self._field_ref = None
        self._resource_field_ref = None
        self._secret_key_ref = None
        self.discriminator = None

        if config_map_key_ref is not None:
            self.config_map_key_ref = config_map_key_ref
        if field_ref is not None:
            self.field_ref = field_ref
        if resource_field_ref is not None:
            self.resource_field_ref = resource_field_ref
        if secret_key_ref is not None:
            self.secret_key_ref = secret_key_ref

    @property
    def config_map_key_ref(self):
        """Gets the config_map_key_ref of this V1EnvVarSource.  # noqa: E501


        :return: The config_map_key_ref of this V1EnvVarSource.  # noqa: E501
        :rtype: V1ConfigMapKeySelector
        """
        return self._config_map_key_ref

    @config_map_key_ref.setter
    def config_map_key_ref(self, config_map_key_ref):
        """Sets the config_map_key_ref of this V1EnvVarSource.


        :param config_map_key_ref: The config_map_key_ref of this V1EnvVarSource.  # noqa: E501
        :type: V1ConfigMapKeySelector
        """

        self._config_map_key_ref = config_map_key_ref

    @property
    def field_ref(self):
        """Gets the field_ref of this V1EnvVarSource.  # noqa: E501


        :return: The field_ref of this V1EnvVarSource.  # noqa: E501
        :rtype: V1ObjectFieldSelector
        """
        return self._field_ref

    @field_ref.setter
    def field_ref(self, field_ref):
        """Sets the field_ref of this V1EnvVarSource.


        :param field_ref: The field_ref of this V1EnvVarSource.  # noqa: E501
        :type: V1ObjectFieldSelector
        """

        self._field_ref = field_ref

    @property
    def resource_field_ref(self):
        """Gets the resource_field_ref of this V1EnvVarSource.  # noqa: E501


        :return: The resource_field_ref of this V1EnvVarSource.  # noqa: E501
        :rtype: V1ResourceFieldSelector
        """
        return self._resource_field_ref

    @resource_field_ref.setter
    def resource_field_ref(self, resource_field_ref):
        """Sets the resource_field_ref of this V1EnvVarSource.


        :param resource_field_ref: The resource_field_ref of this V1EnvVarSource.  # noqa: E501
        :type: V1ResourceFieldSelector
        """

        self._resource_field_ref = resource_field_ref

    @property
    def secret_key_ref(self):
        """Gets the secret_key_ref of this V1EnvVarSource.  # noqa: E501


        :return: The secret_key_ref of this V1EnvVarSource.  # noqa: E501
        :rtype: V1SecretKeySelector
        """
        return self._secret_key_ref

    @secret_key_ref.setter
    def secret_key_ref(self, secret_key_ref):
        """Sets the secret_key_ref of this V1EnvVarSource.


        :param secret_key_ref: The secret_key_ref of this V1EnvVarSource.  # noqa: E501
        :type: V1SecretKeySelector
        """

        self._secret_key_ref = secret_key_ref

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1EnvVarSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1EnvVarSource):
            return True

        return self.to_dict() != other.to_dict()
