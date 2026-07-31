from rich import print
from rich.panel import Panel as panel

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.jogos = []

    def add_favoritos(self, jogos):
        self.jogos.append(jogos)

    def ficha(self):
        print(panel(f"[bold green]Nome:[/bold green] {self.nome}\n[bold blue]Nick:[/bold blue] {self.nick}\n[bold yellow]Jogos Favoritos:[/bold yellow] {', '.join(self.jogos)}", title="[bold red]Ficha do Gamer[/bold red]", subtitle="[bold yellow]End of Ficha[/bold yellow]", expand=False))

j1 = Gamer("Isaac", "MC.ansiedade")
j1.add_favoritos("Minecraft")
j1.add_favoritos("GTA V")

j1.ficha()