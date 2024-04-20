#Faça um programa com uma função maior e menor, que leia uma lista
#com 5 valores informados pelo usuário e retorne esses valores e a posição deles
'''
idades = []
for ele in range(5):
    idades.append(int(input('Digite um valor: ')))


def programaMax(idade):
    idade = max(idades)
    return idade

def programaMin(idade):
    idade = min(idades)
    return idade



print(f'O maior valor é {programaMax(idades)} e a sua posição é {idades.index(programaMax(idades)) +1}.'
      f'\n O menor valor é {programaMin(idades)} e a sua posição é {idades.index(programaMin(idades)) +1}')

'''

def maior(valores):
    maior_numero = valores[0]
    for ele in valores:
        if ele > maior_numero:
            maior_numero = ele
    return maior_numero


def menor(valores):
    menor_numero = valores[0]
    for ele in valores:
        if ele < menor_numero:
            menor_numero = ele
    return menor_numero


lista = []

for ele in range(5):
    lista.append(int(input('Digite um número: ')))

print(maior(lista))
print(menor(lista))

