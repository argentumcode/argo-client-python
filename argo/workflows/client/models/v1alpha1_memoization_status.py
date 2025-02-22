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


class V1alpha1MemoizationStatus(object):
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
        'cache_name': 'str',
        'hit': 'bool',
        'key': 'str'
    }

    attribute_map = {
        'cache_name': 'cacheName',
        'hit': 'hit',
        'key': 'key'
    }

    def __init__(self, cache_name=None, hit=None, key=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1MemoizationStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cache_name = None
        self._hit = None
        self._key = None
        self.discriminator = None

        self.cache_name = cache_name
        self.hit = hit
        self.key = key

    @property
    def cache_name(self):
        """Gets the cache_name of this V1alpha1MemoizationStatus.  # noqa: E501

        Cache is the name of the cache that was used  # noqa: E501

        :return: The cache_name of this V1alpha1MemoizationStatus.  # noqa: E501
        :rtype: str
        """
        return self._cache_name

    @cache_name.setter
    def cache_name(self, cache_name):
        """Sets the cache_name of this V1alpha1MemoizationStatus.

        Cache is the name of the cache that was used  # noqa: E501

        :param cache_name: The cache_name of this V1alpha1MemoizationStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and cache_name is None:  # noqa: E501
            raise ValueError("Invalid value for `cache_name`, must not be `None`")  # noqa: E501

        self._cache_name = cache_name

    @property
    def hit(self):
        """Gets the hit of this V1alpha1MemoizationStatus.  # noqa: E501

        Hit indicates whether this node was created from a cache entry  # noqa: E501

        :return: The hit of this V1alpha1MemoizationStatus.  # noqa: E501
        :rtype: bool
        """
        return self._hit

    @hit.setter
    def hit(self, hit):
        """Sets the hit of this V1alpha1MemoizationStatus.

        Hit indicates whether this node was created from a cache entry  # noqa: E501

        :param hit: The hit of this V1alpha1MemoizationStatus.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and hit is None:  # noqa: E501
            raise ValueError("Invalid value for `hit`, must not be `None`")  # noqa: E501

        self._hit = hit

    @property
    def key(self):
        """Gets the key of this V1alpha1MemoizationStatus.  # noqa: E501

        Key is the name of the key used for this node's cache  # noqa: E501

        :return: The key of this V1alpha1MemoizationStatus.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this V1alpha1MemoizationStatus.

        Key is the name of the key used for this node's cache  # noqa: E501

        :param key: The key of this V1alpha1MemoizationStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and key is None:  # noqa: E501
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

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
        if not isinstance(other, V1alpha1MemoizationStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1MemoizationStatus):
            return True

        return self.to_dict() != other.to_dict()
