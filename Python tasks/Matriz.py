n = int(input('Digite um valor para n: '))

matriz = [[i+j for j in range(n)] for i in range(n)]
for i in range (0, n):
    for j in range (0, n):
        print(f'[{matriz[i] [j]:^3}]', end='')
    print()