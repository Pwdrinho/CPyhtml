/* Métodos para descobrir código de algum caractere em ASCII*/

#include <stdio.h>

int main() {
    char c;

    printf("Digite algum caractere: ");
    scanf("%c", &c);

    printf("Codigo ASCII de '%c': %d\n", c, c);

    return 0;
}

/* ex1 de execução
input: e
output: Codigo ASCII de 'e': 101
*/

/* ex2 de execução
input: $
output: Codigo ASCII de '$': 36
*/