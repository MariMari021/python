#Crie um arquivo .py com todas as operações matemáticas, que
# receba valores, desempacote e return

from importar import soma
from importar import subtracao
from importar import multi
from importar import divisao

from importar import somaMais
from importar import multiMais
from importar import divisaoMais

print(F'A soma de 2 + 4 é: {soma(2, 4)}')
print(f'A subtração de 6 - 4 é: {subtracao(6, 4)}')
print(f'A multiplicação de 8*6 é: {multi(8, 6)}')
print(f'A divisão de 456/6 é: {divisao(456, 6)}')

print('----- Funções feitas com *numeros -----')
print(F'A soma de 2 + 4 é: {somaMais(2, 4)}')
print(f'A multiplicação de 8*6 é: {multiMais(8, 6)}')
print(f'A média de 456 e 6 é: {divisaoMais(456, 6)}')