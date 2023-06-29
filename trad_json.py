from googletrans import Translator
import json
import time

# Charger le fichier JSON
i = 0
with open('workout-data.json') as file:
    data = json.load(file)

# Créer une instance du traducteur
translator = Translator(service_urls=['translate.google.com'])
translator.raise_Exception = True
# Traduire chaque étape du fichier JSON en français
steps_list = []  # Liste pour stocker les valeurs 'steps'

# Parcourir chaque objet dans le tableau
for obj in data:
    time.sleep(1)
    if 'steps' in obj and obj['steps'] and obj['steps'] != '':    # Vérifier si la clé 'steps' existe et n'est pas vide
         steps = obj['steps']  # Récupérer la valeur de la clé 'steps' pour chaque objet
         i+=1
    print(i)
    # Traduire chaque étape en français
    translated_steps = []
    for step in steps:
        translated_step = translator.translate(step, src='en', dest='fr').text
        translated_steps.append(translated_step)
    obj['steps'] = translated_steps

# Sauvegarder les données traduites dans un nouveau fichier JSON
with open('./fichier_traduit.json', 'w+') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
