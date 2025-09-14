#include <stdio.h>

int main() {
    float num, soma = 0;
    int contador = 0;

    printf("Digite os numeros (digite -1 para parar):\n");

    while (1) {
        scanf("%f", &num);
        if (num == -1) { // critério de parada
            break;
        }
        soma += num;
        contador++;
    }

    if (contador > 0) {
        float media = soma / contador;
        printf("Foram inseridos %d numeros.\n", contador);
        printf("A media dos numeros eh: %.2f\n", media);
    } else {
        printf("Nenhum numero valido foi inserido.\n");
    }

    return 0;
}
