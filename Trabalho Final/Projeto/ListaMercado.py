from dado.Mercado import Mercado
from dado.Item import Item
from json import JSONEncoder 

class ListaMercado(JSONEncoder):
    def __init__(self, mercado:Mercado):
        self.mercado = mercado
        self.itens = []
        self.custo_total = 0

    def adicionar_item(self, item:Item):
        self.itens.append(item)
        self.custo_total += item.custo

    def imprimir(self):
        mercado = self.mercado.nome
        print('-'*30)
        print('{}:'.format(mercado))
        print('-'*30)

        for item in self.itens:
            print('Produto: {} | Marca: {} | Valor: {:.2f}'.format(item.produto.nome, item.marca.nome, item.custo))
        
        print('\nCusto: R$ {:.2f}'.format(self.custo_total))
