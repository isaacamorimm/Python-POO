from classes031 import Retangulo
from rich import print, inspect

def main():
    r = Retangulo(10, 10)
    r.base = 10
    r.altura = 10
    r.medidas = (4, 4)
    print(r.medidas)
    inspect(r, private=True, methods=True)

if __name__ == "__main__":
    main()