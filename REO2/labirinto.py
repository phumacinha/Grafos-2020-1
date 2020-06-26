'''
Disciplina:
	GCC218 - Algoritmo em Grafos

Integrantes: 
	Igor Antônio dos Santos Alves Mendes
	Isaías Gonçalves Ribeiro
	Pedro Antônio de Souza

Nome do Exercício:
	Labirinto - 1621

Estratégia Adotada:
	Para a resolução do problema utilizamos o Algortimo de Dijkstra.
	Cada caracter da entrada foi modelado como um vértice, sempre que o caracter for igual '.', verificava-se os caracteres entorno dele.
	Caso o caracter do entorno for igual a '.' é adicionado uma aresta ligando-os.
	A partir da interpretação do enunciado supomos que o grafo será sempre conexo.
	Encontramos o primeiro vértice que continha vizinhos e aplicamos o algoritmo a partir dele.
	A partir das distâncias encontradas, selecionamos o vértice com a maior distância e reaplicamos 
	o Algortimo de Dijkstra a partir dele para encontrar novas distancias,
	pois somente a partir dele é possível encontrar distâncias superiores.
	Por fim, retornamos a maior distância encontrada na segunda aplicação.
'''

'''
    Classe para implementar filas de prioridade para os menores elementos.
'''
class FilaDePrioridade:
    def __init__(self):
        self.fila = list()

    def push(self, element):
        self.fila.append(element)
        self.fila.sort()
    
    def pop(self):
        return self.fila.pop()

    def empty(self):
        return len(self.fila) == 0

distancias = list()  # Lista de inteiros para armazenar distâncias encontradas no Algoritmo de Dijkstra
grafo = list(list())  # Lista de adjacência
labirinto = list()  # Lista de string's (ou matriz de caracteres) que armazenará as linhas da entrada
N = int()  # Número de linhas do labirinto
M = int()  # Número de colunas do labirinto

'''
    Algoritmp de Dijkstra que solucuiona o problema do caminho mais curto de um grafo (direcionado ou não)
    com arestas de peso não negativo.
'''
def dijkstra (origem:int):
    global N, M, distancias, grafo

    distancias.clear()
    # Inicializa a lista de distâncias com todos infinito para todos os vértices
    distancias = [float('inf') for _ in range(N*M)]
    distancias[origem] = 0  # Define a distância da origem como zero.

    # Fila que armazenará tuplas do tipo (distância, vértice) e será sempre ordenada
    # de forma crescente pela distância e, em caso de empate, pela ordem lexicográfica
    # dos vértices.
    fila_de_prioridade = FilaDePrioridade()
    fila_de_prioridade.push((0, origem))

    # Enquanto houver elementos na fila, tenta relaxar as arestas
    while not fila_de_prioridade.empty():
        prioritario = fila_de_prioridade.pop()
        vertice = prioritario[1]

        for i in range(len(grafo[vertice])):
            vizinho = grafo[vertice][i]

            # Relaxa arestas
            if distancias[vizinho] > distancias[vertice] + 1:
                distancias[vizinho] = distancias[vertice] + 1
                fila_de_prioridade.push((distancias[vizinho], vizinho))


while (True):
    entrada = input().split()
    # N é a quantidade de linhas do labirinto
    N = int(entrada[0])

    # M é a quantidade de colunas do labirinto
    M = int(entrada[1])

    # Verifica se N e M são iguais a zero.
    if not N and not M:
        break

    grafo = [list() for _ in range(N*M)]

    # Insere as linhas do labirinto.
    for _ in range(N):
        labirinto.append(input())

    for i in range(N):
        for j in range(M):
            # Calculo do índice do vértice
            vertice = M*i + j

            if labirinto[i][j] == '.':
                if i > 0:  # Verifica se não está na primeira linha
                    if labirinto[i-1][j] == '.':  # Verifica se vizinho superior é caminho livre
                        grafo[vertice].append(M*(i - 1) + j)
                
                if i < N - 1:  # Verifica se não está na útlima linha
                    if labirinto[i+1][j] == '.':  # Verifica se vizinho inferior é caminho livre
                        grafo[vertice].append(M*(i + 1) + j)
                
                if j > 0:  # Verifica se não está na primeira coluna
                    if labirinto[i][j-1] == '.':  # Verifica se vizinho da esquerda é caminho livre
                        grafo[vertice].append(vertice - 1)
                
                if j < M - 1:  # Verifica se não está na última coluna
                    if labirinto[i][j+1] == '.':  # Verifica se vizinho da direita é caminho livre
                        grafo[vertice].append(vertice + 1)

    # Encontra o primeiro vértice que possui vizinhos.            
    for v in range(N):
        if len(grafo[v]) > 0:
            break
    
    dijkstra(v)
    maior_distancia = float('-inf')

    # Retorna a maior distância e seu vértice.
    for i in range(N*M):
        if distancias[i] != float('inf') and distancias[i] > maior_distancia:
            maior_distancia = distancias[i]
            v = i
    
    dijkstra(v)
    
    # Imprime a maior distância
    print(max(list(filter(lambda d: d != float('inf'), distancias))))
    grafo.clear()
    labirinto.clear()