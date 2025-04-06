#include <stdio.h>
#include <stdlib.h>

int main(){
    int n1, n2, n3, n4, soma;

    printf("Insira quatro numeros para serem somados:\n");
    fflush(stdin);
    scanf("%d", &n1);
    scanf("%d", &n2);
    scanf("%d", &n3);
    scanf("%d", &n4);
    
    soma = n1 + n2 + n3 + n4;
    printf("\n\nA soma entre eles eh: %d\n\n", soma);

    system("pause");
    return 0;
}