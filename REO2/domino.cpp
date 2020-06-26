/*
Disciplina:
	Algoritmo em Grafos - GCC218

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

*/
#include <iostream> //Biblioteca padrão c++
#include <vector> //Biblioteca para trabalhar com lista(vetor) mais facilmente no c++
#include <stack> //Biblioteca para trabalhar com pilha mais facilmente no c++
#include <set> //Biblioteca para trabalhar com conjuntos mais facilmente no c++
#include <algorithm> //Biblioteca para facilitar operações de intervalos de elementos
using namespace std; 

int arestaAtual=0; //Inicio
vector<vector<bool > > grafo; //Definido o grafo, no caso uma matriz, pois vector de vector é matriz, do tipo bool
vector<int> resultados; //Uma vetor do resultado
stack<int> caminho; //A pilha para empilhar os caminhos
set<pair<int,int > > visitado; //Conjunto de dois valores para saber se foi visitado ou não

// verifica se a aresta foi visitada
bool foiVisitado(pair<int,int> aresta){
	return (visitado.find(aresta) != visitado.end());
}

// pega o primeiro vertice que possua um caminho válido
int filho(int pai){
	for(int _filho=0; _filho < grafo[pai].size(); _filho++){
		if(grafo[pai][_filho] && ! foiVisitado(make_pair(pai,_filho))) 
			return _filho;
	}
	return -1;
}

// executa a busca em profundidade contando as arestas
void buscaEmProfundidade(int verticeAtual){
	int verticeFilho = filho(verticeAtual);
	
	// se tem filho vai
	if(verticeFilho != -1){
		arestaAtual++;
		visitado.insert(make_pair(verticeAtual,verticeFilho));
		caminho.push(verticeAtual);
		buscaEmProfundidade(verticeFilho);
		
	// se nao é orfão, volta
	}else if(!caminho.empty()){
		int pai = caminho.top();
		caminho.pop();
		resultados.push_back(arestaAtual);
		arestaAtual--;
		buscaEmProfundidade(pai);
	}
}


int main(){
	int N;
	while(cin >> N){ //Numero de peças restantes
		// constroi o grafo
		for(int cont=0; cont < 10; cont++){
			grafo.push_back(vector<bool>(10,false)); //inicializa a matriz de adjacencia em false
		}

		//Popula o grafo
		//Matriz de adjacência
		for(int cont=0; cont < N; cont++){
			int A, B;
			cin >> A >> B;
			grafo[A][B] = true; //define adjacencias baseada nas peças do domino
		}

		// devido ao grafo poder ser desconexo, precisamos garantir 
		// que todos vertices vão ser visistados
		for(int cont=0; cont < 10; cont++){
			visitado.clear();
			arestaAtual = 0;
			buscaEmProfundidade(cont);	
		}
        //max_element é da Biblioteca Algorithm que pega o maior numero da lista
		cout << *max_element(resultados.begin(), resultados.end() ) << endl;
		
		// fazendo a limpa, para a proxima iteração
		grafo.clear();
		resultados.clear();
		visitado.clear();
	}
	
	return 0;
	
}