from ListaDeCompra import ListaDeCompra
from dado.Mercado import Mercado
from dado.Produto import Produto
from dado.Marca import Marca
from dado.Item import Item

mercados = []
mercados.append(Mercado(1, "BH"))
mercados.append(Mercado(2, "Rex"))

produtos = []
produtos.append(Produto(1, "Arroz 5 KG"))
produtos.append(Produto(2, "Feijão 1 KG"))
produtos.append(Produto(3, "Amaciante 2 L"))
produtos.append(Produto(4, "Farinha"))

marcas = []
marcas.append(Marca(1, "Tio João"))
marcas.append(Marca(2, "Prato Fino"))
marcas.append(Marca(3, "Rex"))
marcas.append(Marca(4, "Urbano"))
marcas.append(Marca(5, "Kicaldo"))
marcas.append(Marca(6, "BH"))
marcas.append(Marca(7, "Confort"))

itens = []
itens.append(Item(mercados[0], produtos[0], marcas[0], 18.90))
itens.append(Item(mercados[0], produtos[0], marcas[1], 19.90))
itens.append(Item(mercados[1], produtos[0], marcas[1], 19.90))
itens.append(Item(mercados[1], produtos[0], marcas[2], 14.90))

itens.append(Item(mercados[0], produtos[1], marcas[3], 7))
itens.append(Item(mercados[0], produtos[1], marcas[4], 8))
itens.append(Item(mercados[1], produtos[1], marcas[3], 7))
itens.append(Item(mercados[1], produtos[1], marcas[4], 9))

itens.append(Item(mercados[0], produtos[2], marcas[5], 8))
itens.append(Item(mercados[0], produtos[2], marcas[6], 10))
itens.append(Item(mercados[1], produtos[2], marcas[6], 11))

lista = ListaDeCompra(produtos)

for item in itens:
    lista.adicionar_item(item)

lista.gerar_lista()
lista.imprimir_lista()
