# PipelineProperties

A pipeline properties
## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **name** | **str** | The friendly name of your pipeline. | [optional]  |
| **logs** | [**list[PipelineResponse]**](PipelineResponse.md) | The information of the log aggregator | [optional]  |
| **tcp_address** | **str** | The address to connect fluentBit compatible logging agents to | [optional]  |
| **http_address** | **str** | The address to post logs to using JSON with basic auth | [optional]  |
| **grafana_address** | **str** | The address of the client&#39;s grafana instance | [optional]  |


