class Teste(object):
    def __init__(self, teste:str):
        self.teste = teste

arestas = dict()
teste = Teste('oi')
arestas[teste] = 'tchau'
if (Teste('oi') in arestas.keys()):
    print('rolou')
else:
    print (arestas.keys())
    print (Teste('oi'))