from grafo.Aresta import Aresta

class GrafoSteiner(object):
    def __init__(self):
        self.steiner = set()
        self.terminal = set()
        self.arestas = dict()

    def imprimir_conjunto_vertices(self, conjunto:set, nome_conjunto:str):
        print('{}: {}'.format(nome_conjunto, *conjunto))


    def ler_dados(self, id_produto:int, id_mercado:int, custo:float):
        nova_aresta = Aresta(id_produto, id_mercado, custo)
        self.terminal.add(id_produto)
        self.steiner.add(id_mercado)
        
        if id_produto in arestas.keys():
            self.arestas[id_produto].append(nova_aresta)
        else:
            self.arestas[id_produto] = [nova_aresta]
    
    def adicionar_raiz(self):
        vertice_raiz = 0
        custo_para_raiz = 0

        for mercado in self.steiner:
            self.arestas[mercado] = [Aresta(mercado, vertice_raiz, custo_para_raiz)]

    def get_aresta_menor_custo(self, vertice:int) -> Aresta:
        arestas_do_vertice = self.arestas[vertice]

        aresta_menor_custo = Aresta(0, 0, float('inf'))

        for aresta in arestas_do_vertice:
            if aresta < aresta_menor_custo:
                aresta_menor_custo = aresta

        return aresta_menor_custo

    def calcula_arvore_steiner(self) -> GrafoSteiner:
        arvore_steiner = GrafoSteiner()

        for vertice in self.terminal:
            aresta_menor_custo = get_aresta_menor_custo(vertice)
            arvore_steiner.terminal.add(vertice)
            arvore_steiner.arestas[aresta_menor_custo.destino] = aresta_menor_custo
            arvore_steiner.steiner.add(aresta_menor_custo.destino)
        
        return arvore_steiner