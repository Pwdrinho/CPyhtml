# Pergunta: Escreva um código que conte a ocorrência de elementos em uma lista.
import random

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
    
# Exemplo de uso
lista = [random.randint(1, 20) for _ in range(15)]
contador = ContadorDeOcorrencias(lista)
ocorrencias = contador.contar_ocorrencias()
print(f"Lista: {lista}")
print(f"Ocorrências: {ocorrencias}")

