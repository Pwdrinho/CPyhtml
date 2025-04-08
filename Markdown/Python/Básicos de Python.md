# Introdução ao Python

Python é uma linguagem de programação de alto nível, interpretada e de propósito geral. Ela é amplamente utilizada para desenvolvimento web, automação, análise de dados, inteligência artificial e muito mais.

## Instalando o Python
Para instalar o Python, acesse [python.org](https://www.python.org/) e faça o download da versão mais recente. Certifique-se de marcar a opção "Add Python to PATH" durante a instalação.

Após a instalação, verifique se o Python está funcionando executando o comando:
```sh
python --version
```

## Executando Código Python
Python pode ser executado de várias formas:
- Diretamente no terminal usando `python`.
- Criando scripts (`.py`) e executando com `python nome_do_arquivo.py`.
- Usando notebooks Jupyter para uma abordagem interativa.

---

# Tipos de Dados e Variáveis

## Declarando Variáveis
Python não exige declaração explícita de tipo:
```python
idade = 25  # Inteiro
altura = 1.75  # Float
nome = "Carlos"  # String
ativo = True  # Booleano
```

## Principais Tipos de Dados
- **Inteiros (`int`)**: Números inteiros, ex: `10`, `-5`
- **Ponto Flutuante (`float`)**: Números decimais, ex: `3.14`, `-0.5`
- **String (`str`)**: Sequência de caracteres, ex: `"Olá, mundo!"`
- **Booleano (`bool`)**: Valores `True` ou `False`

## Conversão de Tipos (Casting)
Podemos converter tipos de dados manualmente:
```python
numero = "10"
numero_int = int(numero)  # Converte string para inteiro
preco = float("19.99")  # Converte string para float
idade_str = str(25)  # Converte inteiro para string
```

---

# Estruturas de Controle de Fluxo

## Condicionais (`if`, `elif`, `else`)
Usamos `if` para criar fluxos condicionais baseados em valores booleanos.
```python
idade = 18
if idade >= 18:
    print("Você é maior de idade.")
elif idade >= 16:
    print("Você pode votar, mas não dirigir.")
else:
    print("Você é menor de idade.")
```

## Laços de Repetição

### `for`
Usamos `for` para iterar sobre sequências como listas e strings:
```python
for i in range(5):
    print(f"Número: {i}")
```

### `while`
Executa um bloco de código enquanto a condição for verdadeira:
```python
contador = 0
while contador < 5:
    print(f"Contagem: {contador}")
    contador += 1
```

---

# Operações Matemáticas e Comparação

## Operações Matemáticas
- **Soma (`+`)**: `a + b`
- **Subtração (`-`)**: `a - b`
- **Multiplicação (`*`)**: `a * b`
- **Divisão (`/`)**: `a / b`
- **Divisão Inteira (`//`)**: `a // b`
- **Módulo (`%`)**: `a % b` (resto da divisão)
- **Exponenciação (`**`)**: `a ** b`

Exemplo:
```python
a = 10
b = 3
print(a + b)  # 13
print(a // b)  # 3 (Divisão inteira)
print(a ** b)  # 1000 (10^3)
```

## Operadores de Comparação
- **Igualdade (`==`)**: `a == b`
- **Diferente (`!=`)**: `a != b`
- **Maior que (`>`)**: `a > b`
- **Menor que (`<`)**: `a < b`
- **Maior ou igual (`>=`)**: `a >= b`
- **Menor ou igual (`<=`)**: `a <= b`

Exemplo:
```python
x = 5
y = 10
print(x == y)  # False
print(x < y)   # True
print(x >= 5)  # True
```

---

# Exemplo Integrado

O seguinte código combina variáveis, condicionais, loops e operações matemáticas para criar um programa que recebe um nome e idade do usuário, verifica se ele é maior de idade e exibe uma contagem regressiva.

```python
# Solicita nome e idade do usuário
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

# Verifica a maioridade
if idade >= 18:
    print(f"{nome}, você é maior de idade.")
else:
    print(f"{nome}, você ainda é menor de idade.")

# Exemplo de operações matemáticas
soma = idade + 5
print(f"Daqui a 5 anos, você terá {soma} anos.")

# Contagem regressiva até zero
print("Contagem regressiva:")
for i in range(idade, 0, -1):
    print(i)
print("FIM!")
```

---
Esse documento cobre a introdução ao Python, variáveis, tipos de dados, controle de fluxo e operações matemáticas. 🚀