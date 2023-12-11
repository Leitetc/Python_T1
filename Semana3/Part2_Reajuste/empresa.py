from funcionario import Funcionario

def carregar_funcionarios(arquivo):
    funcionarios = []
    try:
        with open(arquivo, 'r') as file:
            linhas = file.readlines()
            for linha in linhas:
                dados = linha.strip().split(',')
                if len(dados) == 3:  
                    data_nascimento, nome_completo, salario = dados
                    nome_sobrenome = nome_completo.split(' ')
                    if len(nome_sobrenome) >= 2:  
                        nome = nome_sobrenome[0]
                        sobrenome = ' '.join(nome_sobrenome[1:])
                        funcionario = Funcionario(nome, sobrenome, data_nascimento, "", "", salario)
                        funcionarios.append(funcionario)
                    else:
                        print(f"Erro: Linha com dados incompletos: {linha}")
                else:
                    print(f"Erro: Formato de dados inválido na linha: {linha}")
    except FileNotFoundError:
        print(f"Arquivo '{arquivo}' não encontrado. Será criado um novo arquivo ao salvar os dados.")

    return funcionarios

def salvar_funcionarios(funcionarios, arquivo):
    with open(arquivo, 'w') as file:
        for funcionario in funcionarios:
            nome_completo = f"{funcionario.nome} {funcionario.sobrenome}"
            file.write(f"{funcionario.data_nascimento},{nome_completo},{funcionario.salario}\n")

def reajusta_dez_porcento(funcionarios):
    for funcionario in funcionarios:
        funcionario.salario = float(funcionario.salario.replace("R$", "").replace(".", "").replace(",", ".")) * 1.1
        funcionario.salario = f"R$ {funcionario.salario:.2f}"

def adicionar_funcionario():
    nome = input("Digite o nome do funcionário: ")
    sobrenome = input("Digite o sobrenome do funcionário: ")
    data_nascimento = input("Digite a data de nascimento do funcionário (dia/mês/ano): ")
    rg = input("Digite o RG do funcionário: ")
    ano_admissao = input("Digite o ano de admissão do funcionário: ")
    salario = input("Digite o salário do funcionário (R$ XXXX,XX): ")

    return Funcionario(nome, sobrenome, data_nascimento, rg, ano_admissao, salario)

def excluir_funcionario(funcionarios):
    if not funcionarios:
        print("Não há funcionários para excluir.")
        return funcionarios

    print("Funcionários:")
    for i, funcionario in enumerate(funcionarios):
        print(f"{i + 1}. {funcionario.nome} {funcionario.sobrenome}")

    try:
        indice = int(input("Digite o número do funcionário a ser excluído: ")) - 1
        if 0 <= indice < len(funcionarios):
            funcionarios.pop(indice)
            print("Funcionário excluído com sucesso!")
        else:
            print("Número de funcionário inválido.")
    except ValueError:
        print("Por favor, insira um número válido.")

    return funcionarios