from filme import Filme
from serie import Serie
from playlist import Playlist

vingadores_g_i=Filme('vingadores, guerra infinita', 2018, 160)
vingadores_u=Filme('vingadores, ultimato', 2019, 182)

see=Serie('see', 2019, 1)
the_morning_show=Serie('the morning show', 2019, 1)

vingadores_g_i.dar_likes()
vingadores_g_i.dar_likes()

vingadores_u.dar_likes()
vingadores_u.dar_likes()

see.dar_likes()
see.dar_likes()

the_morning_show.dar_likes()
the_morning_show.dar_likes()

lista=[vingadores_g_i, vingadores_u, see, the_morning_show]
minha_playlist = Playlist('fim de semana', lista)

for programa in minha_playlist:
    print(programa)

print('tamanho: {}'.format(len(minha_playlist)))

