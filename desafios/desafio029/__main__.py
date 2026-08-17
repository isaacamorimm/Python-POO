from classes029 import Diario
from rich import print, inspect

def main():
    d = Diario("Senha")

    d.escrever("Olá mundo!")
    d.escrever("oi")
    d.escrever("vai tomando")

    d.ler("Senha")

    inspect(d, private=True, methods=True)

if __name__ == "__main__":
    main()

