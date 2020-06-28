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
        if (self.__pode_saque(valor)):
            self.__saldo-=valor
            print("valor retirado da conta")
        else:
            print("O saque não foi possível pois você não tem dinheiro suficiente")

    def transfere(self, valor, destino):
        if (self.__pode_saque(valor)):
            self.saca(valor)
            destino.deposita(valor)
        else:
            print("A conta de origem não tem dinheiro suficiente")

    def __pode_saque(self, valor):
        return valor<=(self.__saldo+self.__limite)

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

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}

