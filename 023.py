#Escreva um programa que peça ao usuário uma palavra e
# imprima se começa com vogal ou consoante.

try:
    usuario = input('Insira uma palavra: ').strip().lower()

    if usuario[0] in 'aeiou':
        print(f'A palavra começa com uma vogal!')
    else:
        print(f'A palavra começa com uma consoante!')

except IndexError:
    print("Erro: A caixa de entrada está vazia, insira um dado válido!")