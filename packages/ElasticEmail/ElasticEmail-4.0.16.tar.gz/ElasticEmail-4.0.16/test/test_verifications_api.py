"""
    Elastic Email REST API

    This API is based on the REST API architecture, allowing the user to easily manage their data with this resource-based approach.    Every API call is established on which specific request type (GET, POST, PUT, DELETE) will be used.    To start using this API, you will need your Access Token (available <a href=\"https://elasticemail.com/account#/settings/new/manage-api\">here</a>). Remember to keep it safe. Required access levels are listed in the given request’s description.    This is the documentation for REST API. If you’d like to read our legacy documentation regarding Web API v2 click <a href=\"https://api.elasticemail.com/public/help\">here</a>.  # noqa: E501

    The version of the OpenAPI document: 4.0.0
    Contact: support@elasticemail.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import ElasticEmail
from ElasticEmail.api.verifications_api import VerificationsApi  # noqa: E501


class TestVerificationsApi(unittest.TestCase):
    """VerificationsApi unit test stubs"""

    def setUp(self):
        self.api = VerificationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_verifications_by_email_delete(self):
        """Test case for verifications_by_email_delete

        Delete Email Verification Result  # noqa: E501
        """
        pass

    def test_verifications_by_email_get(self):
        """Test case for verifications_by_email_get

        Get Email Verification Result  # noqa: E501
        """
        pass

    def test_verifications_by_email_post(self):
        """Test case for verifications_by_email_post

        Verify Email  # noqa: E501
        """
        pass

    def test_verifications_files_by_id_delete(self):
        """Test case for verifications_files_by_id_delete

        Delete File Verification Result  # noqa: E501
        """
        pass

    def test_verifications_files_by_id_result_download_get(self):
        """Test case for verifications_files_by_id_result_download_get

        Download File Verification Result  # noqa: E501
        """
        pass

    def test_verifications_files_by_id_result_get(self):
        """Test case for verifications_files_by_id_result_get

        Get Detailed File Verification Result  # noqa: E501
        """
        pass

    def test_verifications_files_post(self):
        """Test case for verifications_files_post

        Verify From File  # noqa: E501
        """
        pass

    def test_verifications_files_result_get(self):
        """Test case for verifications_files_result_get

        Get Simple Files Verification Results  # noqa: E501
        """
        pass

    def test_verifications_get(self):
        """Test case for verifications_get

        Get Emails Verification Results  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
