#Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
#mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores

contador = 0
resposta = 'S'
soma = 0
maior = None
menor = None

while resposta != 'N':
    valor = int(input('Insira um número: '))
    if maior == None and menor == None:
        maior = valor
        menor = valor

    if valor > maior:
        maior = valor

    if valor < menor:
        menor = valor

    contador +=1
    soma += valor
    resposta = input('Deseja continuar? [S/N] ->').strip().upper()


media = soma /contador
print(f'A média é {media}, o maior valor é {maior} e o menor valor é {menor}')