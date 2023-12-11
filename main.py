import os
import datetime
from Cliente import Cliente
from Produto import Produto
from Servico import Servico
from Arquivo import salvar_em_arquivo, carregar_do_arquivo

















def menu():
    clientes = carregar_do_arquivo("clientes.txt")
    produtos = carregar_do_arquivo("produtos.txt")
    servicos = carregar_do_arquivo("servicos.txt")

    opcao = 0
    while opcao != 8:
        print("\n==== Menu Principal ====")
        print("1 - Cadastrar Cliente")
        print("2 - Cadastrar Produto")
        print("3 - Cadastrar Serviço")
        print("4 - Agendar Serviço")
        print("5 - Exibir Estoque de Produtos")
        print("6 - Vender Produto")
        print("7 - Exibir Clientes")
        print("8 - Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            Cliente.cadastrar_cliente()
        elif opcao == 2:
            Produto.cadastrar_produto()
        elif opcao == 3:
            Servico.cadastrar_servico()
        elif opcao == 4:
            cliente = Cliente.escolher_cliente(clientes)
            servico = Servico.escolher_servico(servicos)
            if cliente and servico:
                Servico.agendar_servico(cliente, servico)
        elif opcao == 5:
            Produto.exibir_estoque(produtos)
        elif opcao == 6:
            vender_produto(produtos)
        elif opcao == 7:
            for cliente in clientes:
                print(cliente)
        elif opcao == 8:
            print("Saindo do programa.")
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
