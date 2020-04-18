class Conta:            
    # função abaixo é executada na criação de um objeto, construtor
    def __init__(self, numero, titular, saldo, limite):
        # se criar método passando limite=1000.0 esse será o valor padrão. Então pode ser criado o objeto sem essa informação, que ele já terá o valor padrão
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    
    # a palavra chave pass serve para fazer esse código funcionar
    pass

