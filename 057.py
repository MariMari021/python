#Faça um programa com uma função maior e menor, que leia uma lista
#com 5 valores informados pelo usuário e retorne esses valores e a posição deles

def programaMax(idade):
    return max(idade), idade.index(max(idade)) + 1

def programaMin(idade):
    return min(idade), idade.index(min(idade)) + 1

try:
    idades = []
    for ele in range(5):
        idades.append(int(input('Digite um valor: ')))

    maior_valor, posicao_maior = programaMax(idades)
    menor_valor, posicao_menor = programaMin(idades)

    print(f'O maior valor é {maior_valor} e a sua posição é {posicao_maior}.'
          f'\nO menor valor é {menor_valor} e a sua posição é {posicao_menor}')
except ValueError as e:
    print(f"Erro: Insira apenas números inteiros.")


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

'''