from dado.Mercado import Mercado
from dado.Produto import Produto
from dado.Marca import Marca
from dado.Item import Item
from grafo.Aresta import Aresta

class Grafo(object):
    def __init__(self):
        self.steiner = set()
        self.terminal = set()
        self.arestas = dict()

    def imprimir_conjunto_vertices(self, conjunto:set, nome_conjunto:str):
        print('{}: {}'.format(nome_conjunto, *conjunto))

    def adicionar_aresta(self, mercado:Mercado, produto:Produto, marca:Marca, custo:float):
        nova_aresta = Aresta(mercado, produto, marca, custo)
        self.terminal.add(produto.id_produto)
        self.steiner.add(mercado.id_mercado)
        
        if produto.id_produto in self.arestas.keys():
            self.arestas[produto.id_produto].append(nova_aresta)
        else:
            self.arestas[produto.id_produto] = [nova_aresta]

    def get_aresta_menor_custo(self, id_produto:int) -> Aresta:
        arestas_do_produto = self.arestas[id_produto]

        aresta_menor_custo = Aresta(None, None, None, float('inf'))

        for aresta in arestas_do_produto:
            if aresta < aresta_menor_custo:
                aresta_menor_custo = aresta

        return aresta_menor_custo

    def calcula_floresta_steiner(self):
        floresta_steiner = Grafo()

        for id_produto in self.terminal:
            aresta_menor_custo = self.get_aresta_menor_custo(id_produto)
            floresta_steiner.terminal.add(id_produto)
            floresta_steiner.steiner.add(aresta_menor_custo.mercado.id_mercado)
            floresta_steiner.adicionar_aresta(aresta_menor_custo.mercado, aresta_menor_custo.produto, aresta_menor_custo.marca, aresta_menor_custo.custo)
        
        return floresta_steiner