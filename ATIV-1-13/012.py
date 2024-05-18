#Crie um programa que leia um nome, e mostre o
# primeiro e o último nome

print('----- Saiba seu primeiro e último nome! -----')

try:
    Nome = input('Digite seu nome completo:')
    if not Nome.isalpha():
        print('Insira apenas letras.')
    else:
        separar = Nome.split()
        quant = len(separar) - 1
        primeiro_nome = separar[0]
        ultimo_nome = separar[quant]

        print(f'Entrada: {Nome}'
              f'\nPrimeiro nome: {primeiro_nome}'
              f'\nÚltimo nome: {ultimo_nome}')
except IndexError:
    print("Erro: O nome completo deve conter pelo menos um nome e um sobrenome.")
'''
#solucao2

quant_nome = len(separar)
print(separar[quant_nome -1])'''