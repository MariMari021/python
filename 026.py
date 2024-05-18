#Crie um programa para analisar o IMC de uma pessoa, e
#classifique se ela está entre a faixa ideal, acima ou abaixo do IMC ideal.

try:
    peso = float(input('Qual é o seu peso? '))
    alto = float(input('Qual é a sua altura? '))

    imc = peso / (alto ** 2)

    if imc < 18.5:
        print(f'Abaixo do peso ideal.')
    elif 18.5 <= imc <= 24.9:
        print(f'Peso ideal.')
    else:
        print(f'Acima do peso ideal.')

except ValueError:
    print("Por favor, insira um valor numérico.")


