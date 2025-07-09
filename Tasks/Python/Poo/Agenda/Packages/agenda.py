from Packages.contato import Contato

class Agenda: 
    def __init__(self): 
        self.contatos = []

    def adicionar_contato(self, nome, telefone):
        self.contatos.append(Contato(nome, telefone))
        print("Contato adicionado com sucesso!")

    def listar_contatos(self):
        if not self.contatos:
            print("\nA agenda está vazia.")
        else:
            for i, contato in enumerate(self.contatos):
                print(f"[{i}] Nome: {contato.nome}, Telefone: {contato.telefone}")


    def buscar_contato(self, nome):
        encontrados = [c for c in self.contatos if c.nome.lower() == nome.lower()]
        if encontrados:
            for contato in encontrados:
                print(contato)
        else:
            print("Contato não encontrado.")

    def remover_contato(self, indice):
        if not self.contatos:
            print("\nA agenda está vazia.")
            return

        if 0 <= indice < len(self.contatos):
            removido = self.contatos.pop(indice)
            print(f"Contato '{removido.nome}' removido com sucesso.")
        else:
            print("Índice inválido!")

    def editar_contato(self, indice):
        if 0 <= indice < len(self.contatos):
            contato = self.contatos[indice]
            print(f"Editando contato: {contato}")
            novo_nome = input("\n Novo nome (pressione Enter para manter o atual): ")
            novo_telefone = input("Novo telefone (pressione Enter para manter o atual): ")

            if novo_nome.strip():
                contato.nome = novo_nome
            if novo_telefone.strip():
                contato.telefone = novo_telefone

            print("Contato atualizado com sucesso!")
        else:
            print("Índice inválido!")