# 1. Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
# lista = list((range(1,11)))
# for n in lista:
#     print(n**2)

# 2. Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
# ling = ["Python", "Java", "C++", "JavaScript"]
# ling.remove("C++")
# ling.append("Ruby")
# print(ling)

# 3. Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. 
# Imprima cada informação.
# livros = {'Nome:':"The Hellbound Heart", 'Autor:':"Clive Barker", 'Ano:':"1986"}
# for chave, valor in livros.items():
#     print(f"{chave} {valor}")

# 4. Escreva um programa que conta o número de ocorrências de cada caractere em uma 
# string usando um dicionário.
# def contar_caracteres(s):
#     contagem = {}
#     for caractere in s:
#         contagem[caractere] = contagem.get(caractere, 0) + 1
#     return contagem
#
# print(contar_caracteres("abbccceeeeddddd"))
# Esse método get() está buscando o caracter dentro da String informada, caso não localize, ele por padrão
# retorna 0.

# 5. Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65},
# calcule o preço total da lista de compras.
frutas = ["maçã", "banana", "cereja"]
precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
total = sum(precos[item] for item in frutas)
print(f"Preço total: {total}")

# 6. Eliminação de Duplicatas - Dada uma lista de emails, remover todos os duplicados.
emails = ["abc@email.com", "cba@email.com", "abc@email.com", "123@email.com"]
emails_unicos = list(set(emails))
print(emails_unicos)