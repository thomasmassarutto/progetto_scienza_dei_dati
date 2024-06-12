## questo script scarica e formatta il catalogo dei dataset NASA
## i dataset pubblici NASA: https://data.nasa.gov/data.json
## 
## dataset trovato su: https://www.tidytextmining.com/nasa
## 

import requests
import json

def scarica_file_json(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # errori HTTP
        return response.json()  # Parso il contenuto JSON
    ## gestione errori try
    except requests.exceptions.RequestException as e:
        print(f"Errore download: {e}")
        return None

def formatta_file_json(dati, percorso_file_output, indentazione=4):
    try:
        with open(percorso_file_output, 'w', encoding='utf-8') as file:
            json.dump(dati, file, indent=indentazione, ensure_ascii=False)
    ## gestione errori try    
    except Exception as e:
        print(f"Errore scrittura {e}")

## MAIN
url = 'https://data.nasa.gov/data.json'
percorso_file_output = 'data_nasa_formattato.json'

dati_json = scarica_file_json(url)

## se è stato scaricato correttamente procedi con formattazione
if dati_json:
    formatta_file_json(dati_json, percorso_file_output)
