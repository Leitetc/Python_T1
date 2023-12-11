class Funcionario:
    def __init__(self, nome, sobrenome, data_nascimento, rg, ano_admissao, salario):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
        self.rg = rg
        self.ano_admissao = ano_admissao
        self.salario = salario

    def __str__(self):
        return f"{self.data_nascimento},{self.nome} {self.sobrenome},{self.salario}\n"