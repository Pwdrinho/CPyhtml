def max(a, b):
    if a > b:
        return a
    else:
        return b
    
def potencia(a, b):
    produto = 1
    for i in range (b):
        produto = a * produto
    return produto

print("-----/-/-----")
print("Insira valores para a e b \n")
a = int(input("a:"))
b = int(input("b:"))

maior = max(a, b)
exp = potencia(a, b)

print("Maior:", maior)
print("a^b:", exp)
print("-----/-/-----")