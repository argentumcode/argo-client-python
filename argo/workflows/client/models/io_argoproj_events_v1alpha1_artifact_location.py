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


class IoArgoprojEventsV1alpha1ArtifactLocation(object):
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
        'configmap': 'V1ConfigMapKeySelector',
        'file': 'IoArgoprojEventsV1alpha1FileArtifact',
        'git': 'IoArgoprojEventsV1alpha1GitArtifact',
        'inline': 'str',
        'resource': 'IoArgoprojEventsV1alpha1Resource',
        's3': 'IoArgoprojEventsV1alpha1S3Artifact',
        'url': 'IoArgoprojEventsV1alpha1URLArtifact'
    }

    attribute_map = {
        'configmap': 'configmap',
        'file': 'file',
        'git': 'git',
        'inline': 'inline',
        'resource': 'resource',
        's3': 's3',
        'url': 'url'
    }

    def __init__(self, configmap=None, file=None, git=None, inline=None, resource=None, s3=None, url=None, local_vars_configuration=None):  # noqa: E501
        """IoArgoprojEventsV1alpha1ArtifactLocation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._configmap = None
        self._file = None
        self._git = None
        self._inline = None
        self._resource = None
        self._s3 = None
        self._url = None
        self.discriminator = None

        if configmap is not None:
            self.configmap = configmap
        if file is not None:
            self.file = file
        if git is not None:
            self.git = git
        if inline is not None:
            self.inline = inline
        if resource is not None:
            self.resource = resource
        if s3 is not None:
            self.s3 = s3
        if url is not None:
            self.url = url

    @property
    def configmap(self):
        """Gets the configmap of this IoArgoprojEventsV1alpha1ArtifactLocation.  # noqa: E501


        :return: The configmap of this IoArgoprojEventsV1alpha1ArtifactLocation.  # noqa: E501
        :rtype: V1ConfigMapKeySelector
        """
        return self._configmap

    @configmap.setter
    def configmap(self, configmap):
        """Sets the configmap of this IoArgoprojEventsV1alpha1ArtifactLocation.


        :param configmap: The configmap of this IoArgoprojEventsV1alpha1ArtifactLocation.  # noqa: E501
        :type: V1ConfigMapKeySelector
        """

        self._configmap = configmap

    @property
    def file(self):
        """Gets the file of this IoArgoprojEventsV1alpha1ArtifactLocation.  # noqa: E501


        :return: The file of this IoArgoprojEventsV1alpha1ArtifactLocation.  # noqa: E501
        :rtype: IoArgoprojEventsV1alpha1FileArtifact
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this IoArgoprojEventsV1alpha1ArtifactLocation.


        :param file: The file of this IoArgoprojEventsV1alpha1ArtifactLocation.  # noqa: E501
        :type: IoArgoprojEventsV1alpha1FileArtifact
        """

        self._file = file

    @property
    def git(self):
        """Gets the git of this IoArgoprojEventsV1alpha1ArtifactLocation.  # noqa: E501


        :return: The git of this IoArgoprojEventsV1alpha1ArtifactLocation.  # noqa: E501
        :rtype: IoArgoprojEventsV1alpha1GitArtifact
        """
        return self._git

    @git.setter
    def git(self, git):
        """Sets the git of this IoArgoprojEventsV1alpha1ArtifactLocation.


        :param git: The git of this IoArgoprojEventsV1alpha1ArtifactLocation.  # noqa: E501
        :type: IoArgoprojEventsV1alpha1GitArtifact
        """

        self._git = git

    @property
    def inline(self):
        """Gets the inline of this IoArgoprojEventsV1alpha1ArtifactLocation.  # noqa: E501


        :return: The inline of this IoArgoprojEventsV1alpha1ArtifactLocation.  # noqa: E501
        :rtype: str
        """
        return self._inline

    @inline.setter
    def inline(self, inline):
        """Sets the inline of this IoArgoprojEventsV1alpha1ArtifactLocation.


        :param inline: The inline of this IoArgoprojEventsV1alpha1ArtifactLocation.  # noqa: E501
        :type: str
        """

        self._inline = inline

    @property
    def resource(self):
        """Gets the resource of this IoArgoprojEventsV1alpha1ArtifactLocation.  # noqa: E501


        :return: The resource of this IoArgoprojEventsV1alpha1ArtifactLocation.  # noqa: E501
        :rtype: IoArgoprojEventsV1alpha1Resource
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this IoArgoprojEventsV1alpha1ArtifactLocation.


        :param resource: The resource of this IoArgoprojEventsV1alpha1ArtifactLocation.  # noqa: E501
        :type: IoArgoprojEventsV1alpha1Resource
        """

        self._resource = resource

    @property
    def s3(self):
        """Gets the s3 of this IoArgoprojEventsV1alpha1ArtifactLocation.  # noqa: E501


        :return: The s3 of this IoArgoprojEventsV1alpha1ArtifactLocation.  # noqa: E501
        :rtype: IoArgoprojEventsV1alpha1S3Artifact
        """
        return self._s3

    @s3.setter
    def s3(self, s3):
        """Sets the s3 of this IoArgoprojEventsV1alpha1ArtifactLocation.


        :param s3: The s3 of this IoArgoprojEventsV1alpha1ArtifactLocation.  # noqa: E501
        :type: IoArgoprojEventsV1alpha1S3Artifact
        """

        self._s3 = s3

    @property
    def url(self):
        """Gets the url of this IoArgoprojEventsV1alpha1ArtifactLocation.  # noqa: E501


        :return: The url of this IoArgoprojEventsV1alpha1ArtifactLocation.  # noqa: E501
        :rtype: IoArgoprojEventsV1alpha1URLArtifact
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this IoArgoprojEventsV1alpha1ArtifactLocation.


        :param url: The url of this IoArgoprojEventsV1alpha1ArtifactLocation.  # noqa: E501
        :type: IoArgoprojEventsV1alpha1URLArtifact
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
        if not isinstance(other, IoArgoprojEventsV1alpha1ArtifactLocation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojEventsV1alpha1ArtifactLocation):
            return True

        return self.to_dict() != other.to_dict()
