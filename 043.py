#Crie um programa que leia vários números inteiros. O programa só vai
# parar quando o usuário digitar 0000. No final mostre quantos números
# foram digitados e qual a soma entre eles (desconsiderando o flag)

flag = '0000'
soma = 0
contador = 0
while True:
    numero =input('Digite um número: ')
    if numero != '0000':
        contador += 1
    if numero == flag:
        break
    soma += int(numero)
print(f'A soma é {soma} e a quantidade de números digitados são: {contador}')