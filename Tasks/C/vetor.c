//A seguinte função recebe um numero n >= 1
// e um vetor e vevolve o valor de um
// elemento máximo de v[o..n-1].

#include <stdio.h>

int max (int n, int v[]) {
    int x = v[0];
    for (int j = 1; j < n; j += 1)
        if (x < v[j])
            x = v[j];
    return x;
}

int main() {
    // 1. Define um vetor de exemplo para testar a função
    int meus_numeros[] = {10, 5, 42, 18, 99, 37};
    int tamanho = 6; // O número de elementos no vetor

    // 2. Chama a sua função 'max' e guarda o resultado
    int valor_maximo = max(tamanho, meus_numeros);

    // 3. Imprime o resultado na tela
    printf("O valor maximo no vetor eh: %d\n", valor_maximo);

    return 0;
}