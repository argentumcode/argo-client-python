# IoArgoprojEventsV1alpha1WebhookContext

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_secret** | [**V1SecretKeySelector**](V1SecretKeySelector.md) |  | [optional] 
**endpoint** | **str** |  | [optional] 
**metadata** | **dict(str, str)** |  | [optional] 
**method** | **str** |  | [optional] 
**port** | **str** | Port on which HTTP server is listening for incoming events. | [optional] 
**server_cert_path** | **str** | DeprecatedServerCertPath refers the file that contains the cert. | [optional] 
**server_cert_secret** | [**V1SecretKeySelector**](V1SecretKeySelector.md) |  | [optional] 
**server_key_path** | **str** |  | [optional] 
**server_key_secret** | [**V1SecretKeySelector**](V1SecretKeySelector.md) |  | [optional] 
**url** | **str** | URL is the url of the server. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


