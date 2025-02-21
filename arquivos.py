import csv

# Setando o caminho a uma variável
caminho_arq = "arquivos/exemplo.csv"

# Inicializando a variável para receber os valores do csv
dados = []

# Abrindo o csv com o gerenciador de contexto "with"
with open(file=caminho_arq, mode="r", encoding="utf-8") as arquivo:
    valores = csv.DictReader(arquivo)

# Inserindo os valores dentro da lista dados
    for campos in valores:
       dados.append(campos)

# Printando os valores contidos em dados
for linhas in dados:
    print(linhas)
        