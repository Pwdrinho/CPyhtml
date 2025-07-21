import unittest
from cpf import ValidaCPF

class TestValidaCPF(unittest.TestCase):
    
    def test_cpf_valido(self):
        cpf = ValidaCPF('529.982.247-25')
        self.assertTrue(cpf.valida())

    def test_cpf_invalido(self):
        cpf = ValidaCPF('123.456.789-00')
        self.assertFalse(cpf.valida())

    def test_cpf_com_letrar(self):
        cpf = ValidaCPF('529abc982def247gh25')
        self.assertTrue(cpf.valida())
    
    def test_cpf_vazio(self):
        cpf = ValidaCPF('')
        self.assertFalse(cpf.valida())
        
    def test_cpf_sequencia(self):
        cpf = ValidaCPF('777.777.777-77')
        self.assertFalse(cpf.valida())

if __name__ == '__main__':
    unittest.main()