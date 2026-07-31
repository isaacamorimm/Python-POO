class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        return f"Olá, sou {self.nome} e sou {self.cargo} do setor de {self.setor} da empresa Curso em Vídeo"

f1 = Funcionario("Isaac", "TI", "Gestor de TI")
print(f1.apresentacao())

f2 = Funcionario("Isaac", "TI", "Gestor de TI")
print(f2.apresentacao())