import requests
import utils
# import logging
#
# import http.client as http_client
# http_client.HTTPConnection.debuglevel = 1
#
# logging.basicConfig()
# logging.getLogger().setLevel(logging.DEBUG)
# requests_log = logging.getLogger("requests.packages.urllib3")
# requests_log.setLevel(logging.DEBUG)
# requests_log.propagate = True

HEADERS = {'accept': 'application/json', 'content-Type': 'application/json'}

class ApiTester:
    def __init__(self, data, option={}):
        self.apis = data['apis']
        self.hosts = data['hosts']
        self.config = data['config']

    def test_apis(self):
        summary = {'PASS': 0, 'FAIL': 0, 'SKIP': 0}
        for a, api in enumerate(self.apis, 1):
            print('# {}: {} {}'.format(a, api['method'], api['path']))
            if api.get('skip', False):
                summary['SKIP'] += 1
                print('> SKIP~')
                continue
            responses = []
            for h, host in enumerate(self.hosts, 1):
                method = api['method']
                url = 'http://' + host + api['path']
                ignore_keys = api.get('ignoreKeys', []) + self.config.get('globalIgnoreKeys', [])
                if self.config['log'] in ['debug', 'info']:
                    print('\t{} {}'.format(method, url))
                response = requests.request(method, url, json=api.get('body'), headers=HEADERS, timeout=10)
                if self.config['log'] == 'debug':
                    print(response.text)
                responses.append(response)
            equals = self.equals_responses(responses, ignore_keys)
            if equals:
                summary['PASS'] += 1
            else:
                summary['FAIL'] += 1
            if not equals:
                for r in responses:
                    print(r)
            print('> {}'.format('PASS.' if equals else 'FAIL!'))
        print('==> Summary: {}'.format(summary))

    @staticmethod
    def merge_ignore_keys(api, config):
        ignore_keys = api.get('ignoreKeys', [])
        ignore_keys += config.get('globalIgnoreKeys', [])
        return ignore_keys

    @staticmethod
    def equals_responses(responses, ignore_keys=[]):
        for i in range(len(responses) - 1):
            if not utils.equals_headers(responses[i].headers, responses[i + 1].headers, ignore_keys):
                return False
            if not utils.equals_bodies(responses[i].json(), responses[i + 1].json(), ignore_keys):
                return False
        return True
