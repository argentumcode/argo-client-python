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


class IoArgoprojEventsV1alpha1HDFSEventSource(object):
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
        'addresses': 'list[str]',
        'check_interval': 'str',
        'hdfs_user': 'str',
        'krb_c_cache_secret': 'V1SecretKeySelector',
        'krb_config_config_map': 'V1ConfigMapKeySelector',
        'krb_keytab_secret': 'V1SecretKeySelector',
        'krb_realm': 'str',
        'krb_service_principal_name': 'str',
        'krb_username': 'str',
        'metadata': 'dict(str, str)',
        'type': 'str',
        'watch_path_config': 'IoArgoprojEventsV1alpha1WatchPathConfig'
    }

    attribute_map = {
        'addresses': 'addresses',
        'check_interval': 'checkInterval',
        'hdfs_user': 'hdfsUser',
        'krb_c_cache_secret': 'krbCCacheSecret',
        'krb_config_config_map': 'krbConfigConfigMap',
        'krb_keytab_secret': 'krbKeytabSecret',
        'krb_realm': 'krbRealm',
        'krb_service_principal_name': 'krbServicePrincipalName',
        'krb_username': 'krbUsername',
        'metadata': 'metadata',
        'type': 'type',
        'watch_path_config': 'watchPathConfig'
    }

    def __init__(self, addresses=None, check_interval=None, hdfs_user=None, krb_c_cache_secret=None, krb_config_config_map=None, krb_keytab_secret=None, krb_realm=None, krb_service_principal_name=None, krb_username=None, metadata=None, type=None, watch_path_config=None, local_vars_configuration=None):  # noqa: E501
        """IoArgoprojEventsV1alpha1HDFSEventSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._addresses = None
        self._check_interval = None
        self._hdfs_user = None
        self._krb_c_cache_secret = None
        self._krb_config_config_map = None
        self._krb_keytab_secret = None
        self._krb_realm = None
        self._krb_service_principal_name = None
        self._krb_username = None
        self._metadata = None
        self._type = None
        self._watch_path_config = None
        self.discriminator = None

        if addresses is not None:
            self.addresses = addresses
        if check_interval is not None:
            self.check_interval = check_interval
        if hdfs_user is not None:
            self.hdfs_user = hdfs_user
        if krb_c_cache_secret is not None:
            self.krb_c_cache_secret = krb_c_cache_secret
        if krb_config_config_map is not None:
            self.krb_config_config_map = krb_config_config_map
        if krb_keytab_secret is not None:
            self.krb_keytab_secret = krb_keytab_secret
        if krb_realm is not None:
            self.krb_realm = krb_realm
        if krb_service_principal_name is not None:
            self.krb_service_principal_name = krb_service_principal_name
        if krb_username is not None:
            self.krb_username = krb_username
        if metadata is not None:
            self.metadata = metadata
        if type is not None:
            self.type = type
        if watch_path_config is not None:
            self.watch_path_config = watch_path_config

    @property
    def addresses(self):
        """Gets the addresses of this IoArgoprojEventsV1alpha1HDFSEventSource.  # noqa: E501


        :return: The addresses of this IoArgoprojEventsV1alpha1HDFSEventSource.  # noqa: E501
        :rtype: list[str]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this IoArgoprojEventsV1alpha1HDFSEventSource.


        :param addresses: The addresses of this IoArgoprojEventsV1alpha1HDFSEventSource.  # noqa: E501
        :type: list[str]
        """

        self._addresses = addresses

    @property
    def check_interval(self):
        """Gets the check_interval of this IoArgoprojEventsV1alpha1HDFSEventSource.  # noqa: E501


        :return: The check_interval of this IoArgoprojEventsV1alpha1HDFSEventSource.  # noqa: E501
        :rtype: str
        """
        return self._check_interval

    @check_interval.setter
    def check_interval(self, check_interval):
        """Sets the check_interval of this IoArgoprojEventsV1alpha1HDFSEventSource.


        :param check_interval: The check_interval of this IoArgoprojEventsV1alpha1HDFSEventSource.  # noqa: E501
        :type: str
        """

        self._check_interval = check_interval

    @property
    def hdfs_user(self):
        """Gets the hdfs_user of this IoArgoprojEventsV1alpha1HDFSEventSource.  # noqa: E501

        HDFSUser is the user to access HDFS file system. It is ignored if either ccache or keytab is used.  # noqa: E501

        :return: The hdfs_user of this IoArgoprojEventsV1alpha1HDFSEventSource.  # noqa: E501
        :rtype: str
        """
        return self._hdfs_user

    @hdfs_user.setter
    def hdfs_user(self, hdfs_user):
        """Sets the hdfs_user of this IoArgoprojEventsV1alpha1HDFSEventSource.

        HDFSUser is the user to access HDFS file system. It is ignored if either ccache or keytab is used.  # noqa: E501

        :param hdfs_user: The hdfs_user of this IoArgoprojEventsV1alpha1HDFSEventSource.  # noqa: E501
        :type: str
        """

        self._hdfs_user = hdfs_user

    @property
    def krb_c_cache_secret(self):
        """Gets the krb_c_cache_secret of this IoArgoprojEventsV1alpha1HDFSEventSource.  # noqa: E501


        :return: The krb_c_cache_secret of this IoArgoprojEventsV1alpha1HDFSEventSource.  # noqa: E501
        :rtype: V1SecretKeySelector
        """
        return self._krb_c_cache_secret

    @krb_c_cache_secret.setter
    def krb_c_cache_secret(self, krb_c_cache_secret):
        """Sets the krb_c_cache_secret of this IoArgoprojEventsV1alpha1HDFSEventSource.


        :param krb_c_cache_secret: The krb_c_cache_secret of this IoArgoprojEventsV1alpha1HDFSEventSource.  # noqa: E501
        :type: V1SecretKeySelector
        """

        self._krb_c_cache_secret = krb_c_cache_secret

    @property
    def krb_config_config_map(self):
        """Gets the krb_config_config_map of this IoArgoprojEventsV1alpha1HDFSEventSource.  # noqa: E501


        :return: The krb_config_config_map of this IoArgoprojEventsV1alpha1HDFSEventSource.  # noqa: E501
        :rtype: V1ConfigMapKeySelector
        """
        return self._krb_config_config_map

    @krb_config_config_map.setter
    def krb_config_config_map(self, krb_config_config_map):
        """Sets the krb_config_config_map of this IoArgoprojEventsV1alpha1HDFSEventSource.


        :param krb_config_config_map: The krb_config_config_map of this IoArgoprojEventsV1alpha1HDFSEventSource.  # noqa: E501
        :type: V1ConfigMapKeySelector
        """

        self._krb_config_config_map = krb_config_config_map

    @property
    def krb_keytab_secret(self):
        """Gets the krb_keytab_secret of this IoArgoprojEventsV1alpha1HDFSEventSource.  # noqa: E501


        :return: The krb_keytab_secret of this IoArgoprojEventsV1alpha1HDFSEventSource.  # noqa: E501
        :rtype: V1SecretKeySelector
        """
        return self._krb_keytab_secret

    @krb_keytab_secret.setter
    def krb_keytab_secret(self, krb_keytab_secret):
        """Sets the krb_keytab_secret of this IoArgoprojEventsV1alpha1HDFSEventSource.


        :param krb_keytab_secret: The krb_keytab_secret of this IoArgoprojEventsV1alpha1HDFSEventSource.  # noqa: E501
        :type: V1SecretKeySelector
        """

        self._krb_keytab_secret = krb_keytab_secret

    @property
    def krb_realm(self):
        """Gets the krb_realm of this IoArgoprojEventsV1alpha1HDFSEventSource.  # noqa: E501

        KrbRealm is the Kerberos realm used with Kerberos keytab It must be set if keytab is used.  # noqa: E501

        :return: The krb_realm of this IoArgoprojEventsV1alpha1HDFSEventSource.  # noqa: E501
        :rtype: str
        """
        return self._krb_realm

    @krb_realm.setter
    def krb_realm(self, krb_realm):
        """Sets the krb_realm of this IoArgoprojEventsV1alpha1HDFSEventSource.

        KrbRealm is the Kerberos realm used with Kerberos keytab It must be set if keytab is used.  # noqa: E501

        :param krb_realm: The krb_realm of this IoArgoprojEventsV1alpha1HDFSEventSource.  # noqa: E501
        :type: str
        """

        self._krb_realm = krb_realm

    @property
    def krb_service_principal_name(self):
        """Gets the krb_service_principal_name of this IoArgoprojEventsV1alpha1HDFSEventSource.  # noqa: E501

        KrbServicePrincipalName is the principal name of Kerberos service It must be set if either ccache or keytab is used.  # noqa: E501

        :return: The krb_service_principal_name of this IoArgoprojEventsV1alpha1HDFSEventSource.  # noqa: E501
        :rtype: str
        """
        return self._krb_service_principal_name

    @krb_service_principal_name.setter
    def krb_service_principal_name(self, krb_service_principal_name):
        """Sets the krb_service_principal_name of this IoArgoprojEventsV1alpha1HDFSEventSource.

        KrbServicePrincipalName is the principal name of Kerberos service It must be set if either ccache or keytab is used.  # noqa: E501

        :param krb_service_principal_name: The krb_service_principal_name of this IoArgoprojEventsV1alpha1HDFSEventSource.  # noqa: E501
        :type: str
        """

        self._krb_service_principal_name = krb_service_principal_name

    @property
    def krb_username(self):
        """Gets the krb_username of this IoArgoprojEventsV1alpha1HDFSEventSource.  # noqa: E501

        KrbUsername is the Kerberos username used with Kerberos keytab It must be set if keytab is used.  # noqa: E501

        :return: The krb_username of this IoArgoprojEventsV1alpha1HDFSEventSource.  # noqa: E501
        :rtype: str
        """
        return self._krb_username

    @krb_username.setter
    def krb_username(self, krb_username):
        """Sets the krb_username of this IoArgoprojEventsV1alpha1HDFSEventSource.

        KrbUsername is the Kerberos username used with Kerberos keytab It must be set if keytab is used.  # noqa: E501

        :param krb_username: The krb_username of this IoArgoprojEventsV1alpha1HDFSEventSource.  # noqa: E501
        :type: str
        """

        self._krb_username = krb_username

    @property
    def metadata(self):
        """Gets the metadata of this IoArgoprojEventsV1alpha1HDFSEventSource.  # noqa: E501


        :return: The metadata of this IoArgoprojEventsV1alpha1HDFSEventSource.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this IoArgoprojEventsV1alpha1HDFSEventSource.


        :param metadata: The metadata of this IoArgoprojEventsV1alpha1HDFSEventSource.  # noqa: E501
        :type: dict(str, str)
        """

        self._metadata = metadata

    @property
    def type(self):
        """Gets the type of this IoArgoprojEventsV1alpha1HDFSEventSource.  # noqa: E501


        :return: The type of this IoArgoprojEventsV1alpha1HDFSEventSource.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IoArgoprojEventsV1alpha1HDFSEventSource.


        :param type: The type of this IoArgoprojEventsV1alpha1HDFSEventSource.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def watch_path_config(self):
        """Gets the watch_path_config of this IoArgoprojEventsV1alpha1HDFSEventSource.  # noqa: E501


        :return: The watch_path_config of this IoArgoprojEventsV1alpha1HDFSEventSource.  # noqa: E501
        :rtype: IoArgoprojEventsV1alpha1WatchPathConfig
        """
        return self._watch_path_config

    @watch_path_config.setter
    def watch_path_config(self, watch_path_config):
        """Sets the watch_path_config of this IoArgoprojEventsV1alpha1HDFSEventSource.


        :param watch_path_config: The watch_path_config of this IoArgoprojEventsV1alpha1HDFSEventSource.  # noqa: E501
        :type: IoArgoprojEventsV1alpha1WatchPathConfig
        """

        self._watch_path_config = watch_path_config

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
        if not isinstance(other, IoArgoprojEventsV1alpha1HDFSEventSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoArgoprojEventsV1alpha1HDFSEventSource):
            return True

        return self.to_dict() != other.to_dict()
