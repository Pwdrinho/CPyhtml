#include <stdio.h>

int maximo(int a, int b) {
    if (a > b) {
        return a;
    } else {
        return b;
    }
}

int potencia(int a, int b) {
    int i, produto = 1;
    for(i = 0; i < b; i++) {
        produto = a * produto;
    }
    return produto;
}

int main() {
    int a, b, maior, pot;
    printf("-----/-/----- \n");
    printf("Entre com a e b \n");
    scanf("%d %d", &a, &b);
    maior = maximo(a, b);
    pot = potencia(a, b);
    printf("Maior: %d \n", maior);
    printf("a^b: %d \n", pot);
    printf("-----/-/----- \n");
    return 0;
}