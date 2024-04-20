#Crie um programa que leia um nome, e mostre o
# primeiro e o último nome

Nome = input('Digite seu nome completo:')
separar = Nome.split()
'''
quant = len(separar)-1
primeiro_nome = separar[0]
ultimo_nome = separar[quant]
print(f'Entrada: {Nome}'
      f'\nPrimeiro nome: {primeiro_nome}'
      f'\nÚltimo nome: {ultimo_nome}')
'''
#solucao2

quant_nome = len(separar)
print(separar[quant_nome -1])