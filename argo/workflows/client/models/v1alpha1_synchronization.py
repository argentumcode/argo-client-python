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


class V1alpha1Synchronization(object):
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
        'mutex': 'V1alpha1Mutex',
        'semaphore': 'V1alpha1SemaphoreRef'
    }

    attribute_map = {
        'mutex': 'mutex',
        'semaphore': 'semaphore'
    }

    def __init__(self, mutex=None, semaphore=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1Synchronization - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._mutex = None
        self._semaphore = None
        self.discriminator = None

        if mutex is not None:
            self.mutex = mutex
        if semaphore is not None:
            self.semaphore = semaphore

    @property
    def mutex(self):
        """Gets the mutex of this V1alpha1Synchronization.  # noqa: E501


        :return: The mutex of this V1alpha1Synchronization.  # noqa: E501
        :rtype: V1alpha1Mutex
        """
        return self._mutex

    @mutex.setter
    def mutex(self, mutex):
        """Sets the mutex of this V1alpha1Synchronization.


        :param mutex: The mutex of this V1alpha1Synchronization.  # noqa: E501
        :type: V1alpha1Mutex
        """

        self._mutex = mutex

    @property
    def semaphore(self):
        """Gets the semaphore of this V1alpha1Synchronization.  # noqa: E501


        :return: The semaphore of this V1alpha1Synchronization.  # noqa: E501
        :rtype: V1alpha1SemaphoreRef
        """
        return self._semaphore

    @semaphore.setter
    def semaphore(self, semaphore):
        """Sets the semaphore of this V1alpha1Synchronization.


        :param semaphore: The semaphore of this V1alpha1Synchronization.  # noqa: E501
        :type: V1alpha1SemaphoreRef
        """

        self._semaphore = semaphore

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
        if not isinstance(other, V1alpha1Synchronization):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1Synchronization):
            return True

        return self.to_dict() != other.to_dict()
