# IoArgoprojEventsV1alpha1OpenWhiskTrigger

OpenWhiskTrigger refers to the specification of the OpenWhisk trigger.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_name** | **str** | Name of the action/function. | [optional] 
**auth_token** | [**V1SecretKeySelector**](V1SecretKeySelector.md) |  | [optional] 
**host** | **str** | Host URL of the OpenWhisk. | [optional] 
**namespace** | **str** | Namespace for the action. Defaults to \&quot;_\&quot;. +optional. | [optional] 
**parameters** | [**list[IoArgoprojEventsV1alpha1TriggerParameter]**](IoArgoprojEventsV1alpha1TriggerParameter.md) |  | [optional] 
**payload** | [**list[IoArgoprojEventsV1alpha1TriggerParameter]**](IoArgoprojEventsV1alpha1TriggerParameter.md) |  | [optional] 
**version** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


