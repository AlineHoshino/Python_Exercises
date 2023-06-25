import csv

with open('numeros.csv', 'w') as arquivo:
    # Cria objeto de gravação
    writer = csv.writer(arquivo)

    # Grava no arquivo linha a linha

    writer.writerow(('nota1', 'nota2', 'nota3'))
