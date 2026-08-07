from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel as Painel

class Funcionario(ABC):
    sal_min = 1612
    inss = 0.925

    def __init__(self, nome, sal_bruto=0, salario=0):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.salario = salario

    @abstractmethod
    def calcular_salario(self):
        pass

    def analisar_salario(self):
        texto = (
            f"O salário de [bold cyan]{self.nome}[/] ([italic dim]{type(self).__name__}[/])\n"
            f"é de [bold green]R$ {self.salario:.2f}[/] e corresponde a "
            f"[bold yellow]{self.salario / self.sal_min:.1f}[/] salários mínimos."
        )
        
        print(
            Painel(
                texto, 
                title="[bold magenta]📊 Análise Salarial[/]", # Título superior
                subtitle="[dim]Gestão de RH[/]",              # Subtítulo inferior
                border_style="bright_blue",                   # Cor da borda
                expand=False,                                 # Ajusta ao tamanho do texto
                padding=(1, 3)                                # Espaçamento (1 linha vertical, 3 colunas horizontal)
            )
        )

class FuncionarioHorista(Funcionario):
    def __init__(self, nome, valor_hora, horas_trab):
        super().__init__(nome, sal_bruto=0, salario=0)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab

    def calcular_salario(self):
        self.salario = (self.valor_hora * self.horas_trab) * self.inss

class FuncionarioMensalista(Funcionario):
    def __init__(self, nome, sal_bruto):
        super().__init__(nome, sal_bruto=sal_bruto, salario=0)

    def calcular_salario(self):
        self.salario = self.sal_bruto * self.inss
