#Escreva um programa que peça ao usuário para adivinhar um número entre 1 e 10
# e continue pedindo até que o usuário acerte o número.
# E no final, retorne também a quantidade de tentativas necessárias.

import random

contador = 0
numero = random.randint(1,10)
numero_pessoa = int(input('Tente adivinhar o número sorteado entre 1 e 10: '))
print(numero)
while numero_pessoa != numero:
    numero_pessoa = int(input('Tente adivinhar o número sorteado entre 1 e 10: '))
    contador += 1
'''

#prof

import random
pc = random.randint(1,10)
escolha = ''
contador = 0

while pc != escolha:
    escolha = int(input('Digite seu palpite: '))
    contador += 1

    print(f'Acertou, {contador} vezes necessário')'''