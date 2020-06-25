#include <iostream> //Biblioteca padrão c++
#include <vector> //Biblioteca para trabalhar com lista(vetor) mais facilmente no c++
#include <stack> //Biblioteca para trabalhar com pilha mais facilmente no c++
#include <set> //Biblioteca para trabalhar com conjuntos mais facilmente no c++
#include <algorithm> //Biblioteca para facilitar operações de intervalos de elementos
using namespace std; 

int arestaAtual=0; //Inicio
vector<vector<bool>> grafo; //Definido o grafo, no caso uma matriz, pois vector de vector é matriz, do tipo bool
vector<int> resultados; //Uma vetor do resultado
stack<int> caminho; //A pilha para empilhar os caminhos
set<pair<int,int>> visitado; //Conjunto de dois valores para saber se foi visitado ou não

// verifica se a aresta foi visitada
bool foiVisitado(pair<int,int> aresta){
  	if(visitado.find(aresta) != visitado.end() ) return true;
  	else return false;	
}

// pega o primeiro vertice que possua um caminho válido
int filho(int pai){
	for(int cont=0; cont < grafo[pai].size(); cont++){
		if(grafo[pai][cont] && ! foiVisitado({pai,cont})) return cont;
	}
	
	return -1;
}

// executa a busca em profundidade contando as arestas
void buscaEmProfundidade(int verticeAtual){
	int verticeFilho = filho(verticeAtual);
	
	// se tem filho vai
	if(verticeFilho != -1){
		arestaAtual++;
		visitado.insert({verticeAtual,verticeFilho});
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
        //max_element é da Biblioteca Algorithm
		cout << *max_element(resultados.begin(), resultados.end() ) << endl;
		
		// fazendo a limpa, para a proxima iteração
		grafo.clear();
		resultados.clear();
		visitado.clear();
	}
	
	return 0;
	
}