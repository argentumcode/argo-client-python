# V1alpha1ArtifactRepositoryRefStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_map** | **str** | The name of the config map. Defaults to \&quot;artifact-repositories\&quot;. | [optional] 
**default** | **bool** | If this ref represents the default artifact repository, rather than a config map. | [optional] 
**key** | **str** | The config map key. Defaults to the value of the \&quot;workflows.argoproj.io/default-artifact-repository\&quot; annotation. | [optional] 
**namespace** | **str** | The namespace of the config map. Defaults to the workflow&#39;s namespace, or the controller&#39;s namespace (if found). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


