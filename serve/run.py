from flask import Flask
from avro.datafile import DataFileReader
from avro.io import DatumReader
import json

app = Flask(__name__)


@app.route('/user')
def user_schema():
    with open("schema/user.avsc") as schema_file:
        schema = json.load(schema_file)
    with open("protocols/user.avpr") as protocol_file:
        protocol = json.load(protocol_file)
    resp = {
        'schema': schema,
        'protocol': protocol
    }
    return json.dumps(resp)


@app.route('/user/get')
def get_users():
    reader = DataFileReader(open("users.avro", "r"), DatumReader())
    return json.dumps([user for user in reader])


if __name__ == '__main__':
    app.run()