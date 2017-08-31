import eventlet; eventlet.monkey_patch()

from configparser import ConfigParser

from flask import Flask, render_template, jsonify, request

from flask_socketio import SocketIO

from webapp.client.swagger_client import ApiClient
from webapp.client.swagger_client.apis.aggregator_api import AggregatorApi

from webapp.tests.test_handler import TestHandler
from webapp.tests.test_handler import FailedTestException

config = ConfigParser()
config.read('webapp/configfile')

app = Flask(__name__)
app.config['SECRET_KEY'] = config.get('flask', 'secret_key')
socketio = SocketIO(app, async_mode='threading')

pool = eventlet.greenpool.GreenPool(size=1000)

api_client = ApiClient(host=config.get('aggregator', 'url'))
aggregator_api = AggregatorApi(api_client)
beacons = aggregator_api.get_beacons()

test_handler = TestHandler()

state = {}

@app.route("/")
def main():
    global beacons
    beacon_list = [{'name' : beacon.name, 'url' : beacon.url, 'id' : beacon.id} for beacon in beacons]
    return render_template(
        'index.html',
        beacon_list=beacon_list,
        test_names=test_handler.get_names(),
    )

@app.route("/test/<path:beacon_url>/")
def custom_beacons(beacon_url):
    test_names = request.args.getlist('tests')
    results = test_handler.run_tests_for_unknown_beacon(beacon_url, test_names)
    return jsonify(results)

@app.route("/tests/")
def get_tests():
    return jsonify(test_handler.get_names())

@socketio.on('get_state')
def send_state():
    socketio.emit('set_state', list(state.values()), broadcast=True)
    socketio.sleep(0)

@socketio.on('test_beacon')
def handle_test_beacon(beacon_id):
    beacon = next((x for x in beacons if x.id == beacon_id), None)
    if beacon is not None:
        global pool
        pool.spawn(
            test_handler.run_tests,
            beacon,
            start_callback,
            pass_callback,
            fail_callback,
        )

def start_callback(test_name, beacon):
    set_state(test_name, beacon, in_progress=True)
    send_state()

def pass_callback(test_name, beacon):
    set_state(test_name, beacon, in_progress=False, is_passed=True)
    send_state()

def fail_callback(test_name, beacon, error_response):
    set_state(test_name, beacon, in_progress=False, is_passed=False, error_response=error_response)
    send_state()

def set_state(test_name, beacon, in_progress=False, is_passed=None, error_response=None):
    global state
    key = '[' + test_name + ',' + beacon.id + ']'
    state[key] = {
        'in_progress' : in_progress,
        'is_passed' : is_passed,
        'test_name' : test_name,
        'beacon_id' : beacon.id,
        'error_response' : error_response,
    }

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
