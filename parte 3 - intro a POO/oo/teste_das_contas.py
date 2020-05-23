from conta import Conta

Conta.codigo_banco()
Conta.codigos_bancos()

conta1 = Conta(10, "Jorge", 100.0, 1000.0)
conta1.extrato()
conta1.saca(5000)
conta2 = Conta(20, "Mário", 200.0, 1500.0)
conta2.extrato()

conta1.transfere(4000, conta2)
conta1.transfere(20, conta2)
conta1.extrato()
conta2.extrato()

