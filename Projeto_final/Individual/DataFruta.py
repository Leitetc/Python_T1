from abc import ABC, abstractmethod

class Data:
    def __init__(self, dia=1, mes=1, ano=2000):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    @property
    def dia(self):
        return self.__dia
    
    @dia.setter
    def dia(self, dia):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        self.__dia = dia

    @property
    def mes(self):
        return self.__mes
    
    @mes.setter
    def mes(self, mes):
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        self.__mes = mes

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__ano = ano
    
    def __str__(self):
        return "{}/{}/{}".format(self.__dia, self.__mes, self.__ano)

    def __eq__(self, outraData):
        return (self.__dia, self.__mes, self.__ano) == (outraData.__dia, outraData.__mes, outraData.__ano)
    
    def __lt__(self, outraData):
        return (self.__ano, self.__mes, self.__dia) < (outraData.__ano, outraData.__mes, outraData.__dia)
    
    def __gt__(self, outraData):
        return (self.__ano, self.__mes, self.__dia) > (outraData.__ano, outraData.__mes, outraData.__dia)


class AnaliseDados(ABC): 
    @abstractmethod
    def entradaDeDados(self):
        pass

    @abstractmethod
    def mostraMediana(self):
        pass
    
    @abstractmethod
    def mostraMenor(self):
        pass

    @abstractmethod
    def mostraMaior(self):
        pass
    
    @abstractmethod
    def listarEmOrdem(self):
        pass


class ListaNomes(AnaliseDados):
    def __init__(self):
        self.__lista = []        

    def entradaDeDados(self):
        quantidade = int(input("Quantos nomes deseja inserir? "))
        for _ in range(quantidade):
            nome = input("Digite o nome: ")
            self.__lista.append(nome)

    def mostraMediana(self):
        self.__lista.sort()
        tamanho = len(self.__lista)
        if tamanho % 2 == 0:
            indice1 = tamanho // 2 - 1
            indice2 = tamanho // 2
            mediana = self.__lista[indice1]  # Retorna o primeiro nome entre os dois no meio
        else:
            indice = tamanho // 2
            mediana = self.__lista[indice]  # Retorna o nome do meio
        return mediana

    def mostraMenor(self):
        return min(self.__lista)

    def mostraMaior(self):
        return max(self.__lista)

    def listarEmOrdem(self):
        return sorted(self.__lista)


class ListaDatas(AnaliseDados):
    def __init__(self):
        self.__lista = []        
    
    def entradaDeDados(self):
        quantidade = int(input("Quantas datas deseja inserir? "))
        for _ in range(quantidade):
            print("Digite a data no formato dd/mm/aaaa:")
            data_input = input()
            dia, mes, ano = map(int, data_input.split('/'))
            data = Data(dia, mes, ano)
            self.__lista.append(data)

    def mostraMediana(self):
        self.__lista.sort()
        tamanho = len(self.__lista)
        if tamanho % 2 == 0:
            indice1 = tamanho // 2 - 1
            indice2 = tamanho // 2
            mediana = self.__lista[indice1]  # Retorna a primeira data entre as duas no meio
        else:
            indice = tamanho // 2
            mediana = self.__lista[indice]  # Retorna a data do meio
        return mediana

    def mostraMenor(self):
        return min(self.__lista)

    def mostraMaior(self):
        return max(self.__lista)

    def listarEmOrdem(self):
        return sorted(self.__lista)


class ListaSalarios(AnaliseDados):
    def __init__(self):
        self.__lista = []        

    def entradaDeDados(self):
        quantidade = int(input("Quantos salários deseja inserir? "))
        for _ in range(quantidade):
            salario = float(input("Digite o salário: "))
            self.__lista.append(salario)

    def mostraMediana(self):
        self.__lista.sort()
        tamanho = len(self.__lista)
        if tamanho % 2 == 0:
            indice1 = tamanho // 2 - 1
            indice2 = tamanho // 2
            mediana = (self.__lista[indice1] + self.__lista[indice2]) / 2  # Retorna a média entre os dois valores do meio
        else:
            indice = tamanho // 2
            mediana = self.__lista[indice]  # Retorna o valor do meio
        return mediana

    def mostraMenor(self):
        return min(self.__lista)

    def mostraMaior(self):
        return max(self.__lista)

    def listarEmOrdem(self):
        return sorted(self.__lista)


class ListaIdades(AnaliseDados):
    def __init__(self):
        self.__lista = []        
    
    def entradaDeDados(self):
        quantidade = int(input("Quantas idades deseja inserir? "))
        for _ in range(quantidade):
            idade = int(input("Digite a idade: "))
            self.__lista.append(idade)

    def mostraMediana(self):
        self.__lista.sort()
        tamanho = len(self.__lista)
        if tamanho % 2 == 0:
            indice1 = tamanho // 2 - 1
            indice2 = tamanho // 2
            mediana = (self.__lista[indice1] + self.__lista[indice2]) / 2  # Retorna a média entre as duas idades do meio
        else:
            indice = tamanho // 2
            mediana = self.__lista[indice]  # Retorna a idade do meio
        return mediana

    def mostraMenor(self):
        return min(self.__lista)

    def mostraMaior(self):
        return max(self.__lista)

    def listarEmOrdem(self):
        return sorted(self.__lista)


def main():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()

    listaListas = [nomes, datas, salarios, idades]

    for lista in listaListas:
        lista.entradaDeDados()
        print(f"Mediana: {lista.mostraMediana()}")
        print(f"Menor elemento: {lista.mostraMenor()}")
        print(f"Maior elemento: {lista.mostraMaior()}")
        print(f"Lista em ordem: {lista.listarEmOrdem()}")
        print("___________________")

    # Iterador zip
    lista_nomes = ["Eduardo", "Nairan", "Arthur"]
    lista_salarios = [3000, 4000, 5000]

    for nome, salario in zip(lista_nomes, lista_salarios):
        print(f"{nome}: R${salario}")

    # Iterador map
    salarios_reajustados = list(map(lambda salario: salario * 1.1, lista_salarios))
    print(salarios_reajustados)

    # Iterador filter
    lista_datas = [Data(1, 1, 2018), Data(2, 2, 2019), Data(3, 3, 2020)]

    for data in lista_datas:
        if data < Data(1, 1, 2019):
            data.dia = 1

    for data in lista_datas:
        print(data)

    print("Fim do teste!!!")

if __name__ == "__main__":
    main()