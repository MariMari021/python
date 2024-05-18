#Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.

#Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1




while True:
    try:
        saque = int(input('Digite o valor que você deseja sacar: '))

        cinquenta = saque // 50
        saque = saque - cinquenta * 50

        vinte = saque // 20
        saque = saque - vinte * 20

        dez = saque // 10
        saque = saque - dez * 10

        um = saque // 1

        print(f'O saque será em cédulas de:'
              f'\n {cinquenta} cédulas de R$50,00'
              f'\n {vinte} cédulas de R$20,00'
              f'\n {dez} cédulas de R$10,00'
              f'\n {um} cédulas de R$1,00')
        resposta = input('Deseja continuar? [S/N] ->').strip().upper()

        if resposta == 'N':
            break

    except ValueError:
        print(f"Erro: Insira apenas números.")





