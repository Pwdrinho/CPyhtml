from Packages.agenda import Agenda

def menu(): 
    agenda = Agenda() 
    print("\n--- Agenda de Contatos ---")
    while True: 
        print("\n1. Adicionar Contato") 
        print("2. Listar Contatos") 
        print("3. Buscar Contato") 
        print("4. Remover Contato")
        print("5. Editar Contato") 
        print("6. Sair") 
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            Maiuscula = nome.title()
            telefone = input("Telefone: ")
            agenda.adicionar_contato(Maiuscula, telefone)

        elif opcao == "2":
            agenda.listar_contatos()

        elif opcao == "3":
            nome = input("Nome para buscar: ")
            agenda.buscar_contato(nome)

        elif opcao == "4":
            agenda.listar_contatos()
            try:
                indice = int(input("\nDigite o índice do contato que deseja remover: "))
                agenda.remover_contato(indice)
            except ValueError:
                print("Por favor, digite um número válido.")

        elif opcao == "5":
            agenda.listar_contatos()
            try:
                indice = int(input("\n Digite o índice do contato que deseja editar: "))
                agenda.editar_contato(indice)
            except ValueError:
                print("Por favor, digite um número válido.")

        elif opcao == "6":
            print("Saindo...")
            break

        else:
            print("\n Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()