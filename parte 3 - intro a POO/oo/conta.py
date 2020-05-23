class Conta:            
    # função abaixo é executada na criação de um objeto, construtor
    def __init__(self, numero, titular, saldo, limite):
        # se criar método passando limite=1000.0 esse será o valor padrão. Então pode ser criado o objeto sem essa informação, que ele já terá o valor padrão
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo+=valor
        print("valor adicionado a conta")

    def saca(self, valor):
        self.__saldo-=valor
        print("valor retirado da conta")

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite=limite

    # a palavra chave pass serve para fazer esse código funcionar
    pass

