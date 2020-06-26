/*
Disciplina:
	Algoritmo em Grafos - GCC218

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
*/
#include <iostream> //Biblioteca padrão c++
#include <vector> //Biblioteca para trabalhar com lista(vetor) mais facilmente no c++
#include <queue>  //Biblioteca para trabalhar com fila mais facilmento no c++
#include <climits> //Bibliotecas para constantes
using namespace std;
typedef pair<int, int> parDeInteiros;

vector<vector<int > > grafo;
vector<int> dist;
int n;
int m;

//Algoritmo de Dijkstra soluciona o problema do caminho mais curto num grafo dirigido ou não dirigido 
//com arestas de peso não negativo, em tempo computacional O(m + n log n) 
//onde m é o número de arestas e n é o número de vértices. 
void dijkstra(int inicial)
{
	int vizinho;
	int verticeAtual;
	dist.clear();
	dist.assign(n * m, INT_MAX);
	dist[inicial] = 0;
	
	//Esta declaração da fila de prioridade garante que o menor elemento sempre
	//estará a frente, pois por padrão é o maior
	priority_queue<parDeInteiros, vector<parDeInteiros>, greater<parDeInteiros> > filaDePrioridade;
	
	//Define a distancia do vértice inicial como 0 e acrescenta na fila de prioridade
	filaDePrioridade.push(parDeInteiros(0, inicial));
	
	//Enquanto a fila não for vazia, tenta relaxar arestas
	while(!filaDePrioridade.empty())
	{
		parDeInteiros v = filaDePrioridade.top();
		verticeAtual = v.second;
		filaDePrioridade.pop();
		for (int i = 0 ; i < grafo[verticeAtual].size(); i++)
		{
			vizinho = grafo[verticeAtual][i];
			if (dist[vizinho] > dist[verticeAtual] + 1)
			{
				//Relaxamento de arestas
				dist[vizinho] = dist[verticeAtual] + 1; 
				filaDePrioridade.push(parDeInteiros(dist[vizinho], vizinho));
			}
		}
	}
}
int main()
{
	vector<string> aux;
	string linha;
	int vertice;
	//ios_base :: sync_with_stdio(0); cin.tie(0);
	while(1)
	{
		cin >> n >> m;
		if (!n && !m) return 0; //Condição de saída do while
		grafo.assign(n * m, vector<int> ());	//O + 2 é para garantir que não acesse possíções indevidas
		for (int i = 0 ; i < n ; i++)
		{
			cin >> linha;
			aux.push_back(linha); //Vetor de string, que é matriz de caracter
		}
		for (int i = 0 ; i < n; i++)
		{
			for (int j = 0; j < m; j++)
			{
				vertice = m*i+j;
				//Calculos para identificar vizinhos
				if (aux[i][j] == '.')
				{
					if (i > 0)
					{
						if (aux[i - 1][j] == '.') //Olha pra cima
						{
							grafo[vertice].push_back(m * (i - 1) + j);
						}
					}
					if (i < n - 1)
					{
						if (aux[i + 1][j] == '.') //Olha pra baixo
						{
							grafo[vertice].push_back(m * (i + 1) + j);
						}
					}
					if (j > 0)
					{
						if (aux[i][j - 1] == '.') //Olha pra esquerda
						{
							grafo[vertice].push_back(m * i + j - 1);
						}
					}
					if (j < m - 1)
					{
						if (aux[i][j + 1] == '.') //Olha pra direita
						{
							grafo[vertice].push_back(m * i + j + 1);
						}
					}
				}
			}
		}
		int p;
		//Encontra primeiro vértice que contém vizinhos
		for (p = 0; p < grafo.size(); ++p) 
			if (grafo[p].size()) 
				break;
		dijkstra(p);
		int mx = INT_MIN;
		//Acha a maior distância
		for (int i = 0 ; i < dist.size(); ++i)
		{
			if (dist[i] != INT_MAX && dist[i] > mx) 
			{
				mx = dist[i];
				p = i;
			}
		}
		dijkstra(p);
		mx = INT_MIN;
		//Acha a maior distância
		for (int i = 0 ; i < dist.size(); ++i)
		{
			if (dist[i] != INT_MAX && dist[i] > mx) 
				mx = dist[i];
		}
		cout << mx << '\n';
		grafo.clear();		
		aux.clear();
	}
}