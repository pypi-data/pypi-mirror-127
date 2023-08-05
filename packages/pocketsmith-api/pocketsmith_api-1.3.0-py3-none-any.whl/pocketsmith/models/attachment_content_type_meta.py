# coding: utf-8

"""
    PocketSmith

    The public PocketSmith API  # noqa: E501

    The version of the OpenAPI document: 2.0
    Contact: api@pocketsmith.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pocketsmith.configuration import Configuration


class AttachmentContentTypeMeta(object):
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
        'description': 'str',
        'extension': 'str',
        'title': 'str'
    }

    attribute_map = {
        'description': 'description',
        'extension': 'extension',
        'title': 'title'
    }

    def __init__(self, description=None, extension=None, title=None, local_vars_configuration=None):  # noqa: E501
        """AttachmentContentTypeMeta - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._extension = None
        self._title = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if extension is not None:
            self.extension = extension
        if title is not None:
            self.title = title

    @property
    def description(self):
        """Gets the description of this AttachmentContentTypeMeta.  # noqa: E501

        The content type description of the attachment  # noqa: E501

        :return: The description of this AttachmentContentTypeMeta.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AttachmentContentTypeMeta.

        The content type description of the attachment  # noqa: E501

        :param description: The description of this AttachmentContentTypeMeta.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def extension(self):
        """Gets the extension of this AttachmentContentTypeMeta.  # noqa: E501

        The extension type of the attachment  # noqa: E501

        :return: The extension of this AttachmentContentTypeMeta.  # noqa: E501
        :rtype: str
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        """Sets the extension of this AttachmentContentTypeMeta.

        The extension type of the attachment  # noqa: E501

        :param extension: The extension of this AttachmentContentTypeMeta.  # noqa: E501
        :type: str
        """

        self._extension = extension

    @property
    def title(self):
        """Gets the title of this AttachmentContentTypeMeta.  # noqa: E501

        The content type title of the attachment  # noqa: E501

        :return: The title of this AttachmentContentTypeMeta.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this AttachmentContentTypeMeta.

        The content type title of the attachment  # noqa: E501

        :param title: The title of this AttachmentContentTypeMeta.  # noqa: E501
        :type: str
        """

        self._title = title

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
        if not isinstance(other, AttachmentContentTypeMeta):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AttachmentContentTypeMeta):
            return True

        return self.to_dict() != other.to_dict()
