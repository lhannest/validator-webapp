# swagger_client.SummaryApi

All URIs are relative to *http://kba.ncats.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**linked_types**](SummaryApi.md#linked_types) | **GET** /types | 


# **linked_types**
> list[Summary] linked_types(session_id=session_id)



Get a list of types and # of instances in the knowledge source, and a link to the API call for the list of equivalent terminology 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SummaryApi()
session_id = 'session_id_example' # str | identifier to be used for tagging session data  (optional)

try: 
    api_response = api_instance.linked_types(session_id=session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SummaryApi->linked_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| identifier to be used for tagging session data  | [optional] 

### Return type

[**list[Summary]**](Summary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

