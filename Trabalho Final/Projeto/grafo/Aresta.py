from dado.Produto import Produto
from dado.Mercado import Mercado
from dado.Marca import Marca

class Aresta(object):
    def __init__(self, mercado:Mercado, produto:Produto, marca:Marca, custo:float):
        self.mercado = mercado
        self.produto = produto
        self.marca = marca
        self.custo = custo


    def __lt__(self, outra_aresta) -> bool:
        return self.custo < outra_aresta.custo

'''class Aresta(object):
    def __init__(self, origem:int, destino:int, custo:float):
        self.origem = origem
        self.destino = destino
        self.custo = custo
    
    def imprimir(self):
        print('({}, {}) : {}'.format(self.origem, self.destino, self.custo))


    def __lt__(self, outra_aresta) -> bool:
        return self.custo < outra_aresta.custo'''