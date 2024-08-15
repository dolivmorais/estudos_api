# for
# c = 0
# for i in range(5):
#     c += i
#     print(i, c)

# produtos = ['a','b','c','d']
# producao = [10,5,23,6]

# for i in range(len(produtos)):
#    print('{} unidades do produto {}'.format(producao[i],produtos[i]))

# for i in produtos:
#     if i == "a":
#         print("produto encontrado")
#         break
#     else:
#         print("Produto não encontrado")

# valores = [15.99, 8.49, 2.99, 6.79, 8.99, 4.99, 12.49, 9.99, 3.29, 7.99]
# meta = 8
# qtde_lista = len(valores)
# c = 0

# for i in valores:
#     if i >= meta:
#         c += 1

# percentual = c / qtde_lista
# print(qtde_lista)
# print(c)
# print('{:.2%}'.format(percentual))

# produtos_a = ['a','b','c','d']
# producao_a = [10,5,23,6]
# nivel_minimo = 10

# for i,qtde in enumerate(producao_a):
#     if qtde < nivel_minimo:
#         print(produtos_a[i])
#         print(producao_a[i])

# cadastro em lista

# lista = []
# for i in range(2):
#     nome = str(input("Informe o nome: "))
#     idade = int(input("Informe a idade: "))
#     hosp = [nome, 'idade:{}'.format(idade)]
#     lista.append(hosp)
# print(hosp)

# produtos = ["sabonete", "shampoo", "detergente", "esponja de cozinha", "papel toalha"]
# vendas_2020 = [150, 200, 300, 180, 250]
# vendas_2021 = [170, 220, 320, 190, 270]

# for i,produto in enumerate(produtos):
#     if vendas_2021 > vendas_2020:
#         crescimento = vendas_2021[i] / vendas_2020[i] -1
#         print('vendas 2020: {} vendas 2021: {} creciemnto: {:%}'.format(vendas_2020[i],vendas_2021[i],crescimento))

# estoque = [
#     [11, 21, 31, 41, 51, 61],
#     [17, 18, 19, 110, 111, 112],
#     [13, 14, 115, 116, 117, 118],
#     [19, 20, 21, 22, 23, 24],
#     [25, 26, 27, 28, 29, 30]
# ]
# produto = ["sabonete", "shampoo", "detergente", "esponja de cozinha", "papel toalha"]
# nivel_minimo = 20
# lista_baixo_nivel = []

# for i,lista in enumerate(estoque):
#     for qtde in lista:
#         if qtde < nivel_minimo:
#             if produto[i] in lista_baixo_nivel:
#                 pass
#             else:
#                 lista_baixo_nivel.append(produto[i])
# print(lista_baixo_nivel)
 
meta = 1000
c = 0
vendas = [
    ['a',900],
    ['b',1000],
    ['c',1200],
    ['d',1100],
    ['r',1100],
    ['f',800]
    ]

itens_lista = len(vendas)

for i,item in enumerate(vendas):
    if item[1] >= meta:
        c += 1
        #print(i, item)
print(itens_lista)
print(c)
percentual = itens_lista / c - 1
print('{:.0%}'.format(percentual))