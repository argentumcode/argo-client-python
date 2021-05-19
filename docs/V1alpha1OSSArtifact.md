# V1alpha1OSSArtifact

OSSArtifact is the location of an Alibaba Cloud OSS artifact
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key_secret** | [**V1SecretKeySelector**](V1SecretKeySelector.md) |  | [optional] 
**bucket** | **str** | Bucket is the name of the bucket | [optional] 
**create_bucket_if_not_present** | **bool** | CreateBucketIfNotPresent tells the driver to attempt to create the OSS bucket for output artifacts, if it doesn&#39;t exist | [optional] 
**endpoint** | **str** | Endpoint is the hostname of the bucket endpoint | [optional] 
**key** | **str** | Key is the path in the bucket where the artifact resides | 
**secret_key_secret** | [**V1SecretKeySelector**](V1SecretKeySelector.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


