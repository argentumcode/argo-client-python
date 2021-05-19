# IoArgoprojEventsV1alpha1TriggerTemplate

TriggerTemplate is the template that describes trigger specification.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**argo_workflow** | [**IoArgoprojEventsV1alpha1ArgoWorkflowTrigger**](IoArgoprojEventsV1alpha1ArgoWorkflowTrigger.md) |  | [optional] 
**aws_lambda** | [**IoArgoprojEventsV1alpha1AWSLambdaTrigger**](IoArgoprojEventsV1alpha1AWSLambdaTrigger.md) |  | [optional] 
**conditions** | **str** |  | [optional] 
**custom** | [**IoArgoprojEventsV1alpha1CustomTrigger**](IoArgoprojEventsV1alpha1CustomTrigger.md) |  | [optional] 
**http** | [**IoArgoprojEventsV1alpha1HTTPTrigger**](IoArgoprojEventsV1alpha1HTTPTrigger.md) |  | [optional] 
**k8s** | [**IoArgoprojEventsV1alpha1StandardK8STrigger**](IoArgoprojEventsV1alpha1StandardK8STrigger.md) |  | [optional] 
**kafka** | [**IoArgoprojEventsV1alpha1KafkaTrigger**](IoArgoprojEventsV1alpha1KafkaTrigger.md) |  | [optional] 
**log** | [**IoArgoprojEventsV1alpha1LogTrigger**](IoArgoprojEventsV1alpha1LogTrigger.md) |  | [optional] 
**name** | **str** | Name is a unique name of the action to take. | [optional] 
**nats** | [**IoArgoprojEventsV1alpha1NATSTrigger**](IoArgoprojEventsV1alpha1NATSTrigger.md) |  | [optional] 
**open_whisk** | [**IoArgoprojEventsV1alpha1OpenWhiskTrigger**](IoArgoprojEventsV1alpha1OpenWhiskTrigger.md) |  | [optional] 
**slack** | [**IoArgoprojEventsV1alpha1SlackTrigger**](IoArgoprojEventsV1alpha1SlackTrigger.md) |  | [optional] 
**switch** | [**IoArgoprojEventsV1alpha1TriggerSwitch**](IoArgoprojEventsV1alpha1TriggerSwitch.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


