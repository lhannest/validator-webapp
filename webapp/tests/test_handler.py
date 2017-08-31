import importlib
import pkgutil
import inspect

from webapp import tests

from webapp.client.swagger_client.api_client import ApiClient
from webapp.client.swagger_client.rest import ApiException


def _import_submodules(package, recursive=True):
    """ https://stackoverflow.com/a/25562415
    Import all submodules of a module, recursively, including subpackages

    :param package: package (name or actual module)
    :type package: str | module
    :rtype: dict[str, types.ModuleType]
    """
    if isinstance(package, str):
        package = importlib.import_module(package)
    results = {}
    for loader, name, is_pkg in pkgutil.walk_packages(package.__path__):
        full_name = package.__name__ + '.' + name
        results[full_name] = importlib.import_module(full_name)
        if recursive and is_pkg:
            results.update(_import_submodules(full_name))
    return results

class TestHandler(object):
    def __init__(self):
        submodules = _import_submodules(package=tests, recursive=False).values()
        self.__tests = {}

        for module in submodules:
            functions = inspect.getmembers(module, inspect.isfunction)
            for function_name, function in functions:
                if function_name.startswith('test_'):
                    terms = function_name.split('_')
                    if len(terms) > 1:
                        name = ' '.join(terms[1:])
                        self.__tests[name] = function

    def get_tests(self):
        return self.__tests.values()

    def get_names(self):
        return list(self.__tests.keys())

    def get_tests_with_names(self):
        return self.__tests.items()

    def run_tests_for_unknown_beacon(self, url, test_names=[]):
        results = []
        api_client = ApiClient(url)
        for test_name, test in self.get_tests_with_names():
            if test_names != [] and not (test_name in test_names):
                continue

            try:
                api_client.last_url_request = None
                test(api_client)
                results.append({
                    'test_name' : str(test_name),
                    'passed' : True,
                    'error' : None,
                })
            except Exception as e:
                results.append({
                    'test_name' : str(test_name),
                    'passed' : False,
                    'error' : {
                        'type' : e.__class__.__name__,
                        'message' : str(e),
                        'url_request' : api_client.last_url_request,
                    }
                })
        return results

    def run_tests(self, beacon, start_callback, pass_callback, fail_callback):
        """
        Gets all methods with names that are prefixed with "test_" in the
        webapp.test module, and runs them with the given url.

        :param beacon KnowledgeBeacon: The beacon being tested
        :param start_callback function: Callback for when a test begins
        :param pass_callback function: Callback for when a test passes
        :param fail_callback function: Callback for when a test fails

        For callbacks, ensure they have the signature required by this method.
        """
        api_client = ApiClient(beacon.url)

        for test_name, test in self.get_tests_with_names():
            try:
                api_client.last_url_request = None
                start_callback(test_name=test_name, beacon=beacon)
                test(api_client)
                pass_callback(test_name=test_name, beacon=beacon)
            except ApiException as e:
                fail_callback(
                    test_name=test_name,
                    beacon=beacon,
                    error_response={
                        'type' : 'ApiException',
                        'message' : str(e),
                        'url' : api_client.last_url_request,
                        'beacon_name' : beacon.name,
                        'test_name' : test_name,
                    }
                )
            except FailedTestException as e:
                fail_callback(
                    test_name=test_name,
                    beacon=beacon,
                    error_response={
                        'type' : 'FailedTestException',
                        'message' : str(e),
                        'url' : api_client.last_url_request,
                        'beacon_name' : beacon.name,
                        'test_name' : test_name,
                    }
                )
            except Exception as e:
                fail_callback(
                    test_name=test_name,
                    beacon=beacon,
                    error_response={
                        'type' : 'Unknown',
                        'message' : str(e),
                        'url' : api_client.last_url_request,
                        'beacon_name' : beacon.name,
                        'test_name' : test_name,
                    }
                )


class FailedTestException(Exception):
    def __init__(self, message=None):
        super(FailedTestException, self).__init__(message)

def fail(message=None, *args):
    if (args):
        message = message + ' ' + ' '.join([str(arg) for arg in args])
    raise FailedTestException(message)
