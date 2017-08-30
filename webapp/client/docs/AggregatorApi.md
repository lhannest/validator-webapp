# swagger_client.AggregatorApi

All URIs are relative to *http://kba.ncats.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_beacons**](AggregatorApi.md#get_beacons) | **GET** /beacons | 
[**get_errors**](AggregatorApi.md#get_errors) | **GET** /errorlog | 


# **get_beacons**
> list[KnowledgeBeacon] get_beacons(session_id=session_id)



Get a list of the knowledge beacons that the aggregator can query 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AggregatorApi()
session_id = 'session_id_example' # str | identifier to be used for tagging session data  (optional)

try: 
    api_response = api_instance.get_beacons(session_id=session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatorApi->get_beacons: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| identifier to be used for tagging session data  | [optional] 

### Return type

[**list[KnowledgeBeacon]**](KnowledgeBeacon.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_errors**
> list[LogEntry] get_errors(session_id)



Get a log of the most recent errors in this session 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AggregatorApi()
session_id = 'session_id_example' # str | session identifier 

try: 
    api_response = api_instance.get_errors(session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatorApi->get_errors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| session identifier  | 

### Return type

[**list[LogEntry]**](LogEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

