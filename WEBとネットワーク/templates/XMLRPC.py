#サーバーで処理してclientに結果を返す。
from xmlrpc.server import SimpleXMLRPCServer#PythonでRPC（Remote Procedure Call）サーバーを作る

with SimpleXMLRPCServer(('127.0.0.1', 8000)) as server:

    def add_num(x, y):
        return(x + y)
    
    server.register_function(add_num, 'add_num')
    server.serve_forever()