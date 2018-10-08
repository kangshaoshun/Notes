#coding:utf-8
import sys
from SimpleXMLRPCServer import SimpleXMLRPCServer
reload(sys)
sys.setdefaultencoding('utf-8')

def file_reader(file_name):
    with open(file_name)as f:
        return f.read()

server = SimpleXMLRPCServer(('localhost', 8000))
server.register_introspection_functions()

server.register_function(file_reader)
server.serve_forever()

