 # Declaração de Classe

class Gafanhoto:
    """
Essa classe cria um gafanhoto, que é uma pessoa que tem nome e idade.

Para criar uma nova pessoa, use 
variavel = Gafanhoto(nome, idade)
    """
    def __init__(self, n, i): # Método Construtor
        # Atributos de Instância
        self.nome = n
        self.idade = i

    # Métodos de Instância
    def aniversario(self):
        self.idade += 1

    def __str__(self): # Dunder Methods
        return f"{self.nome} é um gafanhoto de {self.idade} anos de idade."

    def __getstate__(self):
        return f"Estado: nome = {self.nome} ; idade = {self.idade}"

# Declaração de Objeto

g1 = Gafanhoto("João", 5)
g1.aniversario()
#print(g1)
# print(g1.__dict__) 
print(g1.__getstate__()) # Method
print(g1.__class__)

# O getstate e o dict retornam a mensagem em forma de variavel composta, a diferença entre os dois é que o getstate é personalizável

g2 = Gafanhoto("Mauro", 53)
g2.aniversario()
print(g2)

# print(g1.__doc__) # Dunder Attribute