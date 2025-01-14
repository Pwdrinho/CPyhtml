def adicão(a, b):
    return a + b 

def subtração(a, b):
    return a - b

def multiplicação(a, b):
    return a * b 

def divisão(a , b):
    if b != 0:
        return a / b
    else:
        return "Erro!! Divisão por zero."

while True:
    print("Escolha uma das seguintes operações:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    choice = input("Selecione uma das Opções disponíveis: ")
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Digite primeiro Número: "))
        num2 = float(input("Digite segundo Número: "))

        if choice == '1':
            print('Resultado:', adicão(num1, num2))

        elif choice == '2':
            print('Resultado: ', subtração(num1, num2))

        elif choice == '3':
            print('Resultado: ', multiplicação(num1, num2))

        elif choice == '4':
            print('Resultado:', divisão(num1, num2))

    elif choice == '5':
        print ("Encerrando Calculadora")
        break

    else:
        print("Erro, entrada invalida. Por favor selecione uma das opções sugeridas")