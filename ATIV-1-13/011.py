#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas minúsculas
#Quantas letras ao todo (sem considerar os espaços)
#Quantas letras tem o primeiro nome


nome_completo = input('Insira seu nome completo: ').strip()
min = nome_completo.lower()
max = nome_completo.upper()
print(f'{min}'
      f'\n{max}')
print(f'O tamanho do nome inserido é {len(nome_completo.replace(" ", ""))}')
nome_completo = nome_completo.split()
primeiro_nome = nome_completo[0]
print(f'O primeiro nome tem {len(nome_completo[0])}')