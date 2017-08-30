# swagger_client.EvidenceApi

All URIs are relative to *http://kba.ncats.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_evidence**](EvidenceApi.md#get_evidence) | **GET** /evidence/{statementId} | 


# **get_evidence**
> list[Annotation] get_evidence(statement_id, keywords=keywords, page_number=page_number, page_size=page_size, beacons=beacons, session_id=session_id)



Retrieves a (paged) list of annotations cited as evidence for a specified concept-relationship statement 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EvidenceApi()
statement_id = 'statement_id_example' # str | (url-encoded) CURIE identifier of the concept-relationship statement (\"assertion\", \"claim\") for which associated evidence is sought 
keywords = 'keywords_example' # str | (url-encoded, space delimited) keyword filter to apply against the label field of the annotation  (optional)
page_number = 56 # int | (1-based) number of the page to be returned in a paged set of query results  (optional)
page_size = 56 # int | number of cited references per page to be returned in a paged set of query results  (optional)
beacons = ['beacons_example'] # list[str] | set of IDs of beacons to be used as knowledge sources for the query  (optional)
session_id = 'session_id_example' # str | identifier to be used for tagging session data  (optional)

try: 
    api_response = api_instance.get_evidence(statement_id, keywords=keywords, page_number=page_number, page_size=page_size, beacons=beacons, session_id=session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EvidenceApi->get_evidence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **statement_id** | **str**| (url-encoded) CURIE identifier of the concept-relationship statement (\&quot;assertion\&quot;, \&quot;claim\&quot;) for which associated evidence is sought  | 
 **keywords** | **str**| (url-encoded, space delimited) keyword filter to apply against the label field of the annotation  | [optional] 
 **page_number** | **int**| (1-based) number of the page to be returned in a paged set of query results  | [optional] 
 **page_size** | **int**| number of cited references per page to be returned in a paged set of query results  | [optional] 
 **beacons** | [**list[str]**](str.md)| set of IDs of beacons to be used as knowledge sources for the query  | [optional] 
 **session_id** | **str**| identifier to be used for tagging session data  | [optional] 

### Return type

[**list[Annotation]**](Annotation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

