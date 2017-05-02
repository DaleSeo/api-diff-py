import json


def load_data(path='data.json'):
    with open(path) as file:
        data = json.load(file)
        apis = data['apis']
        hosts = data['hosts']

    print('Loading data...')
    print('- apis: ' + str(apis))
    print('- hosts: ' + str(hosts))
    print('All data has been loaded...')

    return data