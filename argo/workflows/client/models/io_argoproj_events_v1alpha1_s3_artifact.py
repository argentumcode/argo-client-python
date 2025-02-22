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


class IoArgoprojEventsV1alpha1S3Artifact(object):
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
        'access_key': 'V1SecretKeySelector',
        'bucket': 'IoArgoprojEventsV1alpha1S3Bucket',
        'endpoint': 'str',
        'events': 'list[str]',
        'filter': 'IoArgoprojEventsV1alpha1S3Filter',
        'insecure': 'bool',
        'metadata': 'dict(str, str)',
        'region': 'str',
        'secret_key': 'V1SecretKeySelector'
    }

    attribute_map = {
        'access_key': 'accessKey',
        'bucket': 'bucket',
        'endpoint': 'endpoint',
        'events': 'events',
        'filter': 'filter',
        'insecure': 'insecure',
        'metadata': 'metadata',
        'region': 'region',
        'secret_key': 'secretKey'
    }

    def __init__(self, access_key=None, bucket=None, endpoint=None, events=None, filter=None, insecure=None, metadata=None, region=None, secret_key=None, local_vars_configuration=None):  # noqa: E501
        """IoArgoprojEventsV1alpha1S3Artifact - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._access_key = None
        self._bucket = None
        self._endpoint = None
        self._events = None
        self._filter = None
        self._insecure = None
        self._metadata = None
        self._region = None
        self._secret_key = None
        self.discriminator = None

        if access_key is not None:
            self.access_key = access_key
        if bucket is not None:
            self.bucket = bucket
        if endpoint is not None:
            self.endpoint = endpoint
        if events is not None:
            self.events = events
        if filter is not None:
            self.filter = filter
        if insecure is not None:
            self.insecure = insecure
        if metadata is not None:
            self.metadata = metadata
        if region is not None:
            self.region = region
        if secret_key is not None:
            self.secret_key = secret_key

    @property
    def access_key(self):
        """Gets the access_key of this IoArgoprojEventsV1alpha1S3Artifact.  # noqa: E501


        :return: The access_key of this IoArgoprojEventsV1alpha1S3Artifact.  # noqa: E501
        :rtype: V1SecretKeySelector
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this IoArgoprojEventsV1alpha1S3Artifact.


        :param access_key: The access_key of this IoArgoprojEventsV1alpha1S3Artifact.  # noqa: E501
        :type: V1SecretKeySelector
        """

        self._access_key = access_key

    @property
    def bucket(self):
        """Gets the bucket of this IoArgoprojEventsV1alpha1S3Artifact.  # noqa: E501


        :return: The bucket of this IoArgoprojEventsV1alpha1S3Artifact.  # noqa: E501
        :rtype: IoArgoprojEventsV1alpha1S3Bucket
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this IoArgoprojEventsV1alpha1S3Artifact.


        :param bucket: The bucket of this IoArgoprojEventsV1alpha1S3Artifact.  # noqa: E501
        :type: IoArgoprojEventsV1alpha1S3Bucket
        """

        self._bucket = bucket

    @property
    def endpoint(self):
        """Gets the endpoint of this IoArgoprojEventsV1alpha1S3Artifact.  # noqa: E501


        :return: The endpoint of this IoArgoprojEventsV1alpha1S3Artifact.  # noqa: E501
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this IoArgoprojEventsV1alpha1S3Artifact.


        :param endpoint: The endpoint of this IoArgoprojEventsV1alpha1S3Artifact.  # noqa: E501
        :type: str
        """

        self._endpoint = endpoint

    @property
    def events(self):
        """Gets the events of this IoArgoprojEventsV1alpha1S3Artifact.  # noqa: E501


        :return: The events of this IoArgoprojEventsV1alpha1S3Artifact.  # noqa: E501
        :rtype: list[str]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this IoArgoprojEventsV1alpha1S3Artifact.


        :param events: The events of this IoArgoprojEventsV1alpha1S3Artifact.  # noqa: E501
        :type: list[str]
        """

        self._events = events

    @property
    def filter(self):
        """Gets the filter of this IoArgoprojEventsV1alpha1S3Artifact.  # noqa: E501


        :return: The filter of this IoArgoprojEventsV1alpha1S3Artifact.  # noqa: E501
        :rtype: IoArgoprojEventsV1alpha1S3Filter
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this IoArgoprojEventsV1alpha1S3Artifact.


        :param filter: The filter of this IoArgoprojEventsV1alpha1S3Artifact.  # noqa: E501
        :type: IoArgoprojEventsV1alpha1S3Filter
        """

        self._filter = filter

    @property
    def insecure(self):
        """Gets the insecure of this IoArgoprojEventsV1alpha1S3Artifact.  # noqa: E501


        :return: The insecure of this IoArgoprojEventsV1alpha1S3Artifact.  # noqa: E501
        :rtype: bool
        """
        return self._insecure

    @insecure.setter
    def insecure(self, insecure):
        """Sets the insecure of this IoArgoprojEventsV1alpha1S3Artifact.


        :param insecure: The insecure of this IoArgoprojEventsV1alpha1S3Artifact.  # noqa: E501
        :type: bool
        """

        self._insecure = insecure

    @property
    def metadata(self):
        """Gets the metadata of this IoArgoprojEventsV1alpha1S3Artifact.  # noqa: E501


        :return: The metadata of this IoArgoprojEventsV1alpha1S3Artifact.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this IoArgoprojEventsV1alpha1S3Artifact.


        :param metadata: The metadata of this IoArgoprojEventsV1alpha1S3Artifact.  # noqa: E501
        :type: dict(str, str)
        """

        self._metadata = metadata

    @property
    def region(self):
        """Gets the region of this IoArgoprojEventsV1alpha1S3Artifact.  # noqa: E501


        :return: The region of this IoArgoprojEventsV1alpha1S3Artifact.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this IoArgoprojEventsV1alpha1S3Artifact.


        :param region: The region of this IoArgoprojEventsV1alpha1S3Artifact.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def secret_key(self):
        """Gets the secret_key of this IoArgoprojEventsV1alpha1S3Artifact.  # noqa: E501


        :return: The secret_key of this IoArgoprojEventsV1alpha1S3Artifact.  # noqa: E501
        :rtype: V1SecretKeySelector
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this IoArgoprojEventsV1alpha1S3Artifact.


        :param secret_key: The secret_key of this IoArgoprojEventsV1alpha1S3Artifact.  # noqa: E501
        :type: V1SecretKeySelector
        """

        self._secret_key = secret_key

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
        if not isinstance(other, IoArgoprojEventsV1alpha1S3Artifact):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojEventsV1alpha1S3Artifact):
            return True

        return self.to_dict() != other.to_dict()
