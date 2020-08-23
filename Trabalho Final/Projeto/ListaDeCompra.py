from dado.Item import Item
from grafo.Grafo import Grafo
from ListaMercado import ListaMercado
import json

class ListaDeCompra(object):
    def __init__(self, produtos:list):
        self.lista = {}
        self.custo_total = 0

        self.produtos_indisponiveis = {}
        for produto in produtos:
            self.produtos_indisponiveis[produto.id_produto] = produto

        self.grafo = Grafo()

    def adicionar_item(self, item:Item):
        self.grafo.adicionar_aresta(item.mercado, item.produto, item.marca, item.custo)
        if item.produto.id_produto in self.produtos_indisponiveis.keys():
            del self.produtos_indisponiveis[item.produto.id_produto]

    def gerar_lista(self):
        arvore = self.grafo.calcula_floresta_steiner()

        for aresta in arvore.arestas.values():
            item = Item(aresta[0].mercado, aresta[0].produto, aresta[0].marca, aresta[0].custo)
            
            if item.mercado.id_mercado not in self.lista.keys():
                self.lista[item.mercado.id_mercado] = ListaMercado(item.mercado)

            self.lista[item.mercado.id_mercado].adicionar_item(item)