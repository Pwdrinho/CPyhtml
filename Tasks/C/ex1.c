// Saidas de Dados
#include <stdio.h>

int main() {

    printf("mensagem \? \" \' \\ \t"); 
    printf("mensagem \123 \v"); // octal ASCII
    printf("Hello World!. \n"); // saida literal
    printf("Valor inteiro: %d. \n", 420);
    printf("Valor real: %f. \t", 3.14159265);
    printf("Valor real formatado: %.2f. \v", 3.14159265);
    printf("Dado de texto: %c. \n", 'a');
    printf("Dado de texto: %s. \n", "testando");
    return 0;

}

// "%d, %f, %s, ... " são especificadores de formatos