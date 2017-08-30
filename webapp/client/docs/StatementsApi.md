# swagger_client.StatementsApi

All URIs are relative to *http://kba.ncats.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_statements**](StatementsApi.md#get_statements) | **GET** /statements | 


# **get_statements**
> list[Statement] get_statements(c, page_number=page_number, page_size=page_size, keywords=keywords, semgroups=semgroups, beacons=beacons, session_id=session_id)



Given a list of [CURIE-encoded](https://www.w3.org/TR/curie/) identifiers of exactly matching concepts, retrieves a paged list of concept-relations where either the subject or object concept matches at least one concept in the input list 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatementsApi()
c = ['c_example'] # list[str] | set of [CURIE-encoded](https://www.w3.org/TR/curie/) identifiers of exactly matching concepts to be used in a search for associated concept-relation statements 
page_number = 56 # int | (1-based) number of the page to be returned in a paged set of query results  (optional)
page_size = 56 # int | number of concepts per page to be returned in a paged set of query results  (optional)
keywords = 'keywords_example' # str | a (url-encoded, space-delimited) string of keywords or substrings against which to match the subject, predicate or object names of the set of concept-relations matched by any of the input exact matching concepts  (optional)
semgroups = 'semgroups_example' # str | a (url-encoded, space-delimited) string of semantic groups (specified as codes CHEM, GENE, ANAT, etc.) to which to constrain the subject or object concepts associated with the query seed concept (see [SemGroups](https://metamap.nlm.nih.gov/Docs/SemGroups_2013.txt) for the full list of codes)  (optional)
beacons = ['beacons_example'] # list[str] | set of IDs of beacons to be used as knowledge sources for the query  (optional)
session_id = 'session_id_example' # str | identifier to be used for tagging session data  (optional)

try: 
    api_response = api_instance.get_statements(c, page_number=page_number, page_size=page_size, keywords=keywords, semgroups=semgroups, beacons=beacons, session_id=session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatementsApi->get_statements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **c** | [**list[str]**](str.md)| set of [CURIE-encoded](https://www.w3.org/TR/curie/) identifiers of exactly matching concepts to be used in a search for associated concept-relation statements  | 
 **page_number** | **int**| (1-based) number of the page to be returned in a paged set of query results  | [optional] 
 **page_size** | **int**| number of concepts per page to be returned in a paged set of query results  | [optional] 
 **keywords** | **str**| a (url-encoded, space-delimited) string of keywords or substrings against which to match the subject, predicate or object names of the set of concept-relations matched by any of the input exact matching concepts  | [optional] 
 **semgroups** | **str**| a (url-encoded, space-delimited) string of semantic groups (specified as codes CHEM, GENE, ANAT, etc.) to which to constrain the subject or object concepts associated with the query seed concept (see [SemGroups](https://metamap.nlm.nih.gov/Docs/SemGroups_2013.txt) for the full list of codes)  | [optional] 
 **beacons** | [**list[str]**](str.md)| set of IDs of beacons to be used as knowledge sources for the query  | [optional] 
 **session_id** | **str**| identifier to be used for tagging session data  | [optional] 

### Return type

[**list[Statement]**](Statement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

