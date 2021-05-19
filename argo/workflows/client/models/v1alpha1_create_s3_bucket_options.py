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


class V1alpha1CreateS3BucketOptions(object):
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
        'object_locking': 'bool'
    }

    attribute_map = {
        'object_locking': 'objectLocking'
    }

    def __init__(self, object_locking=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1CreateS3BucketOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._object_locking = None
        self.discriminator = None

        if object_locking is not None:
            self.object_locking = object_locking

    @property
    def object_locking(self):
        """Gets the object_locking of this V1alpha1CreateS3BucketOptions.  # noqa: E501

        ObjectLocking Enable object locking  # noqa: E501

        :return: The object_locking of this V1alpha1CreateS3BucketOptions.  # noqa: E501
        :rtype: bool
        """
        return self._object_locking

    @object_locking.setter
    def object_locking(self, object_locking):
        """Sets the object_locking of this V1alpha1CreateS3BucketOptions.

        ObjectLocking Enable object locking  # noqa: E501

        :param object_locking: The object_locking of this V1alpha1CreateS3BucketOptions.  # noqa: E501
        :type: bool
        """

        self._object_locking = object_locking

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
        if not isinstance(other, V1alpha1CreateS3BucketOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1CreateS3BucketOptions):
            return True

        return self.to_dict() != other.to_dict()
