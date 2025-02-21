import csv

caminho_arq = "arquivos/exemplo.csv"

dados = []

with open(file=caminho_arq, mode="r", encoding="utf-8") as arquivo:
    valores = csv.DictReader(arquivo)
    for campos in valores:
       dados.append(campos)

for linhas in dados:
    print(linhas)
        