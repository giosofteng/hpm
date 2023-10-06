import json
import random
import requests
from types import SimpleNamespace


records_cache = {}


def parse_json(s):
    return json.loads(
        s,
        object_hook=lambda d: SimpleNamespace(**d)
    )


def get_record(o):
    object_id = random.choice(o)

    if object_id in records_cache:
        return records_cache[object_id]

    response = requests.get('https://collectionapi.metmuseum.org/public/collection/v1/objects/' + str(object_id))
    records_cache[object_id] = parse_json(response.content)
    return records_cache[object_id]


if __name__ == '__main__':
    response = requests.get('https://collectionapi.metmuseum.org/public/collection/v1/departments')
    departments = parse_json(response.content).departments

    for department in departments:
        response = requests.get('https://collectionapi.metmuseum.org/public/collection/v1/objects?departmentIds='
                                + str(department.departmentId))
        object_ids = parse_json(response.content).objectIDs

        record = get_record(object_ids)
        attempts = 0
        while not record.isPublicDomain:
            attempts += 1
            if attempts > 10:
                break
            print('RETRIEVED RECORD IS NOT IN PUBLIC DOMAIN - RETRYING...')
            record = get_record(object_ids)
        # ! GET CACHED VALUE
        print(department.displayName + ': ' + (record.primaryImageSmall or 'NA'))
