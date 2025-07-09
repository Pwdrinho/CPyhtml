agenda = []

def criar_contato():
    nome = input("Nome: ")
    Maiuscula = nome.title()
    telefone = input("Telefone: ")
    agenda.append({"nome": Maiuscula, "telefone": telefone})
    print("Contato adicionado!")

def listar_contatos():
    if not agenda:
        print("Nenhum contato.")
        return
    for i, contato in enumerate(agenda):
        print(f"[{i}] Nome: {contato['nome']}, Telefone: {contato['telefone']}")

def editar_contato():
    listar_contatos()
    try:
        idx = int(input("ID do contato a editar: "))
        if idx < 0 or idx >= len(agenda):
            print("ID inválido.")
            return
        print(f"Editando contato: {agenda[idx]['nome']}")
        Nnome = input("\nNovo nome: ")
        Maiuscula = Nnome.title()
        Ntelefone = input("Novo telefone: ")
        agenda[idx] = {"nome": Maiuscula, "telefone": Ntelefone}
        print("Contato atualizado!")
    except ValueError:
        print("Entrada inválida.")

def remover_contato():
    listar_contatos()
    try:
        idx = int(input("ID do contato a remover: "))
        if idx < 0 or idx >= len(agenda):
            print("ID inválido.")
            return
        del agenda[idx]
        print("Contato removido!")
    except ValueError:
        print("Entrada inválida.")

def buscar_contato():
    termo = input("Digite o nome ou parte do nome a buscar: ").lower()
    encontrados = []

    for i, contato in enumerate(agenda):
        if termo in contato['nome'].lower():
            encontrados.append((i, contato))

    if encontrados:
        print("\nContatos encontrados:")
        for i, contato in encontrados:
            print(f"[{i}] Nome: {contato['nome']}, Telefone: {contato['telefone']}")
    else:
        print("Nenhum contato encontrado.")


def menu():
    print("\n--- Agenda de Contatos ---")
    while True:
        print("\n1. Adicionar Contato\n2. Listar Contatos\n3. Editar Contatos\n4. Remover Contatos\n5. Buscar Contatos\n6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            criar_contato()
        elif opcao == '2':
            listar_contatos()
        elif opcao == '3':
            editar_contato()
        elif opcao == '4':
            remover_contato()
        elif opcao == '5':
            buscar_contato()
        elif opcao == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

menu()