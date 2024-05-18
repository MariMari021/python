#Simulação de um Caixa Eletrônico Este programa simula
#um caixa eletrônico, permitindo que o usuário faça depósitos,
#saques e consulte o saldo da conta, e sair

print('___Bem-vindo ao Bank Simulator___')

saldo = 0
try:
    escolha = input('Escolha a operação que deseja: \nDepósito (1) \nSaque (2) \nSaldo (3) \nSair (4)\n Operação escolhida: ')

    while escolha != '4':
        if escolha == '1':
          deposito =  float(input('Digite o valor do depósito: '))
          if deposito >= 0:
              saldo += deposito
              print(f'Esse é o seu novo saldo {saldo} e esse é o valor do depósito {deposito}')
              escolha = input('Escolha a operação que deseja: \nDepósito (1) \nSaque (2) \nSaldo (3) \nSair (4)\n Operação escolhida:  ')
          else:
            print('Digite apenas valores positivos!')


        elif escolha == '2':
            saque = float(input('Digite o valor do saque: '))
            if saque >= 0:
                saldo = saldo - saque
                print(f'Esse é o seu novo saldo {saldo} e esse é o valor do saque {saque}')
                escolha = input('Escolha a operação que deseja: \nDepósito (1) \nSaque (2) \nSaldo (3) \nSair (4)\n Operação escolhida:  ')
            else:
                print('Digite apenas valores positivos!')

        elif escolha == '3':
            print(f'Esse é o seu saldo:{saldo}')
            escolha = input('Escolha a operação que deseja: \nDepósito (1) \nSaque (2) \nSaldo (3) \nSair (4)\n Operação escolhida:  ')

        else:
            print('Digite os valores correspondentes as operações!')
            escolha = input('Escolha a operação que deseja: \nDepósito (1) \nSaque (2) '
                            '\nSaldo (3) \nSair (4)\n Operação escolhida:  ')
except ValueError:
    print('Insira os valores correspondentes as operações! ')