#Crie uma calculadora que após ler 3 valores, mostre e opere de acordo com as opções:

#1.	Somar
#2.	Multiplicar
#3.	Maior
#4.	Novos números
#5.	Sair do programa

contador = 0
valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite um valor: '))
valor3 = int(input('Digite um valor: '))
escolha = input('Escolha a operação que deseja: Soma (1), Multiplicação (2), Maior (3), Novos números (4) ou sair do programa (5). ')


while escolha != '5':

    if escolha == '1':
        soma = valor1 + valor2 + valor3
        print(soma)
        escolha = input('Escolha a operação que deseja: Soma (1), Multiplicação (2), Maior (3), Novos números (4) ou sair do programa (5). ')

    if escolha == '2':
        soma = valor1 * valor2 * valor3
        print(soma)
        escolha = input(
            'Escolha a operação que deseja: Soma (1), Multiplicação (2), Maior (3), Novos números (4) ou sair do programa (5). ')

    if escolha == '3':
        if valor1 > valor2 and valor1 > valor3:
            print(valor1)
        if valor2 > valor1 and valor2 > valor3:
            print(valor2)
        if valor3 > valor2 and valor3 > valor1:
            print(valor3)

        escolha = input( 'Escolha a operação que deseja: Soma (1), Multiplicação (2), Maior (3), Novos números (4) ou sair do programa (5). ')

    if escolha == '4':
        valor1 = int(input('Digite um valor: '))
        valor2 = int(input('Digite um valor: '))
        valor3 = int(input('Digite um valor: '))
        escolha = input('Escolha a operação que deseja: Soma (1), Multiplicação (2), Maior (3), Novos números (4) ou sair do programa (5). ')


