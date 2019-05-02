def potencia_vi():
    V = float(input("Tensão: "))
    I = float(input("Intensidade de Corrente: "))
    potencia_vi = V*I
    
    print(potencia_vi)

potencia_vi()

def potencia_ri2():
    R = float(input("Resitência: "))
    I = float(input("Intensidade de Corrente: "))
    potencia_ri2 = R*I*I

    print(potencia_ri2)

potencia_ri2()
