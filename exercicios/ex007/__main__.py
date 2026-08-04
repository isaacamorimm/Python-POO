from rich import print, inspect
from classes import Aluno, Professor, Funcionario

def main():
    a1 = Aluno("José", 35, "Informática", "TODAS")
    a1.fazer_aniversario()
    a1.fazer_matricula()
    #inspect(a1, methods=True)

    p1 = Professor("Marcos", 17, "Biologia", "T01")
    p1.dar_aula()
    #inspect(a1, methods=True)

    f1 = Funcionario("Claudia", 27, "Secretária", "Secretaria")
    f1.fazer_aniversario()
    f1.bater_ponto()
    #inspect(f1, methods=True)

    a1.estudar()
    p1.estudar()
    f1.estudar()
    
if __name__ == "__main__":
    main()