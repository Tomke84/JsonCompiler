import csv
import json


def csv_to_json(csv_file, json_file):
    # Open het CSV-bestand om te lezen
    with open(csv_file, mode='r', encoding='utf-8-sig') as infile:
        reader = csv.reader(infile, delimiter=';')

        # Maak een lege dictionary voor de JSON-structuur
        data = {}

        for row in reader:
            if len(row) == 2:  # Controleer of de rij twee kolommen heeft
                key, value = row
                keys = key.split('.')  # Split de sleutel als deze een punt bevat
                d = data
                for part in keys[:-1]:  # Loop door de onderdelen van de sleutel behalve het laatste
                    d = d.setdefault(part, {})
                d[keys[-1]] = value  # Voeg de waarde toe aan de uiteindelijke sleutel

        # Schrijf de data naar een JSON-bestand
        with open(json_file, mode='w', encoding='utf-8') as outfile:
            json.dump(data, outfile, indent=4, ensure_ascii=False)


# Voorbeeldgebruik:
csv_file = 'C:\\Users\\kempe\\Downloads\\Map1.csv'  # Pad naar je CSV-bestand
json_file = 'C:\\Users\\kempe\\Downloads\\Map2.json'  # Pad naar het gewenste JSON-bestand

csv_to_json(csv_file, json_file)