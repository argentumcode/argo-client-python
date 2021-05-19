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


class IoArgoprojEventsV1alpha1TriggerPolicy(object):
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
        'k8s': 'IoArgoprojEventsV1alpha1K8SResourcePolicy',
        'status': 'IoArgoprojEventsV1alpha1StatusPolicy'
    }

    attribute_map = {
        'k8s': 'k8s',
        'status': 'status'
    }

    def __init__(self, k8s=None, status=None, local_vars_configuration=None):  # noqa: E501
        """IoArgoprojEventsV1alpha1TriggerPolicy - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._k8s = None
        self._status = None
        self.discriminator = None

        if k8s is not None:
            self.k8s = k8s
        if status is not None:
            self.status = status

    @property
    def k8s(self):
        """Gets the k8s of this IoArgoprojEventsV1alpha1TriggerPolicy.  # noqa: E501


        :return: The k8s of this IoArgoprojEventsV1alpha1TriggerPolicy.  # noqa: E501
        :rtype: IoArgoprojEventsV1alpha1K8SResourcePolicy
        """
        return self._k8s

    @k8s.setter
    def k8s(self, k8s):
        """Sets the k8s of this IoArgoprojEventsV1alpha1TriggerPolicy.


        :param k8s: The k8s of this IoArgoprojEventsV1alpha1TriggerPolicy.  # noqa: E501
        :type: IoArgoprojEventsV1alpha1K8SResourcePolicy
        """

        self._k8s = k8s

    @property
    def status(self):
        """Gets the status of this IoArgoprojEventsV1alpha1TriggerPolicy.  # noqa: E501


        :return: The status of this IoArgoprojEventsV1alpha1TriggerPolicy.  # noqa: E501
        :rtype: IoArgoprojEventsV1alpha1StatusPolicy
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this IoArgoprojEventsV1alpha1TriggerPolicy.


        :param status: The status of this IoArgoprojEventsV1alpha1TriggerPolicy.  # noqa: E501
        :type: IoArgoprojEventsV1alpha1StatusPolicy
        """

        self._status = status

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
        if not isinstance(other, IoArgoprojEventsV1alpha1TriggerPolicy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojEventsV1alpha1TriggerPolicy):
            return True

        return self.to_dict() != other.to_dict()
