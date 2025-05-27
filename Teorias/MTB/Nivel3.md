## Pergunta: Escreva um código que **encontre o maior número em uma lista**.

### Estruturado
```python
def encontrar_maior(lista):
    if not lista:
        return None  # Retorna None se a lista estiver vazia
    maior = lista[0]
    for numero in lista:
        if numero > maior:
            maior = numero
    return maior
```
### Orientado à Objetos
```python
class ListaDeNumeros:
    def __init__(self,numeros):
        self.numeros = numeros

    def MaiorNumero(self):
        if not self.numeros:
            return none
        maior = self.numeros[0]
        for numero in self.numeros:
            if numero > maior:
                maior = numero
    return maior
``` 
---
## Pergunta: Escreva um código que conte a ocorrência de elementos em uma lista.

### Orientado à Objetos
```python
class ContadorDeOcorrencias:
    def __init__(self, lista):
        self.lista = lista

    def contar_ocorrencias(self):
        ocorrencias = {}
        for elemento in self.lista:
            if elemento in ocorrencias:
                ocorrencias[elemento] += 1
            else:
                ocorrencias[elemento] = 1
        return ocorrencias
```

## Pergunta: Escreva um código que combine duas listas em uma 