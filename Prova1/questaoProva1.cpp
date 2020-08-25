#include <set>

int numCaminhosDistintos(const vector<vector<int> > &listaAdjacencia, int x, int y) {
    
    vector<bool> visitado(listaAdjacencia.size(), false);
    int caminhos = 0;

    set<int> fila;
    fila.push_back(x);
    visitado[x] = true;

    while (!fila.empty()) {
        int s = list.front()

        for (int v = 0; v < listaAdjacencia[s].size(); v++) {
            if (v == y)
                ++caminhos;
            
            if (!visitado[v]) {
                visitado[v] = true;
                fila.push_back(v);
            }
        }
    }

    return caminhos;
}