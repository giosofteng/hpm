import random
import requests


records_cache = {}


def get_record(o):
    object_id = random.choice(o)

    if object_id in records_cache:
        return records_cache[object_id]

    response = requests.get('https://collectionapi.metmuseum.org/public/collection/v1/objects/' + str(object_id))
    records_cache[object_id] = response.json()
    return records_cache[object_id]


if __name__ == '__main__':
    response = requests.get('https://collectionapi.metmuseum.org/public/collection/v1/departments')
    departments = response.json()['departments']

    for department in departments:
        response = requests.get('https://collectionapi.metmuseum.org/public/collection/v1/objects?departmentIds='
                                + str(department['departmentId']))
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
