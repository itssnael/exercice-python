# Étape 1 : Créer une fonction et afficher le dictionnaire initial
def gerer_dictionnaires(personne):
    print("le dictionnaire est :", personne)
    #ligne de séparation
    print("-"*20)

# Étape 2 : Ajouter une nouvelle clé-valeur
    personne["profession"] = "Développeur"
    print("ajout de la profession :", personne)
    print("-"*20)

# Étape 3 : Mettre à jour une valeur existante
    personne["âge"] = 30
    print("changement d'âge :", personne)
    print("-"*20)

# Étape 4 : Supprimer une clé
    del personne["ville"]
    print("supp de ville :", personne)
    print("-"*20)

# Étape 5 : Rechercher une clé
    if "nom" in personne:
        print("la clé 'nom' existe toujours et sa valeur est ",personne["nom"])
    #Correction, ajout de else
    else:
        print("La clé 'nom' n'a pas été trouvée.")
    print("-"*20)

# Étape 6 : Parcourir le dictionnaire
    print("Le dictionnaire mis à jour est :")
    for cle, valeur in personne.items():
        print(f"{cle} : {valeur}")
    print("-"*20)

individu = {"nom":"Camille", "âge":22, "ville":"Versailes"}
gerer_dictionnaires(individu)