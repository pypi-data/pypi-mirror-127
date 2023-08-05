"""
    Elastic Email REST API

    This API is based on the REST API architecture, allowing the user to easily manage their data with this resource-based approach.    Every API call is established on which specific request type (GET, POST, PUT, DELETE) will be used.    To start using this API, you will need your Access Token (available <a href=\"https://elasticemail.com/account#/settings/new/manage-api\">here</a>). Remember to keep it safe. Required access levels are listed in the given request’s description.    This is the documentation for REST API. If you’d like to read our legacy documentation regarding Web API v2 click <a href=\"https://api.elasticemail.com/public/help\">here</a>.  # noqa: E501

    The version of the OpenAPI document: 4.0.0
    Contact: support@elasticemail.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ElasticEmail
from ElasticEmail.model.body_part import BodyPart
globals()['BodyPart'] = BodyPart
from ElasticEmail.model.template_payload import TemplatePayload


class TestTemplatePayload(unittest.TestCase):
    """TemplatePayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTemplatePayload(self):
        """Test TemplatePayload"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TemplatePayload()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
