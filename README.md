[![Gitter](https://img.shields.io/gitter/room/ionos-cloud/sdk-general)](https://gitter.im/ionos-cloud/sdk-general)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=sdk-python-logging&metric=alert_status)](https://sonarcloud.io/summary?id=sdk-python-logging)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=sdk-python-logging&metric=bugs)](https://sonarcloud.io/summary/new_code?id=sdk-python-logging)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=sdk-python-logging&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=sdk-python-logging)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=sdk-python-logging&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=sdk-python-logging)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=sdk-python-logging&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=sdk-python-logging)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=sdk-python-logging&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=sdk-python-logging)
[![Release](https://img.shields.io/github/v/release/ionos-cloud/sdk-python-logging.svg)](https://github.com/ionos-cloud/sdk-python-logging/releases/latest)
[![Release Date](https://img.shields.io/github/release-date/ionos-cloud/sdk-python-logging.svg)](https://github.com/ionos-cloud/sdk-python-logging/releases/latest)
[![PyPI version](https://img.shields.io/pypi/v/ionoscloud-logging)](https://pypi.org/project/ionoscloud-logging/)

![Alt text](.github/IONOS.CLOUD.BLU.svg?raw=true "Title")


# Python API client for ionoscloud_logging

Logging as a Service (LaaS) is a service that provides a centralized logging system where users are able to push and aggregate their system or application logs. This service also provides a visualization platform where users are able to observe, search and filter the logs and also create dashboards and alerts for their data points.
This service can be managed through a browser-based \"Data Center Designer\" (DCD) tool or via an API.
The API allows you to create logging pipelines or modify existing ones. It is designed to allow users to leverage the same power and flexibility found within the DCD visual tool. Both tools are consistent with their concepts and lend well to making the experience smooth and intuitive.

## Overview
The IONOS Cloud SDK for Python provides you with access to the IONOS Cloud API. The client library supports both simple and complex requests. It is designed for developers who are building applications in Python. All API operations are performed over SSL and authenticated using your IONOS Cloud portal credentials. The API can be accessed within an instance running in IONOS Cloud or directly over the Internet from any application that can send an HTTPS request and receive an HTTPS response.


### Installation & Usage

**Requirements:**
- Python >= 3.5

### pip install

Since this package is hosted on [Pypi](https://pypi.org/) you can install it by using:

```bash
pip install ionoscloud-logging
```

If the python package is hosted on a repository, you can install directly using:

```bash
pip install git+https://github.com/ionos-cloud/sdk-python-logging.git
```

Note: you may need to run `pip` with root permission: `sudo pip install git+https://github.com/ionos-cloud/sdk-python-logging.git`

Then import the package:

```python
import ionoscloud_logging
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```bash
python setup.py install --user
```

or `sudo python setup.py install` to install the package for all users

Then import the package:

```python
import ionoscloud_logging
```

> **_NOTE:_**  The Python SDK does not support Python 2. It only supports Python >= 3.5.

### Authentication

The username and password **or** the authentication token can be manually specified when initializing the SDK client:

```python
configuration = ionoscloud_logging.Configuration(
                username='YOUR_USERNAME',
                password='YOUR_PASSWORD',
                token='YOUR_TOKEN'
                )
client = ionoscloud_logging.ApiClient(configuration)
```

Environment variables can also be used. This is an example of how one would do that:

```python
import os

configuration = ionoscloud_logging.Configuration(
                username=os.environ.get('IONOS_USERNAME'),
                password=os.environ.get('IONOS_PASSWORD'),
                token=os.environ.get('IONOS_TOKEN')
                )
client = ionoscloud_logging.ApiClient(configuration)
```

**Warning**: Make sure to follow the Information Security Best Practices when using credentials within your code or storing them in a file.


### HTTP proxies

You can use http proxies by setting the following environment variables:
- `IONOS_HTTP_PROXY` - proxy URL
- `IONOS_HTTP_PROXY_HEADERS` - proxy headers

Each line in `IONOS_HTTP_PROXY_HEADERS` represents one header, where the header name and value is separated by a colon. Newline characters within a value need to be escaped. See this example:
```
Connection: Keep-Alive
User-Info: MyID
User-Group: my long\nheader value
```


### Changing the base URL

Base URL for the HTTP operation can be changed in the following way:

```python
import os

configuration = ionoscloud_logging.Configuration(
                username=os.environ.get('IONOS_USERNAME'),
                password=os.environ.get('IONOS_PASSWORD'),
                host=os.environ.get('IONOS_API_URL'),
                server_index=None,
                )
client = ionoscloud_logging.ApiClient(configuration)
```

## Certificate pinning:

You can enable certificate pinning if you want to bypass the normal certificate checking procedure,
by doing the following:

Set env variable IONOS_PINNED_CERT=<insert_sha256_public_fingerprint_here>

You can get the sha256 fingerprint most easily from the browser by inspecting the certificate.


## Documentation for API Endpoints

All URIs are relative to *https://logging.de-txl.ionos.com*
<details >
    <summary title="Click to toggle">API Endpoints table</summary>


| Class | Method | HTTP request | Description |
| ------------- | ------------- | ------------- | ------------- |
| PipelinesApi | [**pipelines_delete**](docs/api/PipelinesApi.md#pipelines_delete) | **DELETE** /pipelines/{pipelineId} | Delete a pipeline |
| PipelinesApi | [**pipelines_find_by_id**](docs/api/PipelinesApi.md#pipelines_find_by_id) | **GET** /pipelines/{pipelineId} | Fetch a pipeline |
| PipelinesApi | [**pipelines_get**](docs/api/PipelinesApi.md#pipelines_get) | **GET** /pipelines | List pipelines |
| PipelinesApi | [**pipelines_key_post**](docs/api/PipelinesApi.md#pipelines_key_post) | **POST** /pipelines/{pipelineId}/key | Renews the key of a Pipeline |
| PipelinesApi | [**pipelines_patch**](docs/api/PipelinesApi.md#pipelines_patch) | **PATCH** /pipelines/{pipelineId} | Patch a pipeline |
| PipelinesApi | [**pipelines_post**](docs/api/PipelinesApi.md#pipelines_post) | **POST** /pipelines | Create a pipeline |

</details>

## Documentation For Models

All URIs are relative to *https://logging.de-txl.ionos.com*
<details >
<summary title="Click to toggle">API models list</summary>

 - [Destination](docs/models/Destination)
 - [ErrorMessage](docs/models/ErrorMessage)
 - [ErrorResponse](docs/models/ErrorResponse)
 - [Metadata](docs/models/Metadata)
 - [Pipeline](docs/models/Pipeline)
 - [PipelineCreate](docs/models/PipelineCreate)
 - [PipelineCreateProperties](docs/models/PipelineCreateProperties)
 - [PipelineCreatePropertiesLogs](docs/models/PipelineCreatePropertiesLogs)
 - [PipelineListResponse](docs/models/PipelineListResponse)
 - [PipelinePatch](docs/models/PipelinePatch)
 - [PipelinePatchProperties](docs/models/PipelinePatchProperties)
 - [PipelineProperties](docs/models/PipelineProperties)
 - [PipelineResponse](docs/models/PipelineResponse)
 - [PipelineResponseAllOf](docs/models/PipelineResponseAllOf)
 - [PipelineResponseAllOf1](docs/models/PipelineResponseAllOf1)
 - [PipelinesKeyPost200Response](docs/models/PipelinesKeyPost200Response)
 - [Processor](docs/models/Processor)


[[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

</details>