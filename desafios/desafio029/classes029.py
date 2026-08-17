class Diario():
    def __init__(self, senha, segredos = []):
        self.__segredos = segredos
        self.__senha = senha

    @property
    def senha(self):
        raise PermissionError("Ninguém tem permissão de ver a senha")

    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    def escrever(self, msg):
        self.__segredos.append(msg)

    def ler(self, senha = None):
        if self.__senha == senha:
            print("Diário LIBERADO!")
            for i in self.__segredos:
                print(f"- {i}")
        else:
            print("Senha incorreta")