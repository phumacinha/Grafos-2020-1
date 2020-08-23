from dado.Produto import Produto
from dado.Mercado import Mercado
from dado.Marca import Marca

class Item(object):
    """Classe que representa um item do banco de dados.
    
    Args:
        mercado (Mercado): Mercado que o item pertence.
        produto (Produto): Produto referente ao item.
        marca (Marca): Marca do produto.
        custo (float): Valor do item.

    Attributes:
        mercado (Mercado): Mercado que o item pertence.
        produto (Produto): Produto referente ao item.
        marca (Marca): Marca do produto.
        custo (float): Valor do item.
    """

    def __init__(self, mercado:Mercado, produto:Produto, marca:Marca, custo:float):
        self.mercado = mercado
        self.produto = produto
        self.marca = marca
        self.custo = custo

    