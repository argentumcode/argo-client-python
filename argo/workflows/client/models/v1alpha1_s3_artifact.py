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


class V1alpha1S3Artifact(object):
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
        'access_key_secret': 'V1SecretKeySelector',
        'bucket': 'str',
        'create_bucket_if_not_present': 'V1alpha1CreateS3BucketOptions',
        'endpoint': 'str',
        'insecure': 'bool',
        'key': 'str',
        'region': 'str',
        'role_arn': 'str',
        'secret_key_secret': 'V1SecretKeySelector',
        'use_sdk_creds': 'bool'
    }

    attribute_map = {
        'access_key_secret': 'accessKeySecret',
        'bucket': 'bucket',
        'create_bucket_if_not_present': 'createBucketIfNotPresent',
        'endpoint': 'endpoint',
        'insecure': 'insecure',
        'key': 'key',
        'region': 'region',
        'role_arn': 'roleARN',
        'secret_key_secret': 'secretKeySecret',
        'use_sdk_creds': 'useSDKCreds'
    }

    def __init__(self, access_key_secret=None, bucket=None, create_bucket_if_not_present=None, endpoint=None, insecure=None, key=None, region=None, role_arn=None, secret_key_secret=None, use_sdk_creds=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1S3Artifact - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._access_key_secret = None
        self._bucket = None
        self._create_bucket_if_not_present = None
        self._endpoint = None
        self._insecure = None
        self._key = None
        self._region = None
        self._role_arn = None
        self._secret_key_secret = None
        self._use_sdk_creds = None
        self.discriminator = None

        if access_key_secret is not None:
            self.access_key_secret = access_key_secret
        if bucket is not None:
            self.bucket = bucket
        if create_bucket_if_not_present is not None:
            self.create_bucket_if_not_present = create_bucket_if_not_present
        if endpoint is not None:
            self.endpoint = endpoint
        if insecure is not None:
            self.insecure = insecure
        self.key = key
        if region is not None:
            self.region = region
        if role_arn is not None:
            self.role_arn = role_arn
        if secret_key_secret is not None:
            self.secret_key_secret = secret_key_secret
        if use_sdk_creds is not None:
            self.use_sdk_creds = use_sdk_creds

    @property
    def access_key_secret(self):
        """Gets the access_key_secret of this V1alpha1S3Artifact.  # noqa: E501


        :return: The access_key_secret of this V1alpha1S3Artifact.  # noqa: E501
        :rtype: V1SecretKeySelector
        """
        return self._access_key_secret

    @access_key_secret.setter
    def access_key_secret(self, access_key_secret):
        """Sets the access_key_secret of this V1alpha1S3Artifact.


        :param access_key_secret: The access_key_secret of this V1alpha1S3Artifact.  # noqa: E501
        :type: V1SecretKeySelector
        """

        self._access_key_secret = access_key_secret

    @property
    def bucket(self):
        """Gets the bucket of this V1alpha1S3Artifact.  # noqa: E501

        Bucket is the name of the bucket  # noqa: E501

        :return: The bucket of this V1alpha1S3Artifact.  # noqa: E501
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this V1alpha1S3Artifact.

        Bucket is the name of the bucket  # noqa: E501

        :param bucket: The bucket of this V1alpha1S3Artifact.  # noqa: E501
        :type: str
        """

        self._bucket = bucket

    @property
    def create_bucket_if_not_present(self):
        """Gets the create_bucket_if_not_present of this V1alpha1S3Artifact.  # noqa: E501


        :return: The create_bucket_if_not_present of this V1alpha1S3Artifact.  # noqa: E501
        :rtype: V1alpha1CreateS3BucketOptions
        """
        return self._create_bucket_if_not_present

    @create_bucket_if_not_present.setter
    def create_bucket_if_not_present(self, create_bucket_if_not_present):
        """Sets the create_bucket_if_not_present of this V1alpha1S3Artifact.


        :param create_bucket_if_not_present: The create_bucket_if_not_present of this V1alpha1S3Artifact.  # noqa: E501
        :type: V1alpha1CreateS3BucketOptions
        """

        self._create_bucket_if_not_present = create_bucket_if_not_present

    @property
    def endpoint(self):
        """Gets the endpoint of this V1alpha1S3Artifact.  # noqa: E501

        Endpoint is the hostname of the bucket endpoint  # noqa: E501

        :return: The endpoint of this V1alpha1S3Artifact.  # noqa: E501
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this V1alpha1S3Artifact.

        Endpoint is the hostname of the bucket endpoint  # noqa: E501

        :param endpoint: The endpoint of this V1alpha1S3Artifact.  # noqa: E501
        :type: str
        """

        self._endpoint = endpoint

    @property
    def insecure(self):
        """Gets the insecure of this V1alpha1S3Artifact.  # noqa: E501

        Insecure will connect to the service with TLS  # noqa: E501

        :return: The insecure of this V1alpha1S3Artifact.  # noqa: E501
        :rtype: bool
        """
        return self._insecure

    @insecure.setter
    def insecure(self, insecure):
        """Sets the insecure of this V1alpha1S3Artifact.

        Insecure will connect to the service with TLS  # noqa: E501

        :param insecure: The insecure of this V1alpha1S3Artifact.  # noqa: E501
        :type: bool
        """

        self._insecure = insecure

    @property
    def key(self):
        """Gets the key of this V1alpha1S3Artifact.  # noqa: E501

        Key is the key in the bucket where the artifact resides  # noqa: E501

        :return: The key of this V1alpha1S3Artifact.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this V1alpha1S3Artifact.

        Key is the key in the bucket where the artifact resides  # noqa: E501

        :param key: The key of this V1alpha1S3Artifact.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and key is None:  # noqa: E501
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def region(self):
        """Gets the region of this V1alpha1S3Artifact.  # noqa: E501

        Region contains the optional bucket region  # noqa: E501

        :return: The region of this V1alpha1S3Artifact.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this V1alpha1S3Artifact.

        Region contains the optional bucket region  # noqa: E501

        :param region: The region of this V1alpha1S3Artifact.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def role_arn(self):
        """Gets the role_arn of this V1alpha1S3Artifact.  # noqa: E501

        RoleARN is the Amazon Resource Name (ARN) of the role to assume.  # noqa: E501

        :return: The role_arn of this V1alpha1S3Artifact.  # noqa: E501
        :rtype: str
        """
        return self._role_arn

    @role_arn.setter
    def role_arn(self, role_arn):
        """Sets the role_arn of this V1alpha1S3Artifact.

        RoleARN is the Amazon Resource Name (ARN) of the role to assume.  # noqa: E501

        :param role_arn: The role_arn of this V1alpha1S3Artifact.  # noqa: E501
        :type: str
        """

        self._role_arn = role_arn

    @property
    def secret_key_secret(self):
        """Gets the secret_key_secret of this V1alpha1S3Artifact.  # noqa: E501


        :return: The secret_key_secret of this V1alpha1S3Artifact.  # noqa: E501
        :rtype: V1SecretKeySelector
        """
        return self._secret_key_secret

    @secret_key_secret.setter
    def secret_key_secret(self, secret_key_secret):
        """Sets the secret_key_secret of this V1alpha1S3Artifact.


        :param secret_key_secret: The secret_key_secret of this V1alpha1S3Artifact.  # noqa: E501
        :type: V1SecretKeySelector
        """

        self._secret_key_secret = secret_key_secret

    @property
    def use_sdk_creds(self):
        """Gets the use_sdk_creds of this V1alpha1S3Artifact.  # noqa: E501

        UseSDKCreds tells the driver to figure out credentials based on sdk defaults.  # noqa: E501

        :return: The use_sdk_creds of this V1alpha1S3Artifact.  # noqa: E501
        :rtype: bool
        """
        return self._use_sdk_creds

    @use_sdk_creds.setter
    def use_sdk_creds(self, use_sdk_creds):
        """Sets the use_sdk_creds of this V1alpha1S3Artifact.

        UseSDKCreds tells the driver to figure out credentials based on sdk defaults.  # noqa: E501

        :param use_sdk_creds: The use_sdk_creds of this V1alpha1S3Artifact.  # noqa: E501
        :type: bool
        """

        self._use_sdk_creds = use_sdk_creds

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
        if not isinstance(other, V1alpha1S3Artifact):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1S3Artifact):
            return True

        return self.to_dict() != other.to_dict()
