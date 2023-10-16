import requests
import time


class DataCollector:
    def __init__(self):
        self._api_url = 'https://collectionapi.metmuseum.org/public/collection/v1/'
        self._object_ids = []

    def _get_object_ids(self):
        response = requests.get(self._api_url + 'objects')
        self._object_ids = response.json()['objectIDs']

    def start_data_collection(self):
        self._get_object_ids()
        for object_id in self._object_ids:
            response = requests.get(self._api_url + 'objects/' + str(object_id))
            data = response.json()
            image_url = data['primaryImageSmall']
            if image_url:
                print(image_url)
            else:
                print('IMAGE IS NOT IN PUBLIC DOMAIN -- SKIPPING...')
            time.sleep(1)
        self.start_data_collection()


if __name__ == '__main__':
    data_collector = DataCollector()
    data_collector.start_data_collection()
