// Enunciado

#include <stdio.h>

int main () {
    char mapa[1002][1002];
    int P;
    int Pinicial;

    scanf("%d", &P);
    Pinicial = P;

    int i = 1, j = 1, iInicial, jInicial;

    while ( scanf(" %c", &mapa[i][j]) != EOF) {
        if (mapa[i][j] == 'S') {
            iInicial = i;
            jInicial = j;
        }
        if (mapa[i][j] == '\n') {
            mapa[i][j] = '#';
            i++;
            j = 1;
            mapa[i][j-1] = '#';
        }
        else
        j++;
    }
    for (int k = 0; k < j; k++) {
        mapa[0][k] = mapa[i+1][k] = '#';
    }
    for (i = iInicial, j = jInicial; mapa[i][j] != 'E';) {
        if (mapa[i][j] == 'o') {
            P--;
        }
        mapa[i][j] = '#';

        if (mapa[i - 1][j] != '#') i--;
        else if (mapa[i][j - 1] != '#') j--;
        else if (mapa[i + 1][j] != '#') i++;
        else if (mapa[i][j + 1] != '#') j++;
    }
    if (P == 0 && Pinicial > 0) {
        printf("Todos morreram :(\n");
    } else if (P == Pinicial) {
        printf("Nenhum patinho foi encontrado pelo caminho...\n");
    } else {
        printf("%d patinhos encontraram a vovó!\n", P);
    }
    return 0;
}