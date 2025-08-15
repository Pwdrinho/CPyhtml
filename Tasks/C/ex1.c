#include <stdio.h>

int main() {

    printf("mensagem \? \" \' \\ \t");
    printf("mensagem \123 \v"); // octal ASCII
    printf("mensagem3. \t");
    printf("mensagem4. \v");
    printf("Hello World!. \n");
    printf("Valor inteiro: %d. \n", 420);
    printf("Valor real: %f. \t", 3.1459265);
    printf("Valor real formatado: %.2f. \v", 3.1459265);
    printf("Dado de texto: %c. \n", 'a');
    printf("Dado de texto: %s. \n", "testando");
    return 0;

}