import sys
import csv
import os
import re

def maior_sequencia(sequencia, substring):
    padrao = f'(?:{substring})+'
    matches = re.findall(padrao, sequencia)
    if matches:
        return max(len(match) // len(substring) for match in matches)
    return 0

def main():
    if len(sys.argv) != 3:
        print("O programa deve ser inicializado com dois argumentos (Caminho para o banco de dados) + (Caminho para a Sequência a comparar)")
        sys.exit(1)

    data_path = sys.argv[1]
    person_path = sys.argv[2]

    if not os.path.isfile(data_path):
        print(f"Erro: O arquivo '{data_path}' não foi encontrado.")
        sys.exit(1)
    elif not os.path.isfile(person_path):
        print(f"Erro: O arquivo '{person_path}' não foi encontrado.")
        sys.exit(1)

    dna_data = []
    
    with open(data_path) as data_csv_file:
        data_csv_reader = list(csv.DictReader(data_csv_file))
        for row in data_csv_reader:
            dna_data.append({key: int(value) if key != 'name' else value for key, value in row.items()})

    with open(person_path) as person_csv_file:
        sequencia = person_csv_file.read().strip()

    relevant_keys = dna_data[0].keys() - {'name'}

    match_counts = {key: maior_sequencia(sequencia, key) for key in relevant_keys}

    for person in dna_data:
        if all(person[key] == match_counts[key] for key in relevant_keys):
            print(f"DNA corresponde a: {person['name']}.")
            break
    else:
        print("Nenhuma correspondência encontrada.")

if __name__ == "__main__":
    main()
