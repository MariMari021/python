#Crie um algoritmo que leia um salário e simule um reajuste positivo de 60%.
print('----- Saiba seu novo salário! -----')
try:
    salario = float(input('Digite seu salário: '))
    reajuste = salario * 1.60
    print(f'O salário de {salario} com o reajuste de 60% será de: {reajuste}')
except ValueError:
    print("Insira apenas valores numérico para o salário.")