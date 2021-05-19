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


class V1Handler(object):
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
        '_exec': 'V1ExecAction',
        'http_get': 'V1HTTPGetAction',
        'tcp_socket': 'V1TCPSocketAction'
    }

    attribute_map = {
        '_exec': 'exec',
        'http_get': 'httpGet',
        'tcp_socket': 'tcpSocket'
    }

    def __init__(self, _exec=None, http_get=None, tcp_socket=None, local_vars_configuration=None):  # noqa: E501
        """V1Handler - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self.__exec = None
        self._http_get = None
        self._tcp_socket = None
        self.discriminator = None

        if _exec is not None:
            self._exec = _exec
        if http_get is not None:
            self.http_get = http_get
        if tcp_socket is not None:
            self.tcp_socket = tcp_socket

    @property
    def _exec(self):
        """Gets the _exec of this V1Handler.  # noqa: E501


        :return: The _exec of this V1Handler.  # noqa: E501
        :rtype: V1ExecAction
        """
        return self.__exec

    @_exec.setter
    def _exec(self, _exec):
        """Sets the _exec of this V1Handler.


        :param _exec: The _exec of this V1Handler.  # noqa: E501
        :type: V1ExecAction
        """

        self.__exec = _exec

    @property
    def http_get(self):
        """Gets the http_get of this V1Handler.  # noqa: E501


        :return: The http_get of this V1Handler.  # noqa: E501
        :rtype: V1HTTPGetAction
        """
        return self._http_get

    @http_get.setter
    def http_get(self, http_get):
        """Sets the http_get of this V1Handler.


        :param http_get: The http_get of this V1Handler.  # noqa: E501
        :type: V1HTTPGetAction
        """

        self._http_get = http_get

    @property
    def tcp_socket(self):
        """Gets the tcp_socket of this V1Handler.  # noqa: E501


        :return: The tcp_socket of this V1Handler.  # noqa: E501
        :rtype: V1TCPSocketAction
        """
        return self._tcp_socket

    @tcp_socket.setter
    def tcp_socket(self, tcp_socket):
        """Sets the tcp_socket of this V1Handler.


        :param tcp_socket: The tcp_socket of this V1Handler.  # noqa: E501
        :type: V1TCPSocketAction
        """

        self._tcp_socket = tcp_socket

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
        if not isinstance(other, V1Handler):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1Handler):
            return True

        return self.to_dict() != other.to_dict()
