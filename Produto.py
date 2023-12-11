from Arquivo import carregar_do_arquivo, salvar_em_arquivo


class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def __str__(self):
        return f"Nome: {self.nome}\nPreço: {self.preco}\nQuantidade: {self.quantidade}\n"

    def cadastrar_produto():
        nome = input("Informe o nome do produto: ")
        quantidade = int(input("Informe a quantidade em estoque: "))
        preco = float(input("Informe o preço do produto: "))

        produtos = carregar_do_arquivo("produtos.txt")
    
        novo_produto = Produto(nome, quantidade, preco)
        produtos.append(novo_produto)
        salvar_em_arquivo(produtos, "produtos.txt")
        print("Produto cadastrado com sucesso!")

    def exibir_estoque(produtos):
        for produto in produtos:
            print(produto)    