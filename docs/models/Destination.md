# Destination

The information of the logging aggregator storage
## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **type** | **str** | The internal output stream to send logs to | [optional] [default to 'loki'] |
| **retention_in_days** | **int** | defines the number of days a log record should be kept in loki. Works with loki destination type only. | [optional] [default to 30] |


