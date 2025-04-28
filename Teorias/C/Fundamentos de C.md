# Fundamentos da Linguagem C

## 1. Introdução à Linguagem C
A linguagem C foi criada por Dennis Ritchie nos anos 1970 para desenvolver o sistema operacional UNIX. É uma linguagem poderosa, eficiente e amplamente utilizada em sistemas embarcados, desenvolvimento de sistemas operacionais e aplicações de alto desempenho. C é uma linguagem compilada, estruturada e procedural, influenciando diversas linguagens modernas como C++, Java e Python.

## 2. Compilando e Executando um Programa C
Para escrever e rodar um programa em C, é necessário um compilador como o **GCC** (GNU Compiler Collection).

### Compilando e Executando com GCC via Terminal
1. Escreva o código em um arquivo **.c** (ex: `programa.c`).
2. Compile o código:
   ```sh
   gcc programa.c -o programa
   ```
3. Execute o programa:
   ```sh
   ./programa
   ```

Explicação:
- `gcc programa.c -o programa`: Compila o arquivo `programa.c` e gera um executável `programa`.
- `./programa`: Executa o programa compilado.

### Compilação no Visual Studio Code
Se você deseja programar em C no VS Code, siga os passos abaixo:

1. Instale o compilador GCC (pelo MinGW no Windows, ou via `sudo apt install gcc` no Linux).
2. No VS Code, instale a extensão **C/C++** da Microsoft.
3. Abra o terminal integrado (`Ctrl + ~`) e compile usando o comando `gcc programa.c -o programa`.
4. Execute o programa com `./programa`.

Isso permite compilar e rodar programas C diretamente no VS Code de forma eficiente.

## 3. Estrutura Básica de um Programa em C
Um programa básico em C segue uma estrutura padronizada:

```c
#include <stdio.h>  // Biblioteca padrão para entrada e saída

int main() {
    printf("Hello, World!\n");
    return 0;
}
```
- `#include <stdio.h>`: Importa a biblioteca para entrada e saída de dados.
- `int main()`: Função principal do programa.
- `printf()`: Função para exibir texto na tela.
- `return 0;`: Indica que o programa foi executado com sucesso.

## 4. Tipos de Dados e Variáveis
Em C, variáveis precisam ser declaradas com um tipo de dado antes do uso:

```c
int idade = 25;       // Inteiro
float altura = 1.75;  // Decimal (precisão simples)
double peso = 70.5;   // Decimal (precisão dupla)
char inicial = 'A';   // Caractere
```

### Modificadores de Tipo
Os tipos podem ser modificados para otimizar o uso de memória:
- `short`, `long` (Ex: `long int x;`)
- `unsigned`, `signed` (Ex: `unsigned int y;`)

## 5. Operadores e Expressões
C suporta operadores para manipular variáveis e valores.

### Operadores Aritméticos
```c
int soma = 10 + 5;  // Adição
int sub = 10 - 5;   // Subtração
int mult = 10 * 5;  // Multiplicação
int div = 10 / 2;   // Divisão
int mod = 10 % 3;   // Resto da divisão
```

### Operadores Relacionais
```c
if (x == y)  // Igualdade
if (x != y)  // Diferente
if (x > y)   // Maior que
if (x < y)   // Menor que
if (x >= y)  // Maior ou igual
if (x <= y)  // Menor ou igual
```

### Operadores Lógicos
```c
if (x > 0 && y > 0) // AND lógico
if (x > 0 || y > 0) // OR lógico
if (!(x > 0))       // NOT lógico
```

## 6. Entrada e Saída de Dados
Para entrada e saída de dados usamos `printf` e `scanf`:

```c
#include <stdio.h>

int main() {
    int idade;
    printf("Digite sua idade: ");
    scanf("%d", &idade);
    printf("Você tem %d anos.\n", idade);
    return 0;
}
```
Explicação:
- `printf()`: Função para exibir texto na tela.
- `scanf()`: Função usada para capturar entrada do usuário. O primeiro argumento define o formato (`%d` para inteiros, `%f` para floats, `%s` para strings, etc.), e o segundo argumento é o endereço da variável (`&idade`).

## 7. Estruturas de Controle
As estruturas de controle permitem que o programa tome decisões e execute blocos de código repetidamente com base em condições específicas.

### Condições (if/else)
A estrutura `if/else` permite a execução condicional de blocos de código. Se a condição for verdadeira, o bloco dentro do `if` será executado; caso contrário, o bloco dentro do `else` será executado.
```c
if (idade >= 18) {
    printf("Maior de idade\n");
} else {
    printf("Menor de idade\n");
}
```
### Switch-Case
O `switch-case` é uma alternativa ao `if-else` quando há múltiplas condições baseadas no mesmo valor.

```c
#include <stdio.h>

int main() {
    int opcao;
    printf("Escolha uma opção (1-3): ");
    scanf("%d", &opcao);

    switch (opcao) {
        case 1:
            printf("Você escolheu a opção 1.\n");
            break;
        case 2:
            printf("Você escolheu a opção 2.\n");
            break;
        case 3:
            printf("Você escolheu a opção 3.\n");
            break;
        default:
            printf("Opção inválida.\n");
    }
    return 0;
}
```

### Laços de Repetição (for, while, do-while)
Os laços de repetição são usados para executar um bloco de código várias vezes.

### For
O laço `for` é geralmente utilizado quando o **número de iterações é conhecido**.
```c
for (int i = 0; i < 5; i++) {
    printf("Número %d\n", i);
}
```
### While
O `while` é usado quando a repetição **depende de uma condição específica**.
```c
int contador = 0;
while (contador < 5) {
    printf("Contagem: %d\n", contador);
    contador++;
}
```
### Do-While
O `do-while` executa o bloco de código **ao menos uma vez** antes de verificar a condição.
```c
#include <stdio.h>

int main() {
    int numero;
    do {
        printf("Digite um número maior que 0: ");
        scanf("%d", &numero);
    } while (numero <= 0);
    printf("Você digitou: %d\n", numero);
    return 0;
}
```

---
## Exemplo Integrado
O código abaixo combina variáveis, entrada de dados, operadores, estruturas de controle e saída formatada:

```c
#include <stdio.h>

int main() {
    int idade;
    float altura;

    printf("Digite sua idade: ");
    scanf("%d", &idade);
    printf("Digite sua altura (em metros): ");
    scanf("%f", &altura);

    if (idade >= 18) {
        printf("Você é maior de idade.\n");
    } else {
        printf("Você é menor de idade.\n");
    }

    printf("Você tem %d anos e %.2f metros de altura.\n", idade, altura);

    printf("Contagem regressiva:\n");
    for (int i = 5; i > 0; i--) {
        printf("%d\n", i);
    }
    printf("FIM!\n");

    return 0;
}
```

Este programa captura a idade e altura do usuário, verifica se ele é maior de idade e exibe uma contagem regressiva.

---
Este documento cobre os conceitos fundamentais da linguagem C, incluindo estrutura básica, compilação, entrada e saída de dados, operadores, controle de fluxo e um exemplo prático! 🚀