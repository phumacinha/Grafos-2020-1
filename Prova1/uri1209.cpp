/*
Disciplina:
    GCC218 - Algoritmo em Grafos

Integrantes: 
    Igor Antônio dos Santos Alves Mendes
    Isaías Gonçalves Ribeiro
    Pedro Antônio de Souza

Nome do Exercício:
    1209 - Festas de São Petersburgo

Estratégia Adotada:
    Modelamos um grafo onde vertices e arestas representam, respectivamente,
    pessoas e as relacoes de amizade. Apos preencher a matriz de adjacencia,
    verificamos as pessoas que possuem numero de amizade abaixo de k, i. e.,
    vertices com grau abaixo de k. Adicionamos esses vertices em um vetor
    chamado 'restritos'. Após isso, percorremos esse vetor simulando uma
    remocao dos vertices restritos, atualizando o grau de seus vizinhos e]
    verificando se houve alguma nova restricao. Os vertices que nao foram
    visitados nessa remocao, sao os vertices de pessoas que devem ser
    convidadas. 
*/
#include <iostream> 
#include <vector> 
#include <list>

int main(int argc, char **argv)
{
    int n, m, k;
    int u, v, i;

    // Lê os parametros n, m, k
    while (scanf("%d %d %d", &n, &m, &k) != EOF) {
        // Inicializa a matriz de adjacencia com 0 em todas as posicoes
        std::vector<std::vector<int > > matrizAdj(n, std::vector<int>(n, 0));
        // Inicializa todos os vertices como nao visitados
        std::vector<bool> visitado (n, false);
        // Inicializa o grau de todos os vertices com 0
        std::vector<int> grau (n, 0);


        for (i = 0; i < m; ++i) {
            // Le as relacoes de amizade
            scanf("%d %d", &u, &v);
            // Define adjacencias na matriz
            matrizAdj[u-1][v-1] = matrizAdj[v-1][u-1] = 1;
            // Incrementa o grau dos vertices
            ++grau[u-1], ++grau[v-1];
        }

        // Lista para guardar os vertices restritos
        std::list<int> restritos;
        for (i = 0; i < n; ++i) {
            // Verifica se a pessoa tem menos amizades que k.
            // Se sim, essa pessoa deve ser restrita.
            if (grau[i] < k) {
                restritos.push_back(i);
                visitado[i] = true;
            }
        }

        // Simula remocao dos vertices restritos, atualizando os seus vizinhos.
        while (restritos.size()) {
            u = restritos.front();
            restritos.pop_front();

            // Percorre os vizinhos
            for (i = 0; i < n; ++i) {
                if (matrizAdj[u][i]) {
                    if (!visitado[i] && --grau[i] < k) {
                        restritos.push_back(i);
                        visitado[i] = true;
                    }
                }
            }
        }

        std::vector<int> convidados;
        for (i = 0; i < n; ++i)
            // Verifica os vertices que nao foram visitados, i. e., pessoas que
            // podem ser convidadas.
            if (!visitado[i])
                convidados.push_back(i+1);

        // Imprime os convidados
        if (convidados.size()) {
            for (std::vector<int>::iterator it = convidados.begin() ; it != convidados.end(); ++it) {
                std::cout << *it;
                if (*it != convidados.back())
                    std::cout << " ";
            }
        }
        else
            std::cout << 0;

        std::cout << std::endl;

    }
    return 0;

}