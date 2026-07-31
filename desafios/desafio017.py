from rich import print

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        print(f"Produto: [bold green]{self.nome}[/bold green] - Preço: [bold blue]R${self.preco:,.2f}[/bold blue]")


p1 = Produto("Ventilador", 16)
p2 = Produto("Geladeira", 2000)

p1.etiqueta()
p2.etiqueta()