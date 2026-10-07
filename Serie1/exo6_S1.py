# Étape 1 : Créer une fonction et afficher le dictionnaire initial
def gerer_dictionnaires(personne):
    print("le dictionnaire est :", personne)

# Étape 2 : Ajouter une nouvelle clé-valeur
    personne["profession"] = "Développeur"
    print("ajout de la profession :", personne)

# Étape 3 : Mettre à jour une valeur existante
    personne["âge"] = 30
    print("changement d'âge :", personne)

# Étape 4 : Supprimer une clé
    del personne["ville"]
    print("supp de ville :", personne)

# Étape 5 : Rechercher une clé
    if "nom" in personne:
        print("la clé 'nom' existe toujours et sa valeur est ",personne["nom"])
    #Correction, ajout de else
    else:
        print("La clé 'nom' n'a pas été trouvée.")

# Étape 6 : Parcourir le dictionnaire
    print("Le dictionnaire mis à jour est :")
    for cle, valeur in personne.items():
        print(f"{cle} : {valeur}")

individu = {"nom":"Camille", "âge":22, "ville":"Versailes"}
gerer_dictionnaires(individu)