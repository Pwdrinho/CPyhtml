#include <stdio.h>

int main() {

    // operações aritmeticas = + - / * % ++ --

    int x = 6;
    int y = 4;
    int z = -2;
    int result = 0;

    result = x + y - z ;


    printf("novo resultado eh: %d \n", result);

    printf("novo valor de z eh: %d \n", z);

    // divisão com floats

    float a = 3;
    float b = 2;
    float c = 0;

    c = b / a;

    printf("novo valor de c eh: %f \n", c);

    z++;
    x--;

    printf("incremento de z eh: %d \n", x);
    printf("decremento de x eh: %d \n", z);

    result = result % 11; 

    printf("resto eh: %d \n", result);
    
    // Atalhos que representam a mesma operação aritmetica
    // x += 3 é igual a x = x + 3;
    // x -= 3 é igual a x = x - 3;
    // x *= 3 é igual a x = x * 3;
    // x /= 3 é igual a x = x / 3;

    return 0;
}