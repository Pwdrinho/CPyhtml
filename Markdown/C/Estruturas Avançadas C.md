# Estruturas Avançadas em C

## 8. Arrays
Arrays são coleções de elementos do mesmo tipo armazenados em posições consecutivas na memória. Eles podem ser **unidimensionais** ou **multidimensionais**. São amplamente utilizados para armazenar e processar grandes quantidades de dados de forma eficiente.

### Declaração e Acesso
Os arrays podem ser declarados especificando seu tipo e tamanho. O acesso aos elementos é feito através de índices que começam em `0`.
```c
#include <stdio.h>

int main() {
    int numeros[5] = {1, 2, 3, 4, 5};
    for (int i = 0; i < 5; i++) {
        printf("Elemento %d: %d\n", i, numeros[i]);
    }
    return 0;
}
```

### Arrays Multidimensionais
Arrays multidimensionais armazenam dados em tabelas, como matrizes.
```c
#include <stdio.h>

int main() {
    int matriz[2][2] = {{1, 2}, {3, 4}};
    printf("Elemento [1][1]: %d\n", matriz[1][1]);
    return 0;
}
```

## 9. Strings
Strings em C são arrays de caracteres terminados pelo caractere nulo `\0`. Como não há um tipo `string` nativo em C, são manipuladas como arrays de `char`.

### Declaração e Manipulação de Strings
```c
#include <stdio.h>
#include <string.h>

int main() {
    char nome[50];
    printf("Digite seu nome: ");
    scanf("%49s", nome);
    printf("Olá, %s!\n", nome);
    return 0;
}
```
Funções úteis para manipulação de strings:
- `strlen(str)`: Retorna o tamanho da string.
- `strcpy(dest, src)`: Copia `src` para `dest`.
- `strcat(dest, src)`: Concatena `src` ao final de `dest`.
- `strcmp(str1, str2)`: Compara duas strings.

## 10. Funções em C
As funções ajudam a modularizar o código e evitar repetição, tornando o código mais organizado e reutilizável. Elas podem ter parâmetros e retornar valores.

### Declaração e Chamada de Funções
```c
#include <stdio.h>

void saudacao() {
    printf("Olá, bem-vindo ao programa!\n");
}

int main() {
    saudacao();
    return 0;
}
```
### Funções com Retorno e Parâmetros
```c
#include <stdio.h>

int soma(int a, int b) {
    return a + b;
}

int main() {
    int resultado = soma(5, 3);
    printf("Soma: %d\n", resultado);
    return 0;
}
```
### Passagem por Referência
Em C, podemos passar argumentos por referência usando ponteiros, permitindo a alteração direta dos valores das variáveis passadas.
```c
#include <stdio.h>

void dobrar(int *num) {
    *num *= 2;
}

int main() {
    int valor = 10;
    dobrar(&valor);
    printf("Valor dobrado: %d\n", valor);
    return 0;
}
```

## 11. Alocação Dinâmica de Memória
A alocação dinâmica permite reservar memória em tempo de execução, útil para manipulação eficiente de grandes quantidades de dados. O uso adequado da função `free()` é essencial para evitar vazamentos de memória.

### Exemplo com malloc e free
```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *ptr = (int*) malloc(5 * sizeof(int));
    if (ptr == NULL) {
        printf("Erro de alocação de memória.\n");
        return 1;
    }
    for (int i = 0; i < 5; i++) {
        ptr[i] = i * 2;
        printf("%d ", ptr[i]);
    }
    free(ptr);
    return 0;
}
```

## 12. Manipulação de Arquivos
A manipulação de arquivos permite a leitura e escrita de dados em arquivos do sistema. Podemos ler e escrever arquivos usando `fopen`, `fscanf` e `fprintf`, `fclose` permitindo salvar e recuperar dados de forma persistente.


### Exemplo de Escrita e Leitura em Arquivo
```c
#include <stdio.h>

int main() {
    FILE *arquivo = fopen("dados.txt", "w");
    if (arquivo == NULL) {
        printf("Erro ao abrir o arquivo.\n");
        return 1;
    }
    fprintf(arquivo, "Olá, arquivo!\n");
    fclose(arquivo);
    
    arquivo = fopen("dados.txt", "r");
    if (arquivo == NULL) {
        printf("Erro ao abrir o arquivo para leitura.\n");
        return 1;
    }
    char linha[100];
    fgets(linha, 100, arquivo);
    printf("Conteúdo do arquivo: %s\n", linha);
    fclose(arquivo);
    return 0;
}
```

## Exemplo Integrado
O código abaixo combina arrays, strings, funções, alocação dinâmica de memória e manipulação de arquivos:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void salvar_dados(char *nome, int *idades, int tamanho) {
    FILE *arquivo = fopen("dados.txt", "w");
    if (arquivo == NULL) {
        printf("Erro ao abrir o arquivo.\n");
        return;
    }
    fprintf(arquivo, "Nome: %s\n", nome);
    fprintf(arquivo, "Idades: ");
    for (int i = 0; i < tamanho; i++) {
        fprintf(arquivo, "%d ", idades[i]);
    }
    fprintf(arquivo, "\n");
    fclose(arquivo);
}

int main() {
    char nome[50];
    printf("Digite seu nome: ");
    scanf("%49s", nome);

    int tamanho = 5;
    int *idades = (int*) malloc(tamanho * sizeof(int));
    if (idades == NULL) {
        printf("Erro de alocação de memória.\n");
        return 1;
    }

    printf("Digite %d idades:\n", tamanho);
    for (int i = 0; i < tamanho; i++) {
        scanf("%d", &idades[i]);
    }

    salvar_dados(nome, idades, tamanho);
    printf("Dados salvos com sucesso!\n");
    
    free(idades);
    return 0;
}
```

Este exemplo recebe um nome e uma lista de idades do usuário, aloca memória dinamicamente e salva os dados em um arquivo.

---

Este documento cobre estruturas avançadas da linguagem C, incluindo manipulação de arrays, strings e arquivos, além de alocação dinâmica de memória! 🚀