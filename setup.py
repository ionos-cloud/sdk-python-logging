# coding: utf-8

"""
    IONOS Logging REST API

    Logging as a Service (LaaS) is a service that provides a centralized logging system where users are able to push and aggregate their system or application logs. This service also provides a visualization platform where users are able to observe, search and filter the logs and also create dashboards and alerts for their data points. This service can be managed through a browser-based \"Data Center Designer\" (DCD) tool or via an API. The API allows you to create logging pipelines or modify existing ones. It is designed to allow users to leverage the same power and flexibility found within the DCD visual tool. Both tools are consistent with their concepts and lend well to making the experience smooth and intuitive.  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup  # noqa: H301
import os
import codecs

NAME = "ionoscloud-logging"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

with open('requirements.txt') as f:
    REQUIRES = f.read().splitlines()

here = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    return codecs.open(os.path.join(here, *parts), 'r', 'utf-8').read()

if os.path.isfile("README.md"):
    long_desc = read('README.md')
else:
    long_desc = "Ionos Cloud API Client Library for Python"

setup(
    name=NAME,
    version=VERSION,
    description="Python SDK for the ionoscloud-logging API",
    author='Ionos Cloud',
    author_email='sdk@cloud.ionos.com',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    url="https://github.com/ionos-cloud/sdk-python-logging",
    keywords=["OpenAPI", "OpenAPI-Generator", "IONOS Logging REST API"],
    install_requires=REQUIRES,
    packages=['ionoscloud_logging', 'ionoscloud_logging.api', 'ionoscloud_logging.models'],
    include_package_data=True,
    classifiers=[
         'Natural Language :: English',
         'Environment :: Web Environment',
         'Intended Audience :: Developers',
         'License :: OSI Approved :: Apache Software License',
         'Operating System :: POSIX',
         'Programming Language :: Python',
         'Programming Language :: Python :: 3',
         'Topic :: Software Development :: Libraries :: Python Modules',
         'Topic :: Software Development :: Libraries :: Application Frameworks',
         'Topic :: Internet :: WWW/HTTP']
)