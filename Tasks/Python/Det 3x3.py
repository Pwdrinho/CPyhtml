#Esse programa, ao receber uma matriz 3x3, calcula o determinante, o traço e verifica se a matriz é linearmente independente ou dependente.
#O determinante é calculado pela regra de Sarrus, o traço é a soma dos elementos da diagonal principal e a matriz é linearmente independente se o determinante for diferente de 0.
print('Por favor, insera valores para compor a sua Matriz')
def Determinante():
    M = [[0,0,0],[0,0,0],[0,0,0]]

    for i in range(3):
        for j in range(3):
            M[i][j]= int(input(f'Digite um valor para [{i}, {j}]: '))
    print("\nMatriz inserida:")

    for i in range (3):
        for j in range (3):
            print(f'[{M[i][j]:^5}]', end=' ')
        print()

    det = M[0][0]*M[1][1]*M[2][2] + M[0][1]*M[1][2]*M[2][0] + M[0][2]*M[1][0]*M[2][1] - M[0][2]*M[1][1]*M[2][0] - M[0][1]*M[1][0]*M[2][2] - M[0][0]*M[1][2]*M[2][1]
    print(f'\nO determinante é {det}')

    if det == 0:
        print('A matriz é Linearmente Dependente')
    else:
        print('A matriz é Linearmente Independente')

    traço = M[0][0] + M[1][1] + M[2][2]
    print(f'O traço da matriz é {traço}')
    return ''

Determinante()