from classes030 import Credencial
from rich import print, inspect

def main():
    c = Credencial()
    c.senha = "OutraSenh"
    print(c.validar("OutraSenh"))

if __name__ == "__main__":
    main()
