#Escreva um programa que converta real para o Franco Congolês

print('----- Converta reais para o franco congoles! -----')

try:
    valor = float(input('Digite o valor a ser convertido: '))
    conversao = valor * 558.33
    print(f'{valor} reais equivalem a {conversao:.2f} Francos Congoleses')
except ValueError:
    print("Insira apenas valores numéricos para o raio.")