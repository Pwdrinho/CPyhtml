# Algoritmo orientado a objetos para calcular o determinante de uma matriz 2x2 ou 3x3.

import random

class Matriz:
    def __init__(self, matriz):
        self.matriz = matriz

    def determinante(self):
        if len(self.matriz) == 2:
            return self._determinante_2x2()
        elif len(self.matriz) == 3:
            return self._determinante_3x3()
        else:
            raise ValueError("A matriz deve ser 2x2 ou 3x3.")
        
    def _determinante_2x2(self):
        if len(self.matriz) != 2 or len(self.matriz[0]) != 2:
            raise ValueError("A matriz deve ser 2x2.")
        return self.matriz[0][0] * self.matriz[1][1] - self.matriz[0][1] * self.matriz[1][0]
    
    def _determinante_3x3(self):
        if len(self.matriz) != 3 or len(self.matriz[0]) != 3:
            raise ValueError("A matriz deve ser 3x3.")
        return None
    
    # falta continuar
    
#exemplo de uso