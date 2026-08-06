from frete import *
from rich.console import Console
from rich.table import Table

console = Console()

def main():
    dist = 5

    viagem = [
        Moto(dist),
        Caminhao(dist),
        Drone(dist)
    ]

    tabela = Table(title="Simulação de Fretes")

    tabela.add_column("Veículo", justify="left", style="cyan", no_wrap=True)
    tabela.add_column("Distância", justify="center", style="magenta")
    tabela.add_column("Valor / Status", justify="left", style="green")

    for entrega in viagem:
        nome_veiculo = type(entrega).__name__
        resultado = entrega.calcular_frete()
        
        if isinstance(resultado, (int, float)):
            texto_resultado = f"R$ {resultado:.2f}"
        else:
            texto_resultado = f"[red]{resultado}[/red]"

        tabela.add_row(nome_veiculo, f"{dist} Km", texto_resultado)

    console.print(tabela)

if __name__ == "__main__":
    main()