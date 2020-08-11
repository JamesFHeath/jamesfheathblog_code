import json

json_string = '{"key": "value", "array_key": [1, 2, 3], "another_key_for_boolean": false}'

python_object = json.loads(json_string)
python_object


python_object['new_key'] = None
python_object['array_key'].append(4)
python_object

new_json_string = json.dumps(python_object)
new_json_string


python_object = {'parent': {'child_1': [1, 2, 3], 'child_2': True}}

json.dumps(python_object, indent=4)

import datetime

now = datetime.datetime.now()
now

# json.dumps(now) TypeError

now = datetime.datetime.now()

class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if type(o) == datetime.datetime:
            return {'datetime_now': str(o)}
        return json.JSONEncoder.default(self, o)

date_time_encoder = DateTimeEncoder()

now_json_string = date_time_encoder.encode(now)

now_json_string