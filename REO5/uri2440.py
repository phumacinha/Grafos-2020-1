'''
Disciplina:
    GCC218 - Algoritmo em Grafos

Integrantes: 
    Igor Antônio dos Santos Alves Mendes
    Isaías Gonçalves Ribeiro
    Pedro Antônio de Souza

Nome do Exercício:
    Famílias de Troia - 2440

Estratégia Adotada:
    Modelamos um grafo onde os vértices representam os elementos da comunidade 
    e as arestas representam a existência de parentesco entre os elementos
    representados pelos vértices vizinhos. Conclui-se, então, que a quantidade 
    de famílias será equivalente à quantidade de componentes conexas desse
    grafo. Assim, aplicamos uma busca em profundidade para fazermos a contagem
    de componentes conexas. Infelizmente, no URI Online Judge, nosso código
    apresenta "Time limir exceeded" e não encontramos solução, apesar de
    funcionar perfeitamente em nossas máquinas.
'''

# n: armazenará a quantidade de elementos da comunidade
# m: armazenará a quantidade de relações de parentescos existentes
n, m = map(int, input().split())

grafo = [None]*n  # Matriz de adjacencia
visitado = [False]*n  # Lista que armazena o status de visitado dos vértices
quantidade_familias = 0  # Armazena a quantidade de famílias (componentes conexas)

# Executa busca em profundidade marcando vértices como visitado.
def busca_em_profundidade (vertice:int):
    global visitado

    # Cria uma pilha pra definir próximos vértices a serem visitados
    pilha = []
    pilha.append(vertice)  

    while pilha:  
        # Retira o elemento di topo da pilha
        vertice = pilha.pop(0) 

        # Verifica se o vértice já foi visitado e, em caso positivo, pula pra próxima iteração.
        if not visitado[vertice]:
            visitado[vertice] = True 

            # Verifica se o vértice possui vizinhos
            if grafo[vertice]:
                # Caso possua, adiciona os vizinhos não visitados na pilha
                for vizinho in grafo[vertice]:  
                    if not visitado[vizinho]:  
                        pilha.insert(0, vizinho)

# Adiciona arestas ao grafo. Verifica se os vértices v e u já possuem vizinhos,
# em caso positivo, apenas acrescenta o novo vizinho e em caso negativo, cria
# uma lista para armazenar as adjacências.
def adiciona_vizinhanca (v, u):
    global grafo

    if isinstance(grafo[v], list):
        grafo[v].append(u)
    else:
        grafo[v] = [u]

    if isinstance(grafo[u], list):
        grafo[u].append(v)
    else:
        grafo[u] = [v]

# Lê todas as relações de parentesco.
for _ in range(m):
    v, u = map(int, input().split())
    adiciona_vizinhanca(v-1, u-1)

# Percorre todos os vértices do grafo aplicando a busca em profundidade e conta
# as componentes conexas.
for v in range(n):
    if not visitado[v]:
        quantidade_familias += 1
        busca_em_profundidade(v)

print(quantidade_familias)