from empresa import carregar_funcionarios, salvar_funcionarios, reajusta_dez_porcento, adicionar_funcionario, excluir_funcionario

def main():
    arquivo = 'funcionarios.txt'
    lista_funcionarios = carregar_funcionarios(arquivo)

    while True:
        print("\nMenu:")
        print("1. Adicionar novo funcionário")
        print("2. Reajustar salários em 10%")
        print("3. Excluir funcionário")
        print("4. Mostrar funcionários")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            novo_funcionario = adicionar_funcionario()
            lista_funcionarios.append(novo_funcionario)
            salvar = input("Deseja salvar os dados? (S/N): ")
            if salvar.lower() == "s":
                salvar_funcionarios(lista_funcionarios, arquivo)
                print("Funcionário adicionado e dados salvos com sucesso!")
            else:
                print("Funcionário adicionado.")
        elif opcao == "2":
            reajusta_dez_porcento(lista_funcionarios)
            salvar_funcionarios(lista_funcionarios, arquivo)
            print("Salários reajustados em 10%. Dados salvos.")
        elif opcao == "3":
            lista_funcionarios = excluir_funcionario(lista_funcionarios)
            salvar_funcionarios(lista_funcionarios, arquivo)
        elif opcao == "4":
            print("Funcionários:")
            for funcionario in lista_funcionarios:
                print(funcionario)
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Escolha uma opção válida.")

if __name__ == "__main__":
    main()