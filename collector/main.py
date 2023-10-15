import requests
import time


API_URL = 'https://collectionapi.metmuseum.org/public/collection/v1/'


def collect():
    response = requests.get(API_URL + 'objects')
    object_ids = response.json()['objectIDs']
    for object_id in object_ids:
        response = requests.get(API_URL + 'objects/' + str(object_id))
        object = response.json()
        image = object['primaryImageSmall']
        if image:
            print(image)
        time.sleep(1)
    collect()


if __name__ == '__main__':
    collect()
