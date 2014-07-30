import sys
import httplib

import avro.ipc as ipc
import avro.protocol as protocol

PROTOCOL = protocol.parse(open("../protocols/../../protocols/user.avpr").read())

server_addr = ('localhost', 5000)