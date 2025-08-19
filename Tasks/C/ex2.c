// Demonstração da utilização do "scanf" para alocar valor na memória nesse caso saber a idade.

#include <stdio.h>

int main() {
    int idade = 0;

    printf("Digite uma idade: ");
    scanf("%d", &idade);

    printf("Idade informada: %d. \n", idade);
}