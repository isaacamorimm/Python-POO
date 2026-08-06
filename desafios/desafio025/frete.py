from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, distancia, fator):
        self.distancia = distancia
        self.fator = fator

    @abstractmethod
    def calcular_frete(self) -> float:
        pass

class Moto(Transporte):
    def __init__(self, distancia, fator=0.50):
        super().__init__(distancia, fator)

    def calcular_frete(self):
        return self.distancia * self.fator

class Caminhao(Transporte):
    def __init__(self, distancia, fator=1.20):
        super().__init__(distancia, fator)

    def calcular_frete(self):
        if self.distancia < 50:
            return "Raio mínimo de 50 Km"
        else:
            return self.distancia * self.fator

class Drone(Transporte):
    def __init__(self, distancia, fator=9.50):
        super().__init__(distancia, fator)

    def calcular_frete(self):
        if self.distancia > 10:
            return "Raio máximo de 10 Km"
        else:
            return self.distancia * self.fator