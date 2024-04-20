#Crie um programa que retorne a tabuada de um número, e só pare quando o número digitado for 0000


parar = '0000'
while True:
    numero = input('Digite um número: ')

    if numero == parar:
        break
    for ele in range(1, 11):
        print(f'{int(numero)} X {ele} = {int(numero) * ele}')

