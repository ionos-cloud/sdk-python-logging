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


class ResponsePipelineAllOf1(object):
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

        'destinations': 'list[Destination]',
    }

    attribute_map = {

        'destinations': 'destinations',
    }

    def __init__(self, destinations=None, local_vars_configuration=None):  # noqa: E501
        """ResponsePipelineAllOf1 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._destinations = None
        self.discriminator = None

        if destinations is not None:
            self.destinations = destinations


    @property
    def destinations(self):
        """Gets the destinations of this ResponsePipelineAllOf1.  # noqa: E501


        :return: The destinations of this ResponsePipelineAllOf1.  # noqa: E501
        :rtype: list[Destination]
        """
        return self._destinations

    @destinations.setter
    def destinations(self, destinations):
        """Sets the destinations of this ResponsePipelineAllOf1.


        :param destinations: The destinations of this ResponsePipelineAllOf1.  # noqa: E501
        :type destinations: list[Destination]
        """
        if (self.local_vars_configuration.client_side_validation and
                destinations is not None and len(destinations) > 1):
            raise ValueError("Invalid value for `destinations`, number of items must be less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                destinations is not None and len(destinations) < 0):
            raise ValueError("Invalid value for `destinations`, number of items must be greater than or equal to `0`")  # noqa: E501

        self._destinations = destinations
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
        if not isinstance(other, ResponsePipelineAllOf1):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponsePipelineAllOf1):
            return True

        return self.to_dict() != other.to_dict()
