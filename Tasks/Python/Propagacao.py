valores = input("Insira os valores: ").split()
erros = input("Insira os erros: ").split()

def propagação(valores, erros):
    erro_final = ((float(erros[0])/float(valores[0]))+(float(erros[1])/float(valores[1])))*float(valores[2])
    erro_final = round(erro_final, 4)
    print("Erro final: ", erro_final)
    return erro_final

propagação(valores, erros)