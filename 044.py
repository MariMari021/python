#Crie um programa para jogar par ou ímpar com o usuário,
# e só pare quando perder. Ao final deve mostrar a quantidade de vitórias

print('-------Impar or Par - ProPlayer--------')

import random

soma = 0
contador = 0

while True:
    try:
        usuario = input('Impar ou Par? ').strip().upper()
        valorUsuario = int(input('Digite um valor: '))
        computador = random.randint(0, 9)
        soma = valorUsuario + computador
        if usuario == 'PAR':
            if soma % 2 == 0:
                contador += 1
                print('Você ganhou! Jogue novamente.')
            else:
                print(f'A soma dos valores é {soma} e a quantidade de vitórias é {contador}')
                break

        if usuario == 'ÍMPAR':
            if soma % 2 > 0:
                contador += 1
                print('Você ganhou! Jogue novamente.')
            else:
                print(f'A soma dos valores é {soma} e a quantidade de vitórias é {contador}')
                break
    except ValueError:
        print(f"Erro: Insira valores inteiros.")


'''

import random
vitorias = 0
while True:
    aleatorio = random.randint(1, 10)
    escolha = input('Par ou Impar [P/I]').strip().upper()
    jogada = int(input('Digite sua jogada: '))

    if ((aleatorio + jogada) % 2==0 and escolha == 'P') or (aleatorio + jogada) % 2 != 0 and escolha == 'I':
        print(f'Você ganhou! {aleatorio} + {jogada} = {aleatorio+jogada}')
        vitorias+= 1
    else:
        print(f'Você Perdeu! {aleatorio} + {jogada} = {aleatorio+jogada}'
              f'\nQuantidade de vitorias: {vitorias}')
        break

'''








