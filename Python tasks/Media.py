valores = input("insira os valores: ").split()
n = len(valores)

def calcular_Tmedio (valores, n):
    somatoria = 0
    for i in range(n):
        somatoria += float(valores[i])

    Tmedio = somatoria/len(valores)
    Tmedio = round(Tmedio, 3)
    print("Tempo medio: ", Tmedio)

    return Tmedio

Tmedio = calcular_Tmedio(valores, n)

def calcular_desvio_padrao (Tmedio, valores, n):
    somatorio = 0
    for i in range(n):
        diferenca = (float(valores[i]) - float(Tmedio))**2.0
        somatorio += diferenca
    
    variancia = (somatorio/(n-1))
    desvio_padrao = variancia**(1/2)
    desvio_padrao = round(desvio_padrao, 3)
    print("Desvio padrão: ", desvio_padrao)

    return desvio_padrao

def calcular_aceleracao (Tmedio):
    distancia = 0.1
    aceleracao = 2*distancia/(Tmedio**2)
    aceleracao = round(aceleracao, 3)
    print("Aceleração: ", aceleracao) 
    
    return aceleracao

calcular_desvio_padrao(Tmedio, valores, n)
calcular_aceleracao(Tmedio)