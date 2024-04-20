#Escreva um programa que leia 10 número, se for
# ímpar deve ser descartado, se não, deve ser agregado a uma soma
soma = 0
for i in range(1,11):
  numero =  int(input('Digite um número: '))
  if numero % 2 == 0:
      soma = numero + soma
print(soma)
