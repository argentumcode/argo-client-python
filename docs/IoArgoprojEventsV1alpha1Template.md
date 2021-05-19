# IoArgoprojEventsV1alpha1Template

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container** | [**V1Container**](V1Container.md) |  | [optional] 
**image_pull_secrets** | [**list[V1LocalObjectReference]**](V1LocalObjectReference.md) |  | [optional] 
**metadata** | [**IoArgoprojEventsV1alpha1Metadata**](IoArgoprojEventsV1alpha1Metadata.md) |  | [optional] 
**node_selector** | **dict(str, str)** |  | [optional] 
**security_context** | [**V1PodSecurityContext**](V1PodSecurityContext.md) |  | [optional] 
**service_account_name** | **str** |  | [optional] 
**tolerations** | [**list[V1Toleration]**](V1Toleration.md) |  | [optional] 
**volumes** | [**list[V1Volume]**](V1Volume.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


