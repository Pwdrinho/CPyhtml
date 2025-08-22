// Enunciado

#include <stdio.h>

int main () {
    char mapa[1002][1002];
    int P;

    scanf("%d", &P);

    int i = 1, j = 1, iInicial, jInicial;

    while ( scanf("%c", &mapa[i][j]) != EOF) {
        if (mapa[i][j] == '\n') {
            i++;
            j = 0;

        }


    }



    return 0;
}