# coding: utf-8

"""
    Translator Knowledge Beacon API

    This is the Translator Knowledge Beacon Aggregator web service application programming interface (API). 

    OpenAPI spec version: 1.0.12
    Contact: richard@starinformatics.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.models.concept import Concept


class TestConcept(unittest.TestCase):
    """ Concept unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testConcept(self):
        """
        Test Concept
        """
        model = swagger_client.models.concept.Concept()


if __name__ == '__main__':
    unittest.main()
