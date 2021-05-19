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


class IoArgoprojEventsV1alpha1StripeEventSource(object):
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
        'api_key': 'V1SecretKeySelector',
        'create_webhook': 'bool',
        'event_filter': 'list[str]',
        'metadata': 'dict(str, str)',
        'webhook': 'IoArgoprojEventsV1alpha1WebhookContext'
    }

    attribute_map = {
        'api_key': 'apiKey',
        'create_webhook': 'createWebhook',
        'event_filter': 'eventFilter',
        'metadata': 'metadata',
        'webhook': 'webhook'
    }

    def __init__(self, api_key=None, create_webhook=None, event_filter=None, metadata=None, webhook=None, local_vars_configuration=None):  # noqa: E501
        """IoArgoprojEventsV1alpha1StripeEventSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._api_key = None
        self._create_webhook = None
        self._event_filter = None
        self._metadata = None
        self._webhook = None
        self.discriminator = None

        if api_key is not None:
            self.api_key = api_key
        if create_webhook is not None:
            self.create_webhook = create_webhook
        if event_filter is not None:
            self.event_filter = event_filter
        if metadata is not None:
            self.metadata = metadata
        if webhook is not None:
            self.webhook = webhook

    @property
    def api_key(self):
        """Gets the api_key of this IoArgoprojEventsV1alpha1StripeEventSource.  # noqa: E501


        :return: The api_key of this IoArgoprojEventsV1alpha1StripeEventSource.  # noqa: E501
        :rtype: V1SecretKeySelector
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this IoArgoprojEventsV1alpha1StripeEventSource.


        :param api_key: The api_key of this IoArgoprojEventsV1alpha1StripeEventSource.  # noqa: E501
        :type: V1SecretKeySelector
        """

        self._api_key = api_key

    @property
    def create_webhook(self):
        """Gets the create_webhook of this IoArgoprojEventsV1alpha1StripeEventSource.  # noqa: E501


        :return: The create_webhook of this IoArgoprojEventsV1alpha1StripeEventSource.  # noqa: E501
        :rtype: bool
        """
        return self._create_webhook

    @create_webhook.setter
    def create_webhook(self, create_webhook):
        """Sets the create_webhook of this IoArgoprojEventsV1alpha1StripeEventSource.


        :param create_webhook: The create_webhook of this IoArgoprojEventsV1alpha1StripeEventSource.  # noqa: E501
        :type: bool
        """

        self._create_webhook = create_webhook

    @property
    def event_filter(self):
        """Gets the event_filter of this IoArgoprojEventsV1alpha1StripeEventSource.  # noqa: E501


        :return: The event_filter of this IoArgoprojEventsV1alpha1StripeEventSource.  # noqa: E501
        :rtype: list[str]
        """
        return self._event_filter

    @event_filter.setter
    def event_filter(self, event_filter):
        """Sets the event_filter of this IoArgoprojEventsV1alpha1StripeEventSource.


        :param event_filter: The event_filter of this IoArgoprojEventsV1alpha1StripeEventSource.  # noqa: E501
        :type: list[str]
        """

        self._event_filter = event_filter

    @property
    def metadata(self):
        """Gets the metadata of this IoArgoprojEventsV1alpha1StripeEventSource.  # noqa: E501


        :return: The metadata of this IoArgoprojEventsV1alpha1StripeEventSource.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this IoArgoprojEventsV1alpha1StripeEventSource.


        :param metadata: The metadata of this IoArgoprojEventsV1alpha1StripeEventSource.  # noqa: E501
        :type: dict(str, str)
        """

        self._metadata = metadata

    @property
    def webhook(self):
        """Gets the webhook of this IoArgoprojEventsV1alpha1StripeEventSource.  # noqa: E501


        :return: The webhook of this IoArgoprojEventsV1alpha1StripeEventSource.  # noqa: E501
        :rtype: IoArgoprojEventsV1alpha1WebhookContext
        """
        return self._webhook

    @webhook.setter
    def webhook(self, webhook):
        """Sets the webhook of this IoArgoprojEventsV1alpha1StripeEventSource.


        :param webhook: The webhook of this IoArgoprojEventsV1alpha1StripeEventSource.  # noqa: E501
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
        if not isinstance(other, IoArgoprojEventsV1alpha1StripeEventSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojEventsV1alpha1StripeEventSource):
            return True

        return self.to_dict() != other.to_dict()
