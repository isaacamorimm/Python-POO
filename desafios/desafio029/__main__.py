from classes029 import Diario
from rich import print, inspect

def main():
    d = Diario("Senha")
    
    d.senha = "123"

    d.escrever("Olá mundo!")
    d.escrever("oi")
    d.escrever("vai tomando")

    d.ler("123")

    inspect(d, private=True, methods=True)

if __name__ == "__main__":
    main()

