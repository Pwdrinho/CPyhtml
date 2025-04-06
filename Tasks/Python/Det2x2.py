#Esse programa, ao receber uma matriz 2x2, calcula o determinante, o traço e verifica se a matriz é linearmente independente ou dependente.
#O determinante é calculado pela regra de Sarrus, o traço é a soma dos elementos da diagonal principal e a matriz é linearmente independente se o determinante for diferente de 0.
print('Por favor, insera valores para compor a sua Matriz')
def Determinante():
    M = [[0, 0], [0, 0]]

    for i in range(2):
        for j in range(2):
            M[i][j] = int(input(f'Digite um valor para [{i}, {j}]: '))
    print("\nMatriz inserida:")

    for i in M:
        print(f'[{i[0]:^5}] [{i[1]:^5}]')

    det = M[0][0] * M[1][1] - M[0][1] * M[1][0]
    print(f'\nO determinante é {det}')

    print("A matriz é LD" if det == 0 else "A matriz é LI")

    traco = M[0][0] + M[1][1]
    print(f'O traço da matriz é {traco}')

Determinante()