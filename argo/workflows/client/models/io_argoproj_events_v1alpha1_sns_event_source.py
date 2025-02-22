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


class IoArgoprojEventsV1alpha1SNSEventSource(object):
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
        'metadata': 'dict(str, str)',
        'region': 'str',
        'role_arn': 'str',
        'secret_key': 'V1SecretKeySelector',
        'topic_arn': 'str',
        'validate_signature': 'bool',
        'webhook': 'IoArgoprojEventsV1alpha1WebhookContext'
    }

    attribute_map = {
        'access_key': 'accessKey',
        'metadata': 'metadata',
        'region': 'region',
        'role_arn': 'roleARN',
        'secret_key': 'secretKey',
        'topic_arn': 'topicArn',
        'validate_signature': 'validateSignature',
        'webhook': 'webhook'
    }

    def __init__(self, access_key=None, metadata=None, region=None, role_arn=None, secret_key=None, topic_arn=None, validate_signature=None, webhook=None, local_vars_configuration=None):  # noqa: E501
        """IoArgoprojEventsV1alpha1SNSEventSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._access_key = None
        self._metadata = None
        self._region = None
        self._role_arn = None
        self._secret_key = None
        self._topic_arn = None
        self._validate_signature = None
        self._webhook = None
        self.discriminator = None

        if access_key is not None:
            self.access_key = access_key
        if metadata is not None:
            self.metadata = metadata
        if region is not None:
            self.region = region
        if role_arn is not None:
            self.role_arn = role_arn
        if secret_key is not None:
            self.secret_key = secret_key
        if topic_arn is not None:
            self.topic_arn = topic_arn
        if validate_signature is not None:
            self.validate_signature = validate_signature
        if webhook is not None:
            self.webhook = webhook

    @property
    def access_key(self):
        """Gets the access_key of this IoArgoprojEventsV1alpha1SNSEventSource.  # noqa: E501


        :return: The access_key of this IoArgoprojEventsV1alpha1SNSEventSource.  # noqa: E501
        :rtype: V1SecretKeySelector
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this IoArgoprojEventsV1alpha1SNSEventSource.


        :param access_key: The access_key of this IoArgoprojEventsV1alpha1SNSEventSource.  # noqa: E501
        :type: V1SecretKeySelector
        """

        self._access_key = access_key

    @property
    def metadata(self):
        """Gets the metadata of this IoArgoprojEventsV1alpha1SNSEventSource.  # noqa: E501


        :return: The metadata of this IoArgoprojEventsV1alpha1SNSEventSource.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this IoArgoprojEventsV1alpha1SNSEventSource.


        :param metadata: The metadata of this IoArgoprojEventsV1alpha1SNSEventSource.  # noqa: E501
        :type: dict(str, str)
        """

        self._metadata = metadata

    @property
    def region(self):
        """Gets the region of this IoArgoprojEventsV1alpha1SNSEventSource.  # noqa: E501


        :return: The region of this IoArgoprojEventsV1alpha1SNSEventSource.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this IoArgoprojEventsV1alpha1SNSEventSource.


        :param region: The region of this IoArgoprojEventsV1alpha1SNSEventSource.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def role_arn(self):
        """Gets the role_arn of this IoArgoprojEventsV1alpha1SNSEventSource.  # noqa: E501


        :return: The role_arn of this IoArgoprojEventsV1alpha1SNSEventSource.  # noqa: E501
        :rtype: str
        """
        return self._role_arn

    @role_arn.setter
    def role_arn(self, role_arn):
        """Sets the role_arn of this IoArgoprojEventsV1alpha1SNSEventSource.


        :param role_arn: The role_arn of this IoArgoprojEventsV1alpha1SNSEventSource.  # noqa: E501
        :type: str
        """

        self._role_arn = role_arn

    @property
    def secret_key(self):
        """Gets the secret_key of this IoArgoprojEventsV1alpha1SNSEventSource.  # noqa: E501


        :return: The secret_key of this IoArgoprojEventsV1alpha1SNSEventSource.  # noqa: E501
        :rtype: V1SecretKeySelector
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this IoArgoprojEventsV1alpha1SNSEventSource.


        :param secret_key: The secret_key of this IoArgoprojEventsV1alpha1SNSEventSource.  # noqa: E501
        :type: V1SecretKeySelector
        """

        self._secret_key = secret_key

    @property
    def topic_arn(self):
        """Gets the topic_arn of this IoArgoprojEventsV1alpha1SNSEventSource.  # noqa: E501


        :return: The topic_arn of this IoArgoprojEventsV1alpha1SNSEventSource.  # noqa: E501
        :rtype: str
        """
        return self._topic_arn

    @topic_arn.setter
    def topic_arn(self, topic_arn):
        """Sets the topic_arn of this IoArgoprojEventsV1alpha1SNSEventSource.


        :param topic_arn: The topic_arn of this IoArgoprojEventsV1alpha1SNSEventSource.  # noqa: E501
        :type: str
        """

        self._topic_arn = topic_arn

    @property
    def validate_signature(self):
        """Gets the validate_signature of this IoArgoprojEventsV1alpha1SNSEventSource.  # noqa: E501


        :return: The validate_signature of this IoArgoprojEventsV1alpha1SNSEventSource.  # noqa: E501
        :rtype: bool
        """
        return self._validate_signature

    @validate_signature.setter
    def validate_signature(self, validate_signature):
        """Sets the validate_signature of this IoArgoprojEventsV1alpha1SNSEventSource.


        :param validate_signature: The validate_signature of this IoArgoprojEventsV1alpha1SNSEventSource.  # noqa: E501
        :type: bool
        """

        self._validate_signature = validate_signature

    @property
    def webhook(self):
        """Gets the webhook of this IoArgoprojEventsV1alpha1SNSEventSource.  # noqa: E501


        :return: The webhook of this IoArgoprojEventsV1alpha1SNSEventSource.  # noqa: E501
        :rtype: IoArgoprojEventsV1alpha1WebhookContext
        """
        return self._webhook

    @webhook.setter
    def webhook(self, webhook):
        """Sets the webhook of this IoArgoprojEventsV1alpha1SNSEventSource.


        :param webhook: The webhook of this IoArgoprojEventsV1alpha1SNSEventSource.  # noqa: E501
        :type: IoArgoprojEventsV1alpha1WebhookContext
        """

        self._webhook = webhook

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
        if not isinstance(other, IoArgoprojEventsV1alpha1SNSEventSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojEventsV1alpha1SNSEventSource):
            return True

        return self.to_dict() != other.to_dict()
