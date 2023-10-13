# PatchRequestPipeline

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **source** | **str** | The source parser to be used | [optional]  |
| **tag** | **str** | Tag is to distinguish different pipelines. must be unique amongst the pipeline&#39;s array items. | [optional]  |
| **protocol** | **str** | Protocol to use as intake | [optional]  |
| **labels** | **list[str]** | Optional custom labels to filter and report logs | [optional]  |
| **destinations** | [**list[Destination]**](Destination.md) | The configuration of the logs datastore | [optional]  |


