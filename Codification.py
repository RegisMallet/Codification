"""Fichier de démarrage"""

import webbrowser
from threading import Timer
from flask import Flask, render_template
import pandas as pd
import os
# import win32gui, win32con

# The_program_to_hide = win32gui.GetForegroundWindow()
# win32gui.ShowWindow(The_program_to_hide, win32con.SW_HIDE)

    
app = Flask(__name__)
# app = Flask(__name__, static_folder='lib/static', template_folder='lib/templates')


@app.route('/')    
def home():
    
    # Lire le fichier CSV
    data = pd.read_csv(r'C:\Users\regis\Documents\Codification\Base de données.csv', sep=';')
    
    # Sélectionner seulement les colonnes impaires
    #data = data.iloc[:, ::2]
    data = data.fillna('')
    # Convertir le DataFrame en une liste de dictionnaires
    data_dict = data.to_dict()

    # Obtenez les noms des colonnes (les clés du dictionnaire)
    col_names = list(data_dict.keys())

    # Créez une liste pour stocker les noms des colonnes
    noms_colonnes = []

    # Créez une liste pour stocker les dictionnaires de valeurs
    dicts_valeurs = []

    # Parcourez chaque nom de colonne
    for col_name in col_names:
        # Ajoutez le nom de la colonne à la liste des noms de colonnes
        noms_colonnes.append(col_name)

        # Obtenez le dictionnaire des valeurs de la colonne
        dict_valeurs = data_dict[col_name]

        # Ajoutez le dictionnaire des valeurs à la liste des dictionnaires de valeurs
        dicts_valeurs.append(dict_valeurs)
    print (f"len(nom_colonnes): {len(noms_colonnes)}")
    
    for i, (col_name, col_values) in enumerate(data_dict.items()):
        print(f"Colonne {i} ({col_name}): {col_values}")

    # Lire le contenu du fichier
    with open(r'C:\Users\regis\Documents\Codification\templates\index.html', 'r') as file:
        html = file.read()

    # Initialiser le conteneur
    container =""
    container += '<div class="parent">\n'
    # Initialiser le compteur des valeurs
    j=1
    for i in range(0,len(noms_colonnes),2): #Boucler chaque colonne et déployer le script html
        container += '<div class="container">\n'
        # container += '<div class="row">\n'
        container += f'<h3>{noms_colonnes[i]}</h3>\n'  # Ajoutez le nom de la colonne
        dict_valeurs = dicts_valeurs[i]
        dict_valeurs_correspondante = dicts_valeurs[i+1]
        for cle, valeur in dict_valeurs.items():
            valeur_associee = dict_valeurs_correspondante[cle]
            print(f"Clé: {cle}, Valeur: {valeur}, valeur_associée: {valeur_associee}")
            
            if valeur != "":
                container += '<div class="checkbox-inline">\n'
                container += f'<input type="checkbox" id="value{j}" name="value{j}" value="{valeur}"\
               data-extra-value="{valeur_associee}">\n'
                container += f'<label for="value{j}">{valeur}</label>\n'
                j=j+1
                container += '</div>\n'  # Fin de la div checkbox
        container += '</div>\n'  # Fin du conteneur
        
    container += '</div>\n'  # Fin du parent

    # Remplacez {checkboxes} dans le code HTML par le conteneur que vous venez de générer
    html = html.replace("{checkboxes}", container)


    # Écrire le contenu modifié dans un nouveau fichier
    with open(r'C:\Users\regis\Documents\Codification\templates\index_modified.html', 'w') as file:
        file.write(html)

    # Rendre le template HTML
    return render_template('index_modified.html', data=data_dict)

def cheminexecutable (*args):
    # Obtenez le répertoire de l'exécutable
    chemin_executable = os.path.dirname(os.path.abspath(__file__))

    # Construisez le chemin absolu du fichier
    chemin_fichier = os.path.join(chemin_executable, *args)
    return chemin_fichier
    


# @app.route('/bonjour', methods=['POST'])
# def hello():
#     resultat = request.form
#     nom = resultat['Nom']
#     prenom = resultat['Prénom']
#     # temps = resultat['Temps']
#     nomComplet = prenom + " " + nom
#     # reponse = temps
#     return render_template("page2.html" , message = nomComplet, message2 = module_globalV.ma_variable)
#     # return render_template("page2.html" , message = nomComplet, message2 = reponse)

def open_browser():
    webbrowser.open('http://localhost:5000/')

Timer(1, open_browser).start()

# url = "http://localhost:5000/"
# chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
# webbrowser.get(chrome_path).open(url)
# webbrowser.open(url)

app.run(host='0.0.0.0', port=5000)





