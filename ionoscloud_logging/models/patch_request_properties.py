# coding: utf-8

"""
    IONOS Logging REST API

    Logging as a Service (LaaS) is a service that provides a centralized logging system where users are able to push and aggregate their system or application logs. This service also provides a visualization platform where users are able to observe, search and filter the logs and also create dashboards and alerts for their data points. This service can be managed through a browser-based \"Data Center Designer\" (DCD) tool or via an API. The API allows you to create logging pipelines or modify existing ones. It is designed to allow users to leverage the same power and flexibility found within the DCD visual tool. Both tools are consistent with their concepts and lend well to making the experience smooth and intuitive.  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ionoscloud_logging.configuration import Configuration


class PatchRequestProperties(object):
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

        'name': 'str',

        'logs': 'list[PatchRequestPipeline]',
    }

    attribute_map = {

        'name': 'name',

        'logs': 'logs',
    }

    def __init__(self, name=None, logs=None, local_vars_configuration=None):  # noqa: E501
        """PatchRequestProperties - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._logs = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if logs is not None:
            self.logs = logs


    @property
    def name(self):
        """Gets the name of this PatchRequestProperties.  # noqa: E501

        The friendly name of your pipeline.  # noqa: E501

        :return: The name of this PatchRequestProperties.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PatchRequestProperties.

        The friendly name of your pipeline.  # noqa: E501

        :param name: The name of this PatchRequestProperties.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def logs(self):
        """Gets the logs of this PatchRequestProperties.  # noqa: E501

        The information of the log pipelines  # noqa: E501

        :return: The logs of this PatchRequestProperties.  # noqa: E501
        :rtype: list[PatchRequestPipeline]
        """
        return self._logs

    @logs.setter
    def logs(self, logs):
        """Sets the logs of this PatchRequestProperties.

        The information of the log pipelines  # noqa: E501

        :param logs: The logs of this PatchRequestProperties.  # noqa: E501
        :type logs: list[PatchRequestPipeline]
        """
        if (self.local_vars_configuration.client_side_validation and
                logs is not None and len(logs) > 3):
            raise ValueError("Invalid value for `logs`, number of items must be less than or equal to `3`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                logs is not None and len(logs) < 1):
            raise ValueError("Invalid value for `logs`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._logs = logs
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
        if not isinstance(other, PatchRequestProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchRequestProperties):
            return True

        return self.to_dict() != other.to_dict()
