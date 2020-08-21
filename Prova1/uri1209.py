while True:
    try:
        entrada = input().split()

        n = int(entrada[0])
        m = int(entrada[1])
        k = int(entrada[2])
        
        lista_de_adjacencia = {}
        visitar = []
        grau = [0]*(n+1)

        for v in range(1, n+1):
            lista_de_adjacencia[v] = []
            visitar.append(v)

        # Define adjacências na matriz e incrementa o grau dos vértices
        for _ in range(m):
            entrada = input().split()

            u = int(entrada[0])
            v = int(entrada[1])

            lista_de_adjacencia[u].append(v)
            grau[u] += 1

            lista_de_adjacencia[v].append(u)
            grau[v] += 1

            if grau[u] >= k:
                try:
                    visitar.remove(u)
                except ValueError:
                    pass

            if grau[v] >= k:
                try:
                    visitar.remove(v)
                except ValueError:
                    pass

        while len(visitar):
            u = visitar.pop()
            for v in lista_de_adjacencia[u]:
                lista_de_adjacencia[v].remove(u)
                grau[v] -= 1
                if v not in visitar and grau[v] < k:
                    visitar.append(v)

            del lista_de_adjacencia[u]
            grau[u] = -1

        if len(lista_de_adjacencia):
            print(*lista_de_adjacencia)
        else:
            print('0')
        
    # Ao atingir o final do arquivo, o loop é parado.
    except EOFError:
        break