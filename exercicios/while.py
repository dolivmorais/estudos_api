# crie um sistema de cadastro
# venda = input("Informe um produto. Para cancelar aperte ENTER na caixa vazia: ")
# vendas = []

# while venda != '':
#     vendas.append(venda)
#     venda = input("Informe um produto. Para cancelae aperte ENTER na caixa vazia: ")
# print(vendas)

vendas = []

while True:
    produto = input('qual produto: ')
    if not produto:
        break
    qtde = int(input('qual é a quantidade: '))
    vendas.append([produto,qtde])
print(vendas)
