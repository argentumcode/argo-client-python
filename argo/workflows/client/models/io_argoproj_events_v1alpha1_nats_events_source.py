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


class IoArgoprojEventsV1alpha1NATSEventsSource(object):
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
        'connection_backoff': 'IoArgoprojEventsV1alpha1Backoff',
        'json_body': 'bool',
        'metadata': 'dict(str, str)',
        'subject': 'str',
        'tls': 'IoArgoprojEventsV1alpha1TLSConfig',
        'url': 'str'
    }

    attribute_map = {
        'connection_backoff': 'connectionBackoff',
        'json_body': 'jsonBody',
        'metadata': 'metadata',
        'subject': 'subject',
        'tls': 'tls',
        'url': 'url'
    }

    def __init__(self, connection_backoff=None, json_body=None, metadata=None, subject=None, tls=None, url=None, local_vars_configuration=None):  # noqa: E501
        """IoArgoprojEventsV1alpha1NATSEventsSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._connection_backoff = None
        self._json_body = None
        self._metadata = None
        self._subject = None
        self._tls = None
        self._url = None
        self.discriminator = None

        if connection_backoff is not None:
            self.connection_backoff = connection_backoff
        if json_body is not None:
            self.json_body = json_body
        if metadata is not None:
            self.metadata = metadata
        if subject is not None:
            self.subject = subject
        if tls is not None:
            self.tls = tls
        if url is not None:
            self.url = url

    @property
    def connection_backoff(self):
        """Gets the connection_backoff of this IoArgoprojEventsV1alpha1NATSEventsSource.  # noqa: E501


        :return: The connection_backoff of this IoArgoprojEventsV1alpha1NATSEventsSource.  # noqa: E501
        :rtype: IoArgoprojEventsV1alpha1Backoff
        """
        return self._connection_backoff

    @connection_backoff.setter
    def connection_backoff(self, connection_backoff):
        """Sets the connection_backoff of this IoArgoprojEventsV1alpha1NATSEventsSource.


        :param connection_backoff: The connection_backoff of this IoArgoprojEventsV1alpha1NATSEventsSource.  # noqa: E501
        :type: IoArgoprojEventsV1alpha1Backoff
        """

        self._connection_backoff = connection_backoff

    @property
    def json_body(self):
        """Gets the json_body of this IoArgoprojEventsV1alpha1NATSEventsSource.  # noqa: E501


        :return: The json_body of this IoArgoprojEventsV1alpha1NATSEventsSource.  # noqa: E501
        :rtype: bool
        """
        return self._json_body

    @json_body.setter
    def json_body(self, json_body):
        """Sets the json_body of this IoArgoprojEventsV1alpha1NATSEventsSource.


        :param json_body: The json_body of this IoArgoprojEventsV1alpha1NATSEventsSource.  # noqa: E501
        :type: bool
        """

        self._json_body = json_body

    @property
    def metadata(self):
        """Gets the metadata of this IoArgoprojEventsV1alpha1NATSEventsSource.  # noqa: E501


        :return: The metadata of this IoArgoprojEventsV1alpha1NATSEventsSource.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this IoArgoprojEventsV1alpha1NATSEventsSource.


        :param metadata: The metadata of this IoArgoprojEventsV1alpha1NATSEventsSource.  # noqa: E501
        :type: dict(str, str)
        """

        self._metadata = metadata

    @property
    def subject(self):
        """Gets the subject of this IoArgoprojEventsV1alpha1NATSEventsSource.  # noqa: E501


        :return: The subject of this IoArgoprojEventsV1alpha1NATSEventsSource.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this IoArgoprojEventsV1alpha1NATSEventsSource.


        :param subject: The subject of this IoArgoprojEventsV1alpha1NATSEventsSource.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def tls(self):
        """Gets the tls of this IoArgoprojEventsV1alpha1NATSEventsSource.  # noqa: E501


        :return: The tls of this IoArgoprojEventsV1alpha1NATSEventsSource.  # noqa: E501
        :rtype: IoArgoprojEventsV1alpha1TLSConfig
        """
        return self._tls

    @tls.setter
    def tls(self, tls):
        """Sets the tls of this IoArgoprojEventsV1alpha1NATSEventsSource.


        :param tls: The tls of this IoArgoprojEventsV1alpha1NATSEventsSource.  # noqa: E501
        :type: IoArgoprojEventsV1alpha1TLSConfig
        """

        self._tls = tls

    @property
    def url(self):
        """Gets the url of this IoArgoprojEventsV1alpha1NATSEventsSource.  # noqa: E501


        :return: The url of this IoArgoprojEventsV1alpha1NATSEventsSource.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this IoArgoprojEventsV1alpha1NATSEventsSource.


        :param url: The url of this IoArgoprojEventsV1alpha1NATSEventsSource.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if not isinstance(other, IoArgoprojEventsV1alpha1NATSEventsSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojEventsV1alpha1NATSEventsSource):
            return True

        return self.to_dict() != other.to_dict()
