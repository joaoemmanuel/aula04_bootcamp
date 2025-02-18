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
# frutas = ["maçã", "banana", "cereja"]
# precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
# total = sum(precos[item] for item in frutas)
# print(f"Preço total: {total}")

# 6. Eliminação de Duplicatas - Dada uma lista de emails, remover todos os duplicados.
# emails = ["abc@email.com", "cba@email.com", "abc@email.com", "123@email.com"]
# emails_unicos = list(set(emails))
# print(emails_unicos)

# 7. Filtragem de Dados - Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
# idades = [5, 7, 11, 17, 19, 18, 3, 22, 54]

# def maioridade(n):
#     if n >= 18:
#         return True
#     else:
#         return False
# adultos = list(filter(maioridade, idades))
# print(adultos)

# # Outra solução possível:
# idades = [5, 7, 11, 17, 19, 18, 3, 22, 54]
# maioridade = [idade for idade in idades if idade >= 18]
# print(maioridade)

# 8. Ordenação Personalizada - Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
# pessoas = [
#     {"nome": "Joao", "idade": 33},
#     {"nome": "Stefany", "idade": 30},
#     {"nome": "Carlos", "idade": 2}
# 
# ordenado = []
# for nome in pessoas:
#     ordenado.append(nome["nome"])
# ordenado.sort()
# print(ordenado)

# Outra solução possível que modifica diretamente o dicionário e é a mais adequada:
# pessoas.sort(key=lambda pessoa: pessoa["nome"])
# print(pessoas)

# 9. Agregação de Dados - Dado um conjunto de números, calcular a média.
# from statistics import fmean
# numeros = [5, 10, 22, 31, 57]
# print(fmean(numeros))

# # Outra solução possível:
# print(sum(numeros) / len(numeros))

# 10. Divisão de Dados em Grupos - Dada uma lista de valores, dividir em lista uma para valores pares e outra para ímpares.
# valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# pares = [valor for valor in valores if valor % 2 == 0]
# impares = [valor for valor in valores if valor % 2 != 0]

# print(f"Lista de Pares: {pares}\nLista de Impares: {impares}")

# 11. Atualização de Dados - Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.
# produtos = [
#     {"id": 1, "nome": "Teclado", "preço": 100},
#     {"id": 2, "nome": "Mouse", "preço": 80},
#     {"id": 3, "nome": "Monitor", "preço": 300}
# ]
# produtos[2]["preço"] += 40

# print(produtos)

# # Outra solução possível:
# for produto in produtos:
#     if produto["id"] == 1:
#         produto["preço"] += 75

# print(produtos)

# 12. Fusão de Dicionários - Dados dois dicionários, fundi-los em um único dicionário.
# dic1 = {"a": 1, "b": 2}
# dic2 = {"c": 3, "d": 4}

# dic3 = dic1 | dic2 # o | para unir dicionários só começou a partir do Python 3.9

# print(dic3)

# 13. Filtragem de Dados em Dicionário - Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.
# estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}
# filtrado = {chave: valor for chave, valor in estoque.items() if valor > 0}
# print(filtrado)

# 14. Extração de Chaves e Valores - Dado um dicionário, criar listas separadas para suas chaves e valores.
dic = {"a": 1, "b": 2, "c": 3}
chaves = list(dic.keys())
vals = list(dic.values())
print(f"Chaves: {chaves}\nValores: {vals}")