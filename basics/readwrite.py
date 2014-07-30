import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

schema = avro.schema.parse(open("models/user.avsc").read())

writer = DataFileWriter(open("users.avro", "w"), DatumWriter(), schema)
writer.append({
    "username": "granttoeppen",
    "eid": "test_eid",
    "email": "grant@adroll.com",
    "first_name": "Grant",
    "last_name": "Toeppen"
})
writer.append({
    "username": "spicy",
    "eid": "test_eid",
    "email": "sp[icy@adroll.com",
    "first_name": "Spicy",
    "last_name": "McHaggis"
})
writer.close()

reader = DataFileReader(open("users.avro", "r"), DatumReader())
for user in reader:
    print user
reader.close()