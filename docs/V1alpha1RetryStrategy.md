# V1alpha1RetryStrategy

RetryStrategy provides controls on how to retry a workflow step
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affinity** | [**V1alpha1RetryAffinity**](V1alpha1RetryAffinity.md) |  | [optional] 
**backoff** | [**V1alpha1Backoff**](V1alpha1Backoff.md) |  | [optional] 
**limit** | **str** | Limit is the maximum number of attempts when retrying a container | [optional] 
**retry_policy** | **str** | RetryPolicy is a policy of NodePhase statuses that will be retried | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


