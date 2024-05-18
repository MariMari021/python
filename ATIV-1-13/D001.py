#Escreva um programa que execute o cálculo da Função horária da posição no MRUV, e
# retorne de acordo com o tempo informado pelo usuário

print('----- Calcule a Função horária da posição no MRUV -----')

try:
    inicial = float(input('Qual é a posição inicial (m/s)? '))
    velocidade = float(input('Qual é a velocidade inicial? '))
    tempo = float(input('Qual é o tempo (s)? '))
    aceleração = float(input('Qual é a aceleração? '))

    resultado = inicial + velocidade * tempo + ((aceleração * (tempo ** 2)) / 2)

    print(f'A posição do objeto no tempo {tempo} é de {resultado}')

except ValueError:
    print("Erro: Insira apenas valores numéricos.")


