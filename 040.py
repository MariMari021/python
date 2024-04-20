#Escreva um programa que leia um número n inteiro qualquer e mostra
# na tela os n primeiros elementos de uma Sequência de Fibonacci


numero = int(input('Digite a quantidade de números a serem mostrados: '))

ciclo = 0
ant = 0
atual = 1

while numero > ciclo:
    if ciclo == 0:
        print('0')
    elif ciclo == 1:
        print('1')
    else:
        proximo = ant + atual
        ant = atual
        atual = proximo
        print(proximo)

    ciclo += 1