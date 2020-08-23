class Aresta(object):
    def __init__(self, origem:int, destino:int, custo:float):
        self.origem = origem
        self.destino = destino
        self.custo = custo
    
    def imprimir(self):
        print('({}, {}) : {}'.format(self.origem, self.destino, self.custo))


    def __lt__(self, outra_aresta:Aresta) -> bool:
        return self.custo < outra_aresta.custo