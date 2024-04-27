#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta

expressao = input('Digite uma expressão que use parênteses: ')

pilha = []

for caractere in expressao:
    if caractere == '(':
        pilha.append(caractere)
    elif caractere == ')':
        try:
            if pilha[-1] == '(':
                pilha.pop()
            else:
                print('A expressão está incorreta')
                break
        except IndexError:
            print('A expressão está incorreta')
            break

else:
    if len(pilha) == 0:
        print('A expressão está correta')
    else:
        print('A expressão está incorreta')