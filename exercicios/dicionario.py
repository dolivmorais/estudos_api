'''
faça um programa que leia nome e media de um aluno,
guarde tambem a situação em um dicionario. no final
mostre o conteudo da estrutura na tela
'''
# aluno = dict()
# aluno['nome'] = str(input('Nome: '))
# aluno['media'] = float(input(f'média de {aluno["nome"]}: '))
# if aluno['media'] >= 7:
#     aluno['situacao'] = 'aprovado'
# elif 5 <= aluno['media'] < 7:
#     aluno['situacao'] = 'recuperacao'
# else:
#     aluno['situacao'] = 'reprovado'

# for k,v in aluno.items():
#     print(f'>> {k} {v}')

'''
crie um programa onde 4 jogadores joguem um dado e tenham resultados
aleatorios. guarde esses resultados em um dicionario, coloque em ordem,
sabendo que o vencedor tirou o maior numero no dado
'''

from random import randint
from time import sleep
from operator import itemgetter

jogo = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)}

ranking = list()

# for k,v in jogo.items():
#     print(f'>> {k} {v}')
#     sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('---' * 30)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar:{v[0]} com {v[1]}')
    sleep(1)

