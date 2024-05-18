#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas minúsculas
#Quantas letras ao todo (sem considerar os espaços)
#Quantas letras tem o primeiro nome

print('----- Conheça mais sobre o seu nome! -----')

try:
      nome_completo = input('Insira seu nome completo: ').strip()
      if not nome_completo.isalpha():
            print('Insira apenas letras.')
      else:
            min = nome_completo.lower()
            max = nome_completo.upper()
            print(f'{min}\n{max}')

            # Calcula o número total de letras (sem considerar os espaços)
            total_letras = len(nome_completo.replace(" ", ""))
            print(f'O tamanho do nome inserido é {total_letras}')

            # Divide o nome completo em partes e pega o primeiro nome
            nome_completo_split = nome_completo.split()
            primeiro_nome = nome_completo_split[0]
            print(f'O primeiro nome tem {len(primeiro_nome)} letras')

except IndexError:
      print("Erro: O nome completo deve conter pelo menos um nome.")