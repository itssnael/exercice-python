def gerer_dictionnaires(personne):
    print("le dictionnaire est :", personne)

    personne["profession"] = "Développeur"
    print("ajout de la profession :", personne)

    personne["âge"] = 30
    print("changement d'âge :", personne)

    del personne["ville"]
    print("supp de ville :", personne)

    if "nom" in personne:
        print("la valeur nom existe toujours et sa valeur est ",personne["nom"])

    print("VD du dictionnaire :")
    for cle, valeur in personne.items():
        print(f"{cle} : {valeur}")

individu = {"nom":"Camille", "âge":22, "ville":"Versailes"}
gerer_dictionnaires(individu)