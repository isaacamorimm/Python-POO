from rich import print

class Livro:
    def __init__(self, titulo, pag, pag_atual = 1):
        self.titulo = titulo
        self.pag = pag
        self.pag_atual = pag_atual
        print(f"Você acabou de abrir o livro [bold green]{self.titulo}[/bold green] que tem [bold blue]{self.pag}[/bold blue] páginas no total. Você agora está na página [bold yellow]{self.pag_atual}[/bold yellow]")

    def avancar_paginas(self, pag_avancadas):
        self.pag_atual += pag_avancadas
        if self.pag_atual >= self.pag:
            print(f"Parabéns, você terminou o livro [bold green]{self.titulo}[/bold green]!")
        else:
            print(f"Você avançou {pag_avancadas} páginas e agora está na página [bold yellow]{self.pag_atual}[/bold yellow]")

l1 = Livro("Memórias Póstumas", 20)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(100)
