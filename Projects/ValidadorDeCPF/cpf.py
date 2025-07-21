import re

class ValidaCPF:
    def __init__(self, cpf):
        self.cpf = cpf
        print (f"DEBUG: CPF inserido: {self.cpf} \n")

    def valida(self):
        if not self.cpf:
            return False, "cpf invalido"
        
        novo_cpf = self._calculadigitos(self.cpf[:9])
        novo_cpf = self._calculadigitos(novo_cpf)

        if novo_cpf == self.cpf:
            return True, "cpf valido"
        return False, "cpf invalido"
        
    @staticmethod
    def _calculadigitos(fatia_cpf):
        if not fatia_cpf:
            return False
        
        sequencia = fatia_cpf[0] * len(fatia_cpf)
        
        if sequencia == fatia_cpf: 
            return False
        
        soma = 0
        for chave, multiplicador in enumerate(range(len(fatia_cpf)+1, 1, -1)):
            #print (f"DEBUG: {chave} * {multiplicador}")
            soma += int(fatia_cpf[chave]) * multiplicador
            #print (f"DEBUG {soma}")

        resto = 11 - (soma % 11)
        resto = resto if resto <= 9 else 0
        #print(f"DEBUG {resto} \n")
        return fatia_cpf + str(resto)

    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter # para chamar outro metodo que não seja numero
    def cpf(self, cpf):
        self._cpf = self._so_numeros(cpf) 

    @staticmethod
    def _so_numeros(cpf):
        return re.sub('[^0-9]', '', cpf)