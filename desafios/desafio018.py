class Churrasco:
    def __init__(self, titulo, quant, cons = 0.400, kgp = 82.40 ):
        self.titulo = titulo
        self.cons = cons
        self.kgp = kgp
        self.quant = quant
        print(f"Analisando {self.titulo} com {self.quant} convidados")

    def analisar(self):
        print(f"Recomendo comprar {self.quant * self.cons:.2f} Kg de carne")
        print(f"O custo total será de {self.quant * self.cons * self.kgp:.2f} reais")
        print(f"Cada pessoa pagará {self.quant * self.cons * self.kgp / self.quant:.2f} reais")

c1 = Churrasco("Truco, Cerveja e Churrasco", 3)
c1.analisar()