class ContaBancaria:
    """
Cria uma conta bancária e permite fazer saques de depósitos
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f"Conta {self.id} criada com sucesso. Saldo atual de R${saldo:,.2f}")

    def __str__(self):
        return f"Conta {self.id} de {self.titular} com saldo de R${self.saldo:,.2f}"

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:,.2f} autorizado na conta {self.id}")

    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Saque negado de R${valor:,.2f} na conta {self.id}. SALDO INSUFICIENTE")
        self.saldo -= valor
        print(f"Saque de R${valor:,.2f} autorizado na conta {self.id}")

c1 = ContaBancaria(1, "João", 1000)
c1.depositar(500)
c1.sacar(3000)
print(c1)