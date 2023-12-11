from produto import Produto

class Supermercado:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, codigo, nome, preco):
        novo_produto = Produto(codigo, nome, preco)
        self.produtos.append(novo_produto)
        print("Produto inserido com sucesso!")

    def excluir_produto(self, codigo):
        for produto in self.produtos:
            if produto.codigo == codigo:
                self.produtos.remove(produto)
                print("Produto excluído com sucesso!")
                return
        print("Produto não encontrado.")

    def listar_produtos(self):
        print("Lista de produtos:")
        for produto in self.produtos:
            print(f"Código: {produto.codigo} | Nome: {produto.nome} | Preço: R$ {produto.preco:.2f}")

    def consultar_preco(self, codigo):
        for produto in self.produtos:
            if produto.codigo == codigo:
                print(f"O preço do produto {produto.nome} é R$ {produto.preco:.2f}")
                return
        print("Produto não encontrado.")