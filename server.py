import xmlrpc.client

# Crie um proxy para se conectar ao servidor RPC
proxy = xmlrpc.client.ServerProxy('http://lcoalhost:8000/RPC2')

# Chame a função remota para obter a data atual
try:
    current_date = proxy.get_date()
    print("Data atual obtida do servidor RPC:", current_date)
except Exception as e:
    print("Erro ao chamar a função remota:", e)
