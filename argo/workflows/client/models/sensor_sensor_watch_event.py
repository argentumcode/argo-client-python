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


class SensorSensorWatchEvent(object):
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
        'object': 'IoArgoprojEventsV1alpha1Sensor',
        'type': 'str'
    }

    attribute_map = {
        'object': 'object',
        'type': 'type'
    }

    def __init__(self, object=None, type=None, local_vars_configuration=None):  # noqa: E501
        """SensorSensorWatchEvent - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._object = None
        self._type = None
        self.discriminator = None

        if object is not None:
            self.object = object
        if type is not None:
            self.type = type

    @property
    def object(self):
        """Gets the object of this SensorSensorWatchEvent.  # noqa: E501


        :return: The object of this SensorSensorWatchEvent.  # noqa: E501
        :rtype: IoArgoprojEventsV1alpha1Sensor
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this SensorSensorWatchEvent.


        :param object: The object of this SensorSensorWatchEvent.  # noqa: E501
        :type: IoArgoprojEventsV1alpha1Sensor
        """

        self._object = object

    @property
    def type(self):
        """Gets the type of this SensorSensorWatchEvent.  # noqa: E501


        :return: The type of this SensorSensorWatchEvent.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SensorSensorWatchEvent.


        :param type: The type of this SensorSensorWatchEvent.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if not isinstance(other, SensorSensorWatchEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SensorSensorWatchEvent):
            return True

        return self.to_dict() != other.to_dict()
