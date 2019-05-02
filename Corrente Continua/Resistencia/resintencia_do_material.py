# 1° - Potências e Raizes
# 2° - Multiplicação e Divisão
# 3° - Adição e Subtração
def resitencia():
    r = float(input("Resistividade do Condutor: "))
    L = float(input("Comprimento do Condutor: "))
    A = float(input("Área da Sessão Transversal: "))

    resitencia_material = (r*L)/A
    print("Resitencia do Material: ")
    print(resitencia)

resitencia()
    
