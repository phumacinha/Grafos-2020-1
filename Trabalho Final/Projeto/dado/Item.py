from dado.Produto import Produto
from dado.Mercado import Mercado
from dado.Marca import MarcaidMercado

class Item(object):
    def __init__(self, idItem:int, mercado:Mercado, produto:Produto, marca:Marca, custo:float):
        self.idItem = idItem
        self.mercado = mercado
        self.produto = produto
        self.marca = marca
        self.custo = custo
