# swagger_client.ConceptsApi

All URIs are relative to *http://kba.ncats.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_concept_details**](ConceptsApi.md#get_concept_details) | **GET** /concepts/{conceptId} | 
[**get_concepts**](ConceptsApi.md#get_concepts) | **GET** /concepts | 


# **get_concept_details**
> list[ConceptDetail] get_concept_details(concept_id, beacons=beacons, session_id=session_id)



Retrieves details for a specified concepts in the system, as specified by a (url-encoded) CURIE identifier of a concept known the given knowledge source. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConceptsApi()
concept_id = 'concept_id_example' # str | (url-encoded) CURIE identifier of concept of interest
beacons = ['beacons_example'] # list[str] | set of IDs of beacons to be used as knowledge sources for the query  (optional)
session_id = 'session_id_example' # str | identifier to be used for tagging session data  (optional)

try: 
    api_response = api_instance.get_concept_details(concept_id, beacons=beacons, session_id=session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptsApi->get_concept_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **concept_id** | **str**| (url-encoded) CURIE identifier of concept of interest | 
 **beacons** | [**list[str]**](str.md)| set of IDs of beacons to be used as knowledge sources for the query  | [optional] 
 **session_id** | **str**| identifier to be used for tagging session data  | [optional] 

### Return type

[**list[ConceptDetail]**](ConceptDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_concepts**
> list[Concept] get_concepts(keywords, semgroups=semgroups, page_number=page_number, page_size=page_size, beacons=beacons, session_id=session_id)



Retrieves a (paged) list of concepts in the system 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConceptsApi()
keywords = 'keywords_example' # str | a (urlencoded) space delimited set of keywords or substrings against which to match concept names and synonyms
semgroups = 'semgroups_example' # str | a (url-encoded) space-delimited set of semantic groups (specified as codes CHEM, GENE, ANAT, etc.) to which to constrain concepts matched by the main keyword search (see [SemGroups](https://metamap.nlm.nih.gov/Docs/SemGroups_2013.txt) for the full list of codes)  (optional)
page_number = 56 # int | (1-based) number of the page to be returned in a paged set of query results  (optional)
page_size = 56 # int | number of concepts per page to be returned in a paged set of query results  (optional)
beacons = ['beacons_example'] # list[str] | set of IDs of beacons to be used as knowledge sources for the query  (optional)
session_id = 'session_id_example' # str | identifier to be used for tagging session data  (optional)

try: 
    api_response = api_instance.get_concepts(keywords, semgroups=semgroups, page_number=page_number, page_size=page_size, beacons=beacons, session_id=session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptsApi->get_concepts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keywords** | **str**| a (urlencoded) space delimited set of keywords or substrings against which to match concept names and synonyms | 
 **semgroups** | **str**| a (url-encoded) space-delimited set of semantic groups (specified as codes CHEM, GENE, ANAT, etc.) to which to constrain concepts matched by the main keyword search (see [SemGroups](https://metamap.nlm.nih.gov/Docs/SemGroups_2013.txt) for the full list of codes)  | [optional] 
 **page_number** | **int**| (1-based) number of the page to be returned in a paged set of query results  | [optional] 
 **page_size** | **int**| number of concepts per page to be returned in a paged set of query results  | [optional] 
 **beacons** | [**list[str]**](str.md)| set of IDs of beacons to be used as knowledge sources for the query  | [optional] 
 **session_id** | **str**| identifier to be used for tagging session data  | [optional] 

### Return type

[**list[Concept]**](Concept.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

