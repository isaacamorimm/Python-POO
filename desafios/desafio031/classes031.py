class Retangulo:
    def __init__(self, base, altura):
        self._base = base
        self._altura = altura
        self._area = base * altura

    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, valor):
        if valor <= 0:
            raise ValueError("A base deve ser maior que 0!")
        self._base = valor

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        if valor <= 0:
            raise ValueError("A altura deve ser maior que 0!")
        self._altura = valor

    @property
    def area(self):
        return self._base * self._altura
    
    @property
    def medidas(self):
        return f"Base: {self._base}\nAltura: {self._altura}\nArea: {self._area}"
    
    @medidas.setter
    def medidas(self, medidas):
        base, altura = medidas
        self.base = base
        self.altura = altura
        self._area = base * altura
