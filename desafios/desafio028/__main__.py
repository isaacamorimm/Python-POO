from classes028 import Termostato
from rich import print, inspect

def main():
    t = Termostato()
    t.temperatura = 23.5
    inspect(t, private=True, methods=True)

if __name__ == "__main__":
    main()