from ex008 import ContaBancaria

def main():
    c1 = ContaBancaria(1, "João", 5000)
    c1.depositar(1000)
    c1._titular = "Pedro"
    c1._ContaBancaria__saldo = 0
    print(c1)

if __name__ == "__main__":
    main()