#Faça um programa que leia o nome e o QI de várias pessoas, guardando tudo e uma lista. No final mostre:

#Quantas pessoas foram cadastradas
#Uma listagem com as pessoas com o maior QI
#Uma listagem com as pessoas de menor QI
'''
lista = []
lista_qi = []
lista_nome = []


for ele in range(5):
    lista_nome.append(input('Nome: '))
    lista_qi.append(int(input('QI: ')))

lista.append(lista_nome[:])
lista.append(lista_qi[:])

def programaMax(qis):
    qis = max(lista_qi)
    return qis

def programaMin(qis):
    qis = min(lista_qi)
    return qis


print(len(lista_nome))
print(programaMax(lista_qi))
print(programaMin(lista_qi))

'''


lista = []
nomes = []
qi = []
while True:
    nome = input('Digite o nome[0 para sair]: ')
    if nome == '0':
        break
    qi.append(int(input('Digite o QI: ')))
    nomes.append(nome)

lista.append(nomes[:])
lista.append(qi[:])

lista_decrescente = sorted(lista[1], reverse=True)
nome_em_ordem_decrescente = []
for ele in lista_decrescente:
    nome_em_ordem_decrescente.append(lista[0][lista[1].index(ele)])

lista_crescente = sorted(lista[1])
nome_em_ordem = []
for ele in lista_crescente:
    nome_em_ordem.append(lista[0][lista[1].index(ele)])

print(f'Quantidade de pessoas {len(lista[0])}'
      f'\nEm ordem decrescente{nome_em_ordem_decrescente}'
      f'\nEm ordem crescente {nome_em_ordem}'
      )