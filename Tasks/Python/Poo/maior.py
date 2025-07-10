# Pergunta: Escreva um código que encontre o maior número em uma lista.
import random

class ListaDeNumeros:
    def __init__(self,numeros):
        self.numeros = numeros

    def MaiorNumero(self):
        if not self.numeros:
            return None
        maior = self.numeros[0]
        for numero in self.numeros:
            if numero > maior:
                maior = numero
        return maior
    
# Exemplo de uso
numeros = [random.randint(1, 1000) for _ in range(15)]
lista = ListaDeNumeros(numeros)
maior_numero = lista.MaiorNumero()
print(f"Lista: {numeros}")
print(f"Maior número: {maior_numero}")