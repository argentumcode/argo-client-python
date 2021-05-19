# IoArgoprojEventsV1alpha1CustomTrigger

CustomTrigger refers to the specification of the custom trigger.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert_file_path** | **str** |  | [optional] 
**cert_secret** | [**V1SecretKeySelector**](V1SecretKeySelector.md) |  | [optional] 
**parameters** | [**list[IoArgoprojEventsV1alpha1TriggerParameter]**](IoArgoprojEventsV1alpha1TriggerParameter.md) |  | [optional] 
**payload** | [**list[IoArgoprojEventsV1alpha1TriggerParameter]**](IoArgoprojEventsV1alpha1TriggerParameter.md) |  | [optional] 
**secure** | **bool** |  | [optional] 
**server_name_override** | **str** | ServerNameOverride for the secure connection between sensor and custom trigger gRPC server. | [optional] 
**server_url** | **str** |  | [optional] 
**spec** | **dict(str, str)** | Spec is the custom trigger resource specification that custom trigger gRPC server knows how to interpret. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


