# Criação de um Objeto Concreto com características e um Objeto Abstrato

class Carro:
    def __init__(self, nome, cor, tamanho):
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho

    def exibir_caracteristicas(self):
        print(f"Nome: {self.nome}, Cor: {self.cor}, Tamanho: {self.tamanho}")

class Alarme:
    def __init__(self, alarme):
        self.alarme = alarme

    def exibir_alarme(self):
        print(f"Alarme: {self.alarme}")

# Exemplo de uso dos objetos
carro1 = Carro("Fusca", "Azul", "Pequeno")
carro1.exibir_caracteristicas()

alarme1 = Alarme("Ativado")
alarme1.exibir_alarme()
