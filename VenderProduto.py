from Arquivo import salvar_em_arquivo


def vender_produto(produtos):
    print("Produtos disponíveis:")
    for i, produto in enumerate(produtos, 1):
        print(f"{i} - {produto}")

    indice_produto = int(input("Escolha o produto a ser vendido (pelo número): "))

    if 1 <= indice_produto <= len(produtos):
        quantidade_venda = int(input("Informe a quantidade a ser vendida: "))
        produto = produtos[indice_produto - 1]

        if quantidade_venda <= produto.quantidade:
            produto.quantidade -= quantidade_venda
            salvar_em_arquivo(produtos, "produtos.txt")
            print(f"{quantidade_venda} unidades de {produto.nome} vendidas com sucesso!")
        else:
            print("Quantidade insuficiente em estoque.")
    else:
        print("Índice de produto inválido.")

        