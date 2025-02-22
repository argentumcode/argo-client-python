# IoArgoprojEventsV1alpha1HDFSEventSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **list[str]** |  | [optional] 
**check_interval** | **str** |  | [optional] 
**hdfs_user** | **str** | HDFSUser is the user to access HDFS file system. It is ignored if either ccache or keytab is used. | [optional] 
**krb_c_cache_secret** | [**V1SecretKeySelector**](V1SecretKeySelector.md) |  | [optional] 
**krb_config_config_map** | [**V1ConfigMapKeySelector**](V1ConfigMapKeySelector.md) |  | [optional] 
**krb_keytab_secret** | [**V1SecretKeySelector**](V1SecretKeySelector.md) |  | [optional] 
**krb_realm** | **str** | KrbRealm is the Kerberos realm used with Kerberos keytab It must be set if keytab is used. | [optional] 
**krb_service_principal_name** | **str** | KrbServicePrincipalName is the principal name of Kerberos service It must be set if either ccache or keytab is used. | [optional] 
**krb_username** | **str** | KrbUsername is the Kerberos username used with Kerberos keytab It must be set if keytab is used. | [optional] 
**metadata** | **dict(str, str)** |  | [optional] 
**type** | **str** |  | [optional] 
**watch_path_config** | [**IoArgoprojEventsV1alpha1WatchPathConfig**](IoArgoprojEventsV1alpha1WatchPathConfig.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


