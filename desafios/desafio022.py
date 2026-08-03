from rich import print
from rich import panel as Panel

class ControleRemoto:
    canal_min: int = 1
    canal_max: int = 6
    volume_min: int = 1
    volume_max: int = 5
    def __init__(self, canal = 1, volume = 1):
        self.canal_atual: int = canal
        self.volume_atual: int = volume
        self.ligado:bool = False

    def mostrar_tv(self):
        conteudo = ''
        if not self.ligado == False:
            conteudo = f":prohibited: [red]A TV está desligada[/red]"
        else: 
            conteudo = f"CANAL e VOLUME"


    tv = Panel(conteudo, title="TV")
    print(tv)

c = ControleRemoto()
c.liga_desliga()
c.mostrar_tv()
