'''

#Calculadora
print(1 + 1)
print(1 - 10)
print(5 + 3)

#String / Texto
print('Meu nome é Mariana')



# Entrada de Dados
N1 = int(input('Digite a sua idade: '))
Idade_Nova = N1 + 1000000
print(f'Sua idade é {Idade_Nova} ')
'''

#Strings
'''
Nome = 'Mariana Gomes'
print(Nome[0])
print(Nome[0:4])
print(Nome[::2])

tamanho = len(Nome)
print(len(Nome))
print(f'A quantidade de l é {Nome.count("i")}')
mai = Nome.upper()
min = Nome.lower()

print(f'{mai} e {min}')

Name = input('Digite seu nome: ').strip()

print(Name)



for contador in range (1, 10):
    print('*'),

for contador in range (1, 10):
    print(contador, end='')
'''
'''
soma = 0
for i in range(1, 11):
    idade = int(input('Digite sua idade: '))
    soma= soma + idade
    print(soma)
'''
'''
carro = ['Ferrari', 'Vermelho', '2024']
print(carro)
carro.append('OI')
print(carro)
carro.pop(0)
print(carro)
carro.remove('OI')
print(carro)

idades = [1,2,3,4,5,6,7]
print(max(idades))
print(min(idades))
print(len(idades))
print(sorted(idades))
print(sum(idades)/len(idades))

for ele in range(3):
    idades.append(int(input('Digite uma idade: ')))

'''
'''
#listas aninhadas


lista = []
lista_auxiliar_nome = []
lista_auxiliar_idade = []

for ele in range(3):
    lista_auxiliar_nome.append(input('Nome: '))
    lista_auxiliar_idade.append(int(input('Idade: ')))
    #lista principal
lista.append(lista_auxiliar_nome[:])
lista.append(lista_auxiliar_idade[:])

print(lista)



lista = []
lista_auxiliar = []



for ele in range(3):
    lista_auxiliar.append(input('Nome: '))
    lista_auxiliar.append(int(input('Idade: ')))
    #lista principal
    lista.append(lista_auxiliar[:])
    lista_auxiliar.clear()

print(lista)
print(lista[0][1])'''


#dicionários

cadastro = {'nome': 'Mariana', 'Idade': 25}

print(cadastro['nome'])
print(cadastro.values())
print(cadastro.keys())
print(cadastro.items())

for chave in cadastro:
    print(cadastro[chave])

for chave, valor in cadastro.items():
    print(chave)

#composto

cadastro = {'Nomes': ['a', 'b', 'c'],
            'Idade': [10, 20, 30]}


print(cadastro['Idade'])
print(max(cadastro['Idade']))