from App import cliente_ja_cadastrado
from Arquivo import carregar_do_arquivo, salvar_em_arquivo


class Cliente:
    def __init__(self, nome, cpf, endereco, telefone):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone

    def __str__(self):
        return f"Nome: {self.nome}\nCPF: {self.cpf}\nEndereço: {self.endereco}\nTelefone: {self.telefone}\n"

    def cadastrar_cliente():
        nome = input("Informe o nome do cliente: ")
        cpf = input("Informe o CPF do cliente: ")
        endereco = input("Informe o endereço do cliente: ")
        telefone = input("Informe o telefone do cliente: ")

        clientes = carregar_do_arquivo("clientes.txt")
    
        if not cliente_ja_cadastrado(cpf, clientes):
            novo_cliente = Cliente(nome, cpf, endereco, telefone)
            clientes.append(novo_cliente)
            salvar_em_arquivo(clientes, "clientes.txt")
            print("Cliente cadastrado com sucesso!")
        else:
            print("Cliente já cadastrado!")

    def cliente_ja_cadastrado(cpf, clientes):
        for cliente in clientes:
            if cliente.cpf == cpf:
                return True
        return False
    
    def escolher_cliente(clientes):
        cpf_cliente = input("Informe o CPF do cliente: ")
        for cliente in clientes:
            if cliente.cpf == cpf_cliente:
                return cliente

        print("Cliente não encontrado.")
        return None