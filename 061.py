#Escreva um programa que crie uma lista vazia e permita que o usuário insira números
# nessa lista até que ele digite um número negativo. Em seguida, exiba a lista na tela.

lista = []

while True:
    try:
        valor = int(input('Digite um número: '))
        if valor < 0:
            break
        else:
            lista.append(valor)
    except:
        print('Digite apenas números')

print(lista)