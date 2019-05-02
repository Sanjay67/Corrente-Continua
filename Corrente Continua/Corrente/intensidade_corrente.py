def itsd_corrente_qt():
    Q = float(input("Quantidade de Carga Elétrica: "))
    t = float(input("Intervalo de Tempo: "))
    itsd_corrente_qt = Q/t

    print("Intensidade de Corrente: ")
    print(itsd_corrente)

def itsd_corrente_vr():
    V = float(input("Tensão: "))
    R = float(input("Resitência: "))
    itsd_corrente_vr = V/R

    print("Intensidade de Corrente: ")
    print(itsd_corrente_vr)
    
