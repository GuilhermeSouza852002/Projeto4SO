from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import datetime


# Classe para manipular as solicitações de RPC
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


# Crie um servidor RPC simples
with SimpleXMLRPCServer(('localhost', 8000), requestHandler=RequestHandler) as server:
    # Defina uma função remota que retorna a data atual
    def get_current_date():
        return datetime.datetime.now().isoformat()


    # Registre a função no servidor RPC
    server.register_function(get_current_date, 'get_date')

    print("Servidor RPC esperando por solicitações na porta 8000...")

    # Inicie o servidor
    server.serve_forever()
