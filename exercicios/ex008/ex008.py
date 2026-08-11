class ContaBancaria:
    """
Cria uma conta bancária e permite fazer saques de depósitos
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id # Publico
        self._titular = nome # Protegido
        self.__saldo: int = saldo # Privado
        print(f"Conta {self.id} criada com sucesso. Saldo atual de R${saldo:,.2f}")

    def __str__(self):
        #return f"Conta {self.id} de {self.titular} com saldo de R${self.__saldo:,.2f}"
        return f"Estado atual da conta: {self.__dict__}"

    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f"Depósito de R${valor:,.2f} autorizado na conta {self.id}")

    def sacar(self, valor):
        valor = abs(valor)
        if valor > self.__saldo:
            print(f"Saque negado de R${valor:,.2f} na conta {self.id}. SALDO INSUFICIENTE")
        self.__saldo -= valor
        print(f"Saque de R${valor:,.2f} autorizado na conta {self.id}")

