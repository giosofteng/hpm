import requests
import unittest

from source.data_collector import DataCollector


class TestAPI(unittest.TestCase):
    def setUp(self):
        data_collector = DataCollector()
        self.api_url = data_collector.api_url

    def test_api_endpoints(self):
        response = requests.get(self.api_url + 'objects')
        self.assertEqual(200, response.status_code)

        object_id = response.json()['objectIDs'][0]
        response = requests.get(self.api_url + 'objects/' + str(object_id))
        self.assertEqual(200, response.status_code)


if __name__ == '__main__':
    unittest.main()
