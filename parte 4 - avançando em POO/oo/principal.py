from filme import Filme
from serie import Serie

vingadores=Filme('vingadores, guerra infinita', 2018, 160)
see=Serie('see', 2019, 1)

vingadores.dar_likes()
vingadores.dar_likes()

see.dar_likes()
see.dar_likes()

lista=[vingadores, see]

for programa in lista:
    print(programa)

