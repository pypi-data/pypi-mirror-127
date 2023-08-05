# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAntitamperRuleRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'policy_id': 'str',
        'page': 'int',
        'pagesize': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'policy_id': 'policy_id',
        'page': 'page',
        'pagesize': 'pagesize'
    }

    def __init__(self, enterprise_project_id=None, policy_id=None, page=None, pagesize=None):
        """ListAntitamperRuleRequest - a model defined in huaweicloud sdk"""
        
        

        self._enterprise_project_id = None
        self._policy_id = None
        self._page = None
        self._pagesize = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.policy_id = policy_id
        if page is not None:
            self.page = page
        if pagesize is not None:
            self.pagesize = pagesize

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListAntitamperRuleRequest.

        企业项目id

        :return: The enterprise_project_id of this ListAntitamperRuleRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListAntitamperRuleRequest.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this ListAntitamperRuleRequest.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def policy_id(self):
        """Gets the policy_id of this ListAntitamperRuleRequest.

        策略id（策略id从查询防护策略列表接口获取）

        :return: The policy_id of this ListAntitamperRuleRequest.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this ListAntitamperRuleRequest.

        策略id（策略id从查询防护策略列表接口获取）

        :param policy_id: The policy_id of this ListAntitamperRuleRequest.
        :type: str
        """
        self._policy_id = policy_id

    @property
    def page(self):
        """Gets the page of this ListAntitamperRuleRequest.

        页码

        :return: The page of this ListAntitamperRuleRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListAntitamperRuleRequest.

        页码

        :param page: The page of this ListAntitamperRuleRequest.
        :type: int
        """
        self._page = page

    @property
    def pagesize(self):
        """Gets the pagesize of this ListAntitamperRuleRequest.

        单页条数

        :return: The pagesize of this ListAntitamperRuleRequest.
        :rtype: int
        """
        return self._pagesize

    @pagesize.setter
    def pagesize(self, pagesize):
        """Sets the pagesize of this ListAntitamperRuleRequest.

        单页条数

        :param pagesize: The pagesize of this ListAntitamperRuleRequest.
        :type: int
        """
        self._pagesize = pagesize

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
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListAntitamperRuleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
