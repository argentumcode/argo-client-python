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


class V1alpha1ArchiveStrategy(object):
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
        '_none': 'object',
        'tar': 'V1alpha1TarStrategy',
        'zip': 'object'
    }

    attribute_map = {
        '_none': 'none',
        'tar': 'tar',
        'zip': 'zip'
    }

    def __init__(self, _none=None, tar=None, zip=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1ArchiveStrategy - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self.__none = None
        self._tar = None
        self._zip = None
        self.discriminator = None

        if _none is not None:
            self._none = _none
        if tar is not None:
            self.tar = tar
        if zip is not None:
            self.zip = zip

    @property
    def _none(self):
        """Gets the _none of this V1alpha1ArchiveStrategy.  # noqa: E501

        NoneStrategy indicates to skip tar process and upload the files or directory tree as independent files. Note that if the artifact is a directory, the artifact driver must support the ability to save/load the directory appropriately.  # noqa: E501

        :return: The _none of this V1alpha1ArchiveStrategy.  # noqa: E501
        :rtype: object
        """
        return self.__none

    @_none.setter
    def _none(self, _none):
        """Sets the _none of this V1alpha1ArchiveStrategy.

        NoneStrategy indicates to skip tar process and upload the files or directory tree as independent files. Note that if the artifact is a directory, the artifact driver must support the ability to save/load the directory appropriately.  # noqa: E501

        :param _none: The _none of this V1alpha1ArchiveStrategy.  # noqa: E501
        :type: object
        """

        self.__none = _none

    @property
    def tar(self):
        """Gets the tar of this V1alpha1ArchiveStrategy.  # noqa: E501


        :return: The tar of this V1alpha1ArchiveStrategy.  # noqa: E501
        :rtype: V1alpha1TarStrategy
        """
        return self._tar

    @tar.setter
    def tar(self, tar):
        """Sets the tar of this V1alpha1ArchiveStrategy.


        :param tar: The tar of this V1alpha1ArchiveStrategy.  # noqa: E501
        :type: V1alpha1TarStrategy
        """

        self._tar = tar

    @property
    def zip(self):
        """Gets the zip of this V1alpha1ArchiveStrategy.  # noqa: E501

        ZipStrategy will unzip zipped input artifacts  # noqa: E501

        :return: The zip of this V1alpha1ArchiveStrategy.  # noqa: E501
        :rtype: object
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this V1alpha1ArchiveStrategy.

        ZipStrategy will unzip zipped input artifacts  # noqa: E501

        :param zip: The zip of this V1alpha1ArchiveStrategy.  # noqa: E501
        :type: object
        """

        self._zip = zip

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
        if not isinstance(other, V1alpha1ArchiveStrategy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1ArchiveStrategy):
            return True

        return self.to_dict() != other.to_dict()
