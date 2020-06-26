'''
Disciplina:
	GCC218 - Algoritmo em Grafos

Integrantes: 
	Igor Antônio dos Santos Alves Mendes
	Isaías Gonçalves Ribeiro
	Pedro Antônio de Souza

Nome do Exercício:
	Domino - 2585

Estratégia Adotada:
	Criamos 9 vértices para representar as enumerações possíveis das extremidades
	das peças do dominó. Assim, modelamos um grafo direcionado com arcos representando
	as peças restantes, isto é, para toda peça com enumeração i e j, haverá um arco 
	ligando os vértices i e j. É importante notar que grafo poderá ser desconexo.
	Com o grafo modelado, aplicamos uma busca em profundidade em todas as componentes conexas
	e armazenamos em um vector o maior caminho percorrido (em número de arestas) em cada componente.
	Após a execução da DFS em todas as componetes, verificamos qual é o maior caminho percorrido e
	essa será a solução do problema.
'''
qtd_arestas_percorridas = int()  # Armazenará a quantidade de arestas percorridas em cada busca em profundidade.
grafo = list(list())  # Matriz de adjacência
maiores_caminhos = list()  # Armazenará os maiores caminhos percorridos, em número de arestas, em cada componente conexa.
caminho = list()  # Irá funcionar como uma pilha para realizar o retorno ao vértice pai na busca em profundidade
arestas_visitadas = list()  # Armazena as arestas visitadas

# Função que verifica se aresta já foi visitada
def foi_visitado(aresta) -> bool:
    global arestas_visitadas
    return aresta in arestas_visitadas

# Encontra o pirmeiro filho (caso exista) alcançável, isto é, um filho cuja aresta (pai, filho) ainda não foi visitada.
def encontra_filho (pai:int) -> int:
    global grafo
    for filho in range(len(grafo[pai])):
        if grafo[pai][filho] and not foi_visitado((pai,filho)):
            return filho
    return -1

# Executa busca em profundidade armazenando a quantidade de arestas percorridas até encontrar um vértice "folha".
def busca_em_profundidade (vertice:int):
    global qtd_arestas_percorridas, arestas_visitadas, caminho, maiores_caminhos
    filho = encontra_filho(vertice)

    # Caso encontre um filho
    if filho != -1:
        qtd_arestas_percorridas += 1
        arestas_visitadas.append((vertice, filho))
        caminho.append(vertice)
        busca_em_profundidade(filho)
    # Caso não haja filhos, porém a pilha de vértices visitados ainda não está vazia
    elif len(caminho) > 0:
        pai = caminho.pop()
        maiores_caminhos.append(qtd_arestas_percorridas)
        qtd_arestas_percorridas -= 1
        busca_em_profundidade(pai)

# Loop infinito que só deve parar quando for lançada a exceção EOFError, ou seja, quando alcançar o fim do arquivo.
while True:
    try:
        # N é a quantidade de peças restantes
        N = int(input())

        # Inicializa a matriz de adjacência com False em todas as posições 
        grafo = [[False for _ in range(10)] for _ in range(10)]

        # Recebe as peças restantes e define adjacências na matriz.
        for i in range(N):
            entrada = input().split()
            A = int(entrada[0])
            B = int(entrada[1])
            grafo[A][B] = True

        # Percorre todos os vértices executando a busca em profundidade.
        # Isso é feito para assegurar que todas as componentes conexas sejam visitadas.
        for vertice in range(10):
            arestas_visitadas.clear()
            qtd_arestas_percorridas = 0
            busca_em_profundidade(vertice)

        # Imprime o maior caminho (em número de arestas) encontrado.
        print(max(maiores_caminhos))
        
        # Limpa as listas para o próximo caso de teste.
        arestas_visitadas.clear()
        grafo.clear()
        maiores_caminhos.clear()

    # Ao atingir o final do arquivo, o loop é parado.
    except EOFError:
        break