from supermercado import Supermercado

def main():
    mercado = Supermercado()

    while True:
        print("\nMenu:")
        print("1. Inserir novo produto")
        print("2. Excluir produto cadastrado")
        print("3. Listar todos os produtos")
        print("4. Consultar preço de um produto")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            codigo = input("Digite o código do produto: ")
            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            mercado.inserir_produto(codigo, nome, preco)
        elif opcao == "2":
            codigo = input("Digite o código do produto a ser excluído: ")
            mercado.excluir_produto(codigo)
        elif opcao == "3":
            mercado.listar_produtos()
        elif opcao == "4":
            codigo = input("Digite o código do produto para consultar o preço: ")
            mercado.consultar_preco(codigo)
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Escolha uma opção válida.")

if __name__ == "__main__":
    main()