# **INSTRUÇÃO PRÁTICA**   | **Python P003**

**OBJETIVO DA ATIVIDADE**
>* Exercitar o uso das técnicas de modularização de código
>com ajuda de funções.
>* Exercitar as técnicas de iteração avançada e compreensões
>de lista e dicionário.


# Exercício 1: Estruturando um código com funções

**Este exercício já foi implementado no módulo anterior, utilizando C++. Vejamos agora como ficaria uma versão feita em Python: Faça um programa para um supermercado que permita a consulta de preço de produtos.O programa deverá armazenar de cada produto o seu código, seu nome e seu preço. Ao utilizar o programa o usuário deve poder:**
1. Inserir um novo produto
2. Excluir um produto cadastrado
3. Listar todos os produtos com seus respectivos códigos e preços
4. Consultar o preço de um produto através de seu código.

**O código deve ser formado de uma string numérica de 13 caracteres (podeconter zeros a esquerda, então não pode ser um número)**

**O nome pode ter qualquer tamanho e deve começar sempre com uma letra maiúscula.**

**O preço deve ser apresentado com duas casas decimais**

**O sistema deve listar os produtos na tela, 10 produtos de cada vez em ordem crescente de preço.** 

* O código deve ser implementado numa pasta Supermercado e o programaprincipal deve ser implementado no arquivo main.py.

* Pode utilizar como modelo o arquivo main.py disponível na postagem daatividade. Pesquise sobre esta estrutura e para que ela serve.

* Cada uma das funcionalidades do menu de opções deve ser implementada numa função específica.
* Já que não temos structs em Python vamos usar dicionários para armazenar cada produto.

* Vamos armazenar os produtos numa lista de dicionários;

# Exercício 2: Pesquisa sobre persistência de dados.

**Este exercício já foi implementado no módulo anterior, utilizando C++.Vejamos agora como ficaria uma versão feita em Python: Crie um dicionário para armazenar dados (nome, sobrenome, ano de nascimento, RG, ano de admissão, salário) de empregados de uma empresa. Leia as informaçõiessobre os funcionários de um arquivo e guarde numa lista.**

* Faça uma função chamada “Reajusta_dez_porcento( )” que receba
por parâmetro a lista de empregados e atualize o salário de cada
empregado em 10%.

* Crie um aplicativo para testar a função. Pode reproduzir a estrutura
utiliza