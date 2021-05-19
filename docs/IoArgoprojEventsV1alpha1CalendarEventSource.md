# IoArgoprojEventsV1alpha1CalendarEventSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclusion_dates** | **list[str]** |  | [optional] 
**interval** | **str** | Interval is a string that describes an interval duration, e.g. 1s, 30m, 2h... | [optional] 
**metadata** | **dict(str, str)** |  | [optional] 
**persistence** | [**IoArgoprojEventsV1alpha1EventPersistence**](IoArgoprojEventsV1alpha1EventPersistence.md) |  | [optional] 
**schedule** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 
**user_payload** | **str** | UserPayload will be sent to sensor as extra data once the event is triggered +optional Deprecated. Please use Metadata instead. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


