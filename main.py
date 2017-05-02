import data_loader
from api_tester import ApiTester

if __name__ == '__main__':
    data = data_loader.load_data()
    apiTester = ApiTester(data)
    apiTester.test_apis()


