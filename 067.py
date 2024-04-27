#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6
# números entre 1 a 60 para cada jogo, cadastrando tudo em uma lista composta

palpites = int(input('Quantos palpites você quer gerar? '))
lista = []
jogo = []

import random
for numero in range(palpites):
    for ele in range(6):
        numeros = random.randint(1, 60)
        jogo.append(numeros)
    lista.append(jogo[:])
    jogo.clear()
print(lista)



