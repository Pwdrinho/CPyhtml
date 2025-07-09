class Reta():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def interpolar(self, x):
        it = self.a + x * self.b
        return it
    
a = int(input("Insira o valor de a: "))
b = int(input("Insira o valor de b: "))

p = Reta(a, b)

print(p.a) 
print(p.b,"\n")

x = int(input("Insira o valor de x: "))

print(p.interpolar(x),"\n")