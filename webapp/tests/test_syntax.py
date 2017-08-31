"""
All functions with names prefixed with "test_" will be automatically loaded and
used. Everything following this prefix will be used to report this test to
the UI (with underscores replaced with spaces), so that the following

    def test_Always_Fails(api_client: ApiClient):
        fail('this method always fails')

This method will be named "Always Fails", it will fail and the message "this
method always fails" will be reported to the UI.

    def test_Always_Passes(api_client: ApiClient):
        return None

This test will be named "Always Passes" and will pass. Upon calling fail() a
test will terminate and its failure will be reported. If a test does not call
fail() then it will pass, unless it throws an exception. Exceptions will be
caught and automatically reported to the UI. Tests needn't return anything, and
if they do the result will not be used.
"""

from webapp.tests.test_handler import fail

from webapp.client.swagger_client.apis.concepts_api import ConceptsApi
from webapp.client.swagger_client.apis.statements_api import StatementsApi
from webapp.client.swagger_client.apis.evidence_api import EvidenceApi

def test_is_online(api_client):
    concepts_api = ConceptsApi(api_client)
    concepts = concepts_api.get_concepts(keywords='e', page_size=1)

def test_workflow(api_client):
    concepts_api = ConceptsApi(api_client)
    statements_api = StatementsApi(api_client)
    evidence_api = EvidenceApi(api_client)

    page_size = 5;
    concepts = concepts_api.get_concepts(keywords='e', page_size=page_size)

    if len(concepts) is 0:
        fail('Test inconclusive, no concepts were found)')

    if len(concepts) > page_size:
        fail('Asked for a page size of',page_size,'got', len(concepts),'instead.')

    details = concepts_api.get_concept_details(concepts[0].id)

    if details is None or len(details) < 1:
        fail('Test inconclusive, no concept details were found')

    page_size = 10
    statements = statements_api.get_statements(
        c=[concept.id for concept in concepts],
        page_size=page_size
    )

    if len(statements) < 1:
        fail('Test inconclusive, no statements were found)')

    if len(statements) > page_size:
        fail('Asked for a page size of',page_size,'got', len(statements),'instead.')

    # Evidene may be infrequent, so we will iterate through each of the
    # statements until we find something. If we find nothing we return False.
    page_size=10
    for statement in statements:
        evidences = evidence_api.get_evidence(statements[0].id, page_size=page_size)
        if evidences is not None or len(evidences) > 0:
            break
        if len(evidences) > page_size:
            fail('Asked for a page size of',page_size,'got', len(evidences),'instead.')
    else:
        fail('Test inconclusive, no evidence was found)')

def test_concept_pagination(api_client):
    api = ConceptsApi(api_client)

    concepts = api.get_concepts(keywords='e', page_number=1, page_size=45)
    size = int(len(concepts) / 2)
    l1 = api.get_concepts(keywords='e', page_number=1, page_size=size)
    l2 = api.get_concepts(keywords='e', page_number=2, page_size=size)

    for a, b in zip(l1 + l2, concepts[:2*size]):
        if a.id != b.id:
            fail(
                'Pagination failed. The first page of', 2*size,
                'items is not equivalent to the first and second pages of',
                size, 'items.'
            )

def test_statement_pagination(api_client):
    api = ConceptsApi(api_client)
    concepts = api.get_concepts(keywords='e', page_number=1, page_size=5)

    api = StatementsApi(api_client)

    statements = api.get_statements(c=[c.id for c in concepts], page_number=1, page_size=45)

    size = int(len(concepts) / 2)

    l1 = api.get_statements(c=[c.id for c in concepts], page_number=1, page_size=size)
    l2 = api.get_statements(c=[c.id for c in concepts], page_number=2, page_size=size)

    for a, b in zip(l1 + l2, statements[:2*size]):
        if a.id != b.id:
            fail(
                'Pagination failed. The first page of', 2*size,
                'items is not equivalent to the first and second pages of',
                size, 'items.'
            )
