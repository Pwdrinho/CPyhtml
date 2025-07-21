from cpf import ValidaCPF

cpf = ValidaCPF('611.664.926-21')

if cpf.valida():
    print("------------------")
    print("CPF válido.")
    print("------------------")
else:
    print("------------------")
    print("CPF inválido")
    print("------------------")