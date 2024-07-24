# Módulo para manipular archivos json
import json

# Función que me permitirá leer un archivo json y guardarlo en una variable
def readJsonFile(fileName):
    data = ""
    try:
        with open(fileName) as json_file:
            data = json.load(json_file)
    except IOError:
        print("El archivo no existe, te equivocaste ;)")
    return data