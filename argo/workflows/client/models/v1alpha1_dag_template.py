# coding: utf-8

"""
    Argo

    Python client for Argo Workflows  # noqa: E501

    OpenAPI spec version: ${GIT_TAG/argo//}
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from argo.workflows.client.models.v1alpha1_dag_task import V1alpha1DAGTask  # noqa: F401,E501


class V1alpha1DAGTemplate(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'target': 'str',
        'tasks': 'list[V1alpha1DAGTask]'
    }

    attribute_map = {
        'target': 'target',
        'tasks': 'tasks'
    }

    def __init__(self, target=None, tasks=None):  # noqa: E501
        """V1alpha1DAGTemplate - a model defined in Swagger"""  # noqa: E501

        self._target = None
        self._tasks = None
        self.discriminator = None

        if target is not None:
            self.target = target
        self.tasks = tasks

    @property
    def target(self):
        """Gets the target of this V1alpha1DAGTemplate.  # noqa: E501

        Target are one or more names of targets to execute in a DAG  # noqa: E501

        :return: The target of this V1alpha1DAGTemplate.  # noqa: E501
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this V1alpha1DAGTemplate.

        Target are one or more names of targets to execute in a DAG  # noqa: E501

        :param target: The target of this V1alpha1DAGTemplate.  # noqa: E501
        :type: str
        """

        self._target = target

    @property
    def tasks(self):
        """Gets the tasks of this V1alpha1DAGTemplate.  # noqa: E501

        Tasks are a list of DAG tasks  # noqa: E501

        :return: The tasks of this V1alpha1DAGTemplate.  # noqa: E501
        :rtype: list[V1alpha1DAGTask]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this V1alpha1DAGTemplate.

        Tasks are a list of DAG tasks  # noqa: E501

        :param tasks: The tasks of this V1alpha1DAGTemplate.  # noqa: E501
        :type: list[V1alpha1DAGTask]
        """
        if tasks is None:
            raise ValueError("Invalid value for `tasks`, must not be `None`")  # noqa: E501

        self._tasks = tasks

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, V1alpha1DAGTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
