 # Declaração de Classe

class Gafanhoto:
    def __init__(self): # Método Construtor
        # Atributos de Instância
        self.nome = ""
        self.idade = 0

    # Métodos de Instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é um gafanhoto de {self.idade} anos de idade."

# Declaração de Objeto
g1 = Gafanhoto()
g1.nome = "João"
g1.idade = 5
g1.aniversario()
print(g1.mensagem())

 