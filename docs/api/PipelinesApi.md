# PipelinesApi

All URIs are relative to *https://logging.de-txl.ionos.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**pipelines_delete**](PipelinesApi.md#pipelines_delete) | **DELETE** /pipelines/{pipelineId} | Delete a pipeline |
| [**pipelines_find_by_id**](PipelinesApi.md#pipelines_find_by_id) | **GET** /pipelines/{pipelineId} | Fetch a pipeline |
| [**pipelines_get**](PipelinesApi.md#pipelines_get) | **GET** /pipelines | List pipelines |
| [**pipelines_key_post**](PipelinesApi.md#pipelines_key_post) | **POST** /pipelines/{pipelineId}/key | Renews the key of a Pipeline |
| [**pipelines_patch**](PipelinesApi.md#pipelines_patch) | **PATCH** /pipelines/{pipelineId} | Patch a pipeline |
| [**pipelines_post**](PipelinesApi.md#pipelines_post) | **POST** /pipelines | Create a pipeline |


# **pipelines_delete**
> Pipeline pipelines_delete(pipeline_id)

Delete a pipeline

Delete a logging pipeline.

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **pipeline_id** | **str**| The unique ID of the pipeline |  |

### Return type

[**Pipeline**](../models/Pipeline.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **pipelines_find_by_id**
> Pipeline pipelines_find_by_id(pipeline_id)

Fetch a pipeline

You can retrieve a pipeline by using its ID. This value can be found in the response body when a pipeline is created or when you GET a list of pipelines.

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **pipeline_id** | **str**| The unique ID of the pipeline |  |

### Return type

[**Pipeline**](../models/Pipeline.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **pipelines_get**
> PipelineListResponse pipelines_get(limit=limit, offset=offset, order_by=order_by)

List pipelines

Retrieves a list of all logging pipelines.

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **limit** | **int**| the maximum number of elements to return (use together with offset for pagination). Default to 100 | [optional] [default to 0] |
| **offset** | **int**| the first element (of the total list of elements) to include in the response (use together with limit for pagination). Default to 0 | [optional] [default to 0] |
| **order_by** | **str**| Sorts the results alphanumerically in ascending order based on the specified property | [optional]  |

### Return type

[**PipelineListResponse**](../models/PipelineListResponse.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **pipelines_key_post**
> PipelinesKeyPost200Response pipelines_key_post(pipeline_id)

Renews the key of a Pipeline

Generates a new key for a pipeline invalidating the old one. The key is used for authentication when sending logs (Shared_Key parameter in the context of fluent-bit).

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **pipeline_id** | **str**| The unique ID of the pipeline |  |

### Return type

[**PipelinesKeyPost200Response**](../models/PipelinesKeyPost200Response.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **pipelines_patch**
> Pipeline pipelines_patch(pipeline_id, pipeline)

Patch a pipeline

Patch attributes of a logging pipeline.

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **pipeline_id** | **str**| The unique ID of the pipeline |  |
| **pipeline** | [**PipelinePatch**](../models/PipelinePatch.md)| The modified pipeline. |  |

### Return type

[**Pipeline**](../models/Pipeline.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **pipelines_post**
> Pipeline pipelines_post(pipeline)

Create a pipeline

Creates a new logging pipeline.

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **pipeline** | [**PipelineCreate**](../models/PipelineCreate.md)| The pipeline to be created. |  |

### Return type

[**Pipeline**](../models/Pipeline.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

