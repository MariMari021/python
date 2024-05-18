#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6
# números entre 1 a 60 para cada jogo, cadastrando tudo em uma lista composta

print('----- Gerador de Palpites Simulator -----')

try:
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

except ValueError:
    print(f"Erro: Insira apenas valores inteiros.")
'''

import random
bolao = []
bolinho = []

try:
    quant_jogos = int(input('Digite a quantidade de jogos que deseja: '))

    for i in range(quant_jogos):
        for i in range(6):
            aleatorio = random.randint(1,60)
            while aleatorio in bolinho:
                aleatorio = random.randint(1,60)

            bolinho.append(aleatorio)

        bolao.append(bolinho[:])
        bolinho.clear()

    for jogo in bolao:
        print(sorted(jogo))

except:
    print('ERRO')

'''