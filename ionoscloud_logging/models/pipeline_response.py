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


class PipelineResponse(object):
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

        'public': 'bool',

        'source': 'str',

        'tag': 'str',

        'protocol': 'str',

        'labels': 'list[str]',

        'destinations': 'list[Destination]',
    }

    attribute_map = {

        'public': 'public',

        'source': 'source',

        'tag': 'tag',

        'protocol': 'protocol',

        'labels': 'labels',

        'destinations': 'destinations',
    }

    def __init__(self, public=None, source=None, tag=None, protocol=None, labels=None, destinations=None, local_vars_configuration=None):  # noqa: E501
        """PipelineResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._public = None
        self._source = None
        self._tag = None
        self._protocol = None
        self._labels = None
        self._destinations = None
        self.discriminator = None

        if public is not None:
            self.public = public
        if source is not None:
            self.source = source
        if tag is not None:
            self.tag = tag
        if protocol is not None:
            self.protocol = protocol
        if labels is not None:
            self.labels = labels
        if destinations is not None:
            self.destinations = destinations


    @property
    def public(self):
        """Gets the public of this PipelineResponse.  # noqa: E501


        :return: The public of this PipelineResponse.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this PipelineResponse.


        :param public: The public of this PipelineResponse.  # noqa: E501
        :type public: bool
        """

        self._public = public

    @property
    def source(self):
        """Gets the source of this PipelineResponse.  # noqa: E501

        The source parser to be used  # noqa: E501

        :return: The source of this PipelineResponse.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this PipelineResponse.

        The source parser to be used  # noqa: E501

        :param source: The source of this PipelineResponse.  # noqa: E501
        :type source: str
        """

        self._source = source

    @property
    def tag(self):
        """Gets the tag of this PipelineResponse.  # noqa: E501

        Tag is to distinguish different pipelines. must be unique amongst the pipeline's array items.  # noqa: E501

        :return: The tag of this PipelineResponse.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this PipelineResponse.

        Tag is to distinguish different pipelines. must be unique amongst the pipeline's array items.  # noqa: E501

        :param tag: The tag of this PipelineResponse.  # noqa: E501
        :type tag: str
        """

        self._tag = tag

    @property
    def protocol(self):
        """Gets the protocol of this PipelineResponse.  # noqa: E501

        Protocol to use as intake  # noqa: E501

        :return: The protocol of this PipelineResponse.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this PipelineResponse.

        Protocol to use as intake  # noqa: E501

        :param protocol: The protocol of this PipelineResponse.  # noqa: E501
        :type protocol: str
        """

        self._protocol = protocol

    @property
    def labels(self):
        """Gets the labels of this PipelineResponse.  # noqa: E501

        Optional custom labels to filter and report logs  # noqa: E501

        :return: The labels of this PipelineResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this PipelineResponse.

        Optional custom labels to filter and report logs  # noqa: E501

        :param labels: The labels of this PipelineResponse.  # noqa: E501
        :type labels: list[str]
        """
        if (self.local_vars_configuration.client_side_validation and
                labels is not None and len(labels) > 3):
            raise ValueError("Invalid value for `labels`, number of items must be less than or equal to `3`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                labels is not None and len(labels) < 0):
            raise ValueError("Invalid value for `labels`, number of items must be greater than or equal to `0`")  # noqa: E501

        self._labels = labels

    @property
    def destinations(self):
        """Gets the destinations of this PipelineResponse.  # noqa: E501


        :return: The destinations of this PipelineResponse.  # noqa: E501
        :rtype: list[Destination]
        """
        return self._destinations

    @destinations.setter
    def destinations(self, destinations):
        """Sets the destinations of this PipelineResponse.


        :param destinations: The destinations of this PipelineResponse.  # noqa: E501
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
        if not isinstance(other, PipelineResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PipelineResponse):
            return True

        return self.to_dict() != other.to_dict()
