from conta import Conta

conta1 = Conta(10, "Jorge", 100.0, 1000.0)
conta1.extrato()
conta2 = Conta(20, "Mário", 200.0, 1500.0)
conta2.extrato()

conta1.transfere(20, conta2)
conta1.extrato()
conta2.extrato()

