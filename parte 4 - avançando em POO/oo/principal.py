from filme import Filme
from serie import Serie

vingadores=Filme('vingadores, guerra infinita', 2018, 160)
see=Serie('see', 2019, 1)

vingadores.dar_likes()
vingadores.dar_likes()

see.dar_likes()
see.dar_likes()

print('o filme {} tem {} likes'.format(vingadores.nome, vingadores.likes))
print('a série {} tem {} likes'.format(see.nome, see.likes))