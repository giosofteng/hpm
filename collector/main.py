import random
import requests


API_URL = 'https://collectionapi.metmuseum.org/public/collection/v1/'
RECORDS_CACHE = {}


def get_record(o):
    object_id = random.choice(o)

    if object_id in RECORDS_CACHE:
        return RECORDS_CACHE[object_id]

    response = requests.get(API_URL + 'objects/' + str(object_id))
    RECORDS_CACHE[object_id] = response.json()
    return RECORDS_CACHE[object_id]


if __name__ == '__main__':
    response = requests.get(API_URL + 'departments')
    departments = response.json()['departments']

    for department in departments:
        response = requests.get(API_URL + 'objects?departmentIds=' + str(department['departmentId']))
        object_ids = response.json()['objectIDs']

        record = get_record(object_ids)
        attempts = 0
        while not record['isPublicDomain']:
            attempts += 1
            if attempts > 1:
                break
            print('RETRIEVED RECORD IS NOT IN PUBLIC DOMAIN - RETRYING...')
            record = get_record(object_ids)
        # ! GET CACHED VALUE
        print(department['displayName'] + ': ' + (record['primaryImageSmall'] or 'NA'))
