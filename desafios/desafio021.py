from rich import print

class Caneta:
    def __init__(self, cor, tampada=True):
        self.cor = cor
        self.tampada = tampada
        if cor == "azul":
            self.cor = "blue"
        elif cor == "vermelha":
            self.cor = "red"
        elif cor == "verde":
            self.cor = "green"

    def destampar(self):
        # Se a caneta não chamar a função destampar, ela não poderá escrever.
        self.tampada = False

    def escrever(self, texto):
        if self.tampada:
            print(f"A [{self.cor}]caneta[/{self.cor}] está tampada.")
            return
        self.texto = texto
        print(f"[{self.cor}]{self.texto}[/{self.cor}]")

    def quebrar_linha(self, quantidade):
        for _ in range(quantidade):
            print()

    

c1 = Caneta("azul")
c2 = Caneta("vermelha")
c3 = Caneta("verde")

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("Olá, tudo bem?")
c1.quebrar_linha(2)
c2.escrever("Fala ratão!")
c3.escrever("Top né?")