# coding: utf-8

"""
    Translator Knowledge Beacon API

    This is the Translator Knowledge Beacon Aggregator web service application programming interface (API). 

    OpenAPI spec version: 1.0.12
    Contact: richard@starinformatics.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import sys
from setuptools import setup, find_packages

NAME = "swagger_client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Translator Knowledge Beacon API",
    author_email="richard@starinformatics.com",
    url="",
    keywords=["Swagger", "Translator Knowledge Beacon API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    This is the Translator Knowledge Beacon Aggregator web service application programming interface (API). 
    """
)
