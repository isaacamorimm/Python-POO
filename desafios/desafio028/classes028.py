class Termostato():
    def __init__(self, temperatura = 16):
        self.__temperatura = temperatura

    # O valor não pode ser ajustado além de números inteiros e com .5 no final, caso seja diferente, da erro.
    @property
    def temperatura(self): # Getter
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor): # Setter
        if not isinstance(valor, (int, float)):
            raise TypeError("A temperatura deve ser um número.")
        if valor % 0.5 != 0:
            raise ValueError(f"A temperatura de {valor}°C é inválida.")
        if 16 <= valor <= 30:
            self.__temperatura = valor
        else:
            if valor < 16:
                self.__temperatura = 16
            else:
                self.__temperatura = 30

    # Exibir temperatura em Celsius no inspect
    @property
    def ftemperatura(self):
        return f"{self.__temperatura}°C"
        
