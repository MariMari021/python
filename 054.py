#Crie uma tupla preenchida com os 10 filmes mais assistidos de todos os tempos, e depois mostre:

#Apenas os 3 primeiros mais assistidos
#Os últimos 2 mais assistidos
#A lista em ordem alfabética
#Em que posição está “O rei leão”

print('----- Saiba mais sobre os filmes mais assistidos do mundo -----')


filmes = ('Avatar', 'Vingadores: Ultimato', 'Avatar: O Caminho da Água', 'Titanic ', 'Star Wars: O Despertar da Força','Vingadores: Guerra Infinita','Homem-Aranha: Sem Volta Para Casa', 'Jurassic World', 'O Rei Leão','Os Vingadores' )

print('----Os últimos 2 mais assistidos----')
for ele in range(8, 10):
    print(filmes[ele])

print('----Apenas os 3 primeiros mais assistidos----')
for ele in range(0, 3):
    print(filmes[ele])

print('----Ordem alfabética----')
print(sorted(filmes))

print('----Em que posição está “O Rei Leão”----')
print(f'{filmes.index("O Rei Leão") +1}. Rei Leão')