#Escreva um programa que leia o peso de 7 pessoas, e no final,
# mostre qual foi o maior e o menor peso lidos


maior_peso = 0

for i in range(1, 8):
   peso = int(input('Digite seu peso: '))

   if peso > maior_peso:
      maior_peso = peso

   if i == 1:
      peso_ref = peso

   if peso < peso_ref:
      menor_peso = peso

print(f'o menor peso é {menor_peso} e o maior peso é {maior_peso}')

'''  RESOLUÇÃO PROFESSOR

maior = None
menor = None

for i in range(0, 7):
    peso = float(input('Digite seu peso: '))

    #solução 1
    if maior == None and menor == None:
        maior = peso
        menor = peso

    #solução 2
    if i == 0:
        maior = peso
        menor = peso
        
    #continuação das duas soluções
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso



print(f'O maior peso é {maior}'
      f'\nO menor peso é {menor}')
'''