# Estruturas de Dados e Funções em Python

## 4. Estruturas de Dados: Listas e Tuplas

### Listas
Listas são coleções ordenadas e **mutáveis** de elementos. Podemos armazenar diferentes tipos de dados em uma lista.

#### Criando e Manipulando Listas
```python
# Criando uma lista
numeros = [1, 2, 3, 4, 5]
nomes = ["Alice", "Bob", "Carlos"]

# Acessando elementos
print(numeros[0])  # Primeiro elemento
print(nomes[-1])   # Último elemento

# Modificando elementos
numeros[0] = 10

# Adicionando elementos
numeros.append(6)  # Adiciona ao final
numeros.insert(2, 99)  # Insere na posição 2

# Removendo elementos
del numeros[2]  # Remove pelo índice
numeros.remove(10)  # Remove pelo valor

# Percorrendo uma lista
for nome in nomes:
    print(nome)
```

### Tuplas
Tuplas são semelhantes às listas, mas são **imutáveis** (seus elementos não podem ser alterados após a criação).
```python
cores = ("vermelho", "azul", "verde")
print(cores[0])  # Acessando elementos
```

---

## 5. Dicionários
Dicionários são coleções de pares `chave: valor`, usados para armazenar dados de forma estruturada.
```python
# Criando um dicionário
aluno = {"nome": "Ana", "idade": 22, "curso": "Engenharia"}

# Acessando valores
print(aluno["nome"])  # Saída: Ana

# Adicionando e alterando valores
aluno["idade"] = 23  # Modificando um valor
aluno["nota"] = 9.5  # Adicionando um novo par

# Removendo um elemento
del aluno["curso"]

# Percorrendo um dicionário
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")
```

---

## 6. Manipulação de Strings
Strings são cadeias de caracteres e possuem diversos métodos úteis.

### Operações com Strings
```python
texto = "Python é incrível!"

# Tamanho da string
print(len(texto)) #Saída: 18

# Maiúsculas e minúsculas
print(texto.upper())  # Tudo maiúsculo
print(texto.lower())  # Tudo minúsculo

# Substituição de palavras
novo_texto = texto.replace("incrível", "fantástico")
print(novo_texto) # Saída: "Python é fantástico!"

# Divisão de strings
palavras = texto.split()  # Divide por espaços
print(palavras) #Saída: ['Python', 'é', 'incrivel!']

# Junção de strings
frase = " - ".join(palavras)
print(frase) #Saìda: Python-é-incrivel!
```

### Formatação de Strings
```python
nome = "Alice"
idade = 25

# Usando f-strings
print(f"Meu nome é {nome} e tenho {idade} anos.")

# Usando format()
print("Meu nome é {} e tenho {} anos.".format(nome, idade))
```

---

## 7. Funções em Python
Funções permitem reutilização de código e organização do programa.

### Criando Funções
```python
def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("Carlos"))
```

### Funções com Múltiplos Argumentos
```python
def soma(a, b):
    return a + b

resultado = soma(5, 3)
print(resultado)
```

### Funções com Valores Padrão
```python
def apresentar(nome, idade=18):
    print(f"Nome: {nome}, Idade: {idade}")

apresentar("Ana")  # Usa o valor padrão de idade
apresentar("Pedro", 25)
```

### Funções Lambda
Funções anônimas de uma linha para operações rápidas.
```python
quadrado = lambda x: x ** 2
print(quadrado(4)) #Saída: 16
```

### Escopo de Variáveis
```python
x = 10  # Variável global

def funcao():
    x = 5  # Variável local
    print(x)

funcao() #Saída: 5
print(x)  # Mantém o valor global
```

### List Comprehension
Uma forma concisa de criar listas.
```python
numeros = [x for x in range(10) if x % 2 == 0]
print(numeros) #Saída: [0, 2, 4, 6, 8]
```

---

## 8. Manipulação de Arquivos

### Leitura e Escrita em Arquivos
```python
# Escrevendo em um arquivo
with open("arquivo.txt", "w") as f:
    f.write("Olá, mundo!\n")

# Lendo um arquivo
with open("arquivo.txt", "r") as f:
    conteudo = f.read()
    print(conteudo)
```

### Trabalhando com CSV e JSON
```python
import csv
import json

# Criando um arquivo CSV
with open("dados.csv", "w", newline='') as f:
    escritor = csv.writer(f)
    escritor.writerow(["Nome", "Idade"])
    escritor.writerow(["Alice", 25])

# Criando um arquivo JSON
dados = {"nome": "Alice", "idade": 25}
with open("dados.json", "w") as f:
    json.dump(dados, f)
```

### Manipulação de Pastas
```python
import os
import shutil

# Criando uma pasta
os.makedirs("minha_pasta", exist_ok=True)

# Movendo um arquivo
shutil.move("arquivo.txt", "minha_pasta/")
```

---

# Exemplo Integrado
O código abaixo combina listas, dicionários, manipulação de strings e funções para criar um sistema simples de cadastro de alunos.

```python
def cadastrar_aluno(nome, idade, curso):
    aluno = {"nome": nome, "idade": idade, "curso": curso}
    return aluno

# Lista para armazenar os alunos
alunos = []

# Adicionando alunos
alunos.append(cadastrar_aluno("Alice", 22, "Matemática"))
alunos.append(cadastrar_aluno("Bob", 20, "Física"))

# Exibindo informações formatadas
def exibir_alunos(lista):
    for aluno in lista:
        print(f"Nome: {aluno['nome']} - Idade: {aluno['idade']} - Curso: {aluno['curso']}")

exibir_alunos(alunos)

# Salvando em JSON
import json
with open("alunos.json", "w") as f:
    json.dump(alunos, f)

# Lendo o JSON
def carregar_alunos():
    with open("alunos.json", "r") as f:
        return json.load(f)

print(carregar_alunos())
```

---
Este documento cobre listas, tuplas, dicionários, manipulação de strings, funções, escopo de variáveis, formatação de strings, list comprehension e manipulação de arquivos, com um exemplo final que integra todos esses conceitos! 🚀