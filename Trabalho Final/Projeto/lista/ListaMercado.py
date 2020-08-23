from dado.Mercado import Mercado

class ListaMercado(object):
    def __init__(self, mercado:Mercado):
        self.mercado = mercado
        self.itens = []
        self.custo_total = 0

    def adicionar_item(self, item:Item):
        self.itens.append(item)
        self.custo_total += item.valor

    def imprimir(self):
        mercado = self.mercado.nome
        print('-'*30)
        print('{}:'.format(mercado))
        print('-'*30)

        for item in itens:
            print('Produto: {} | Marca: {} | Valor: {.2f}'.format(item.produto, item.marca, item.valor))
        
        print('\nCusto: R$ {.2f}'.format(self.custo_total))

