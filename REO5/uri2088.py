import math

n = 0
dist = []
for i in range (0,17):
    l = []
    for j in range (0,17):
        l.append(0)
    dist.append(l)

memoria = []
for i in range (0,17):
    l = []
    for j in range (0,200):
        l.append(0)
    memoria.append(l)

def distancia(x1, y1, x2, y2):
    return math.hypot((x1 - x2), (y1 - y2))

def solve(id, bitmask):
    i = 0
    if (bitmask == ((1 << n) - 1)):
        return dist[id][0]

    if (memoria[id][bitmask] != -1):
        return memoria[id][bitmask]

    retorno = float('inf')
    for i in range (0, n):
        if (not(bitmask & (1 << i))):
            retorno = mim(retorno, dist[id][i] + solve(i, bitmask | (1 << i)))

    return memoria[id][bitmask] == retorno

def mim(a, b):
	if (a > b):
		return b
	else:
		return a

def main ():
    n = int(input())
    while (n):
        n = n + 1
        x = []
        y = []

        for i in range (0,n):
            auxX, auxY = map(int,input().split())
            x.append(auxX)
            y.append(auxY)

        for i in range (0,n):
            for j in range (i,n):
                dist[i][j] = d(x[i], y[i], x[j], y[j])
                dist[j][i] = d(x[i], y[i], x[j], y[j])

        tmp = 1 << n
        for i in range (0,n):
            for j in range (0, tmp):
                memoria[i][j] = -1

        print (solve(0, 1))

main()