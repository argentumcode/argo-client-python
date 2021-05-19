# IoArgoprojEventsV1alpha1KafkaTrigger

KafkaTrigger refers to the specification of the Kafka trigger.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compress** | **bool** |  | [optional] 
**flush_frequency** | **int** |  | [optional] 
**parameters** | [**list[IoArgoprojEventsV1alpha1TriggerParameter]**](IoArgoprojEventsV1alpha1TriggerParameter.md) |  | [optional] 
**partition** | **int** | Partition to write data to. | [optional] 
**partitioning_key** | **str** | The partitioning key for the messages put on the Kafka topic. Defaults to broker url. +optional. | [optional] 
**payload** | [**list[IoArgoprojEventsV1alpha1TriggerParameter]**](IoArgoprojEventsV1alpha1TriggerParameter.md) |  | [optional] 
**required_acks** | **int** | RequiredAcks used in producer to tell the broker how many replica acknowledgements Defaults to 1 (Only wait for the leader to ack). +optional. | [optional] 
**tls** | [**IoArgoprojEventsV1alpha1TLSConfig**](IoArgoprojEventsV1alpha1TLSConfig.md) |  | [optional] 
**topic** | **str** |  | [optional] 
**url** | **str** | URL of the Kafka broker. | [optional] 
**version** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


