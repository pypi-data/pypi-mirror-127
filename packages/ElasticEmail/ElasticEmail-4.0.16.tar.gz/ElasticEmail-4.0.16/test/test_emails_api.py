"""
    Elastic Email REST API

    This API is based on the REST API architecture, allowing the user to easily manage their data with this resource-based approach.    Every API call is established on which specific request type (GET, POST, PUT, DELETE) will be used.    To start using this API, you will need your Access Token (available <a href=\"https://elasticemail.com/account#/settings/new/manage-api\">here</a>). Remember to keep it safe. Required access levels are listed in the given request’s description.    This is the documentation for REST API. If you’d like to read our legacy documentation regarding Web API v2 click <a href=\"https://api.elasticemail.com/public/help\">here</a>.  # noqa: E501

    The version of the OpenAPI document: 4.0.0
    Contact: support@elasticemail.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import ElasticEmail
from ElasticEmail.api.emails_api import EmailsApi  # noqa: E501


class TestEmailsApi(unittest.TestCase):
    """EmailsApi unit test stubs"""

    def setUp(self):
        self.api = EmailsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_emails_by_msgid_view_get(self):
        """Test case for emails_by_msgid_view_get

        View Email  # noqa: E501
        """
        pass

    def test_emails_mergefile_post(self):
        """Test case for emails_mergefile_post

        Send Bulk Emails CSV  # noqa: E501
        """
        pass

    def test_emails_post(self):
        """Test case for emails_post

        Send Bulk Emails  # noqa: E501
        """
        pass

    def test_emails_transactional_post(self):
        """Test case for emails_transactional_post

        Send Transactional Email  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
