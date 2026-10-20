def valider_mail(mail):
    # Vérifie la présence du '@' et du '.' avant le '@'
    if "@" in mail:
        partie_gauche = mail.split("@")[0]
        return "." in partie_gauche
    return False

def extraire_identite(mail):
    return mail.split("@")[0]

def format_identite(patronyme):
    parties = patronyme.split(".")  # Donne ['pierre', 'durand']
    prenom = parties[0].upper()     # 'PIERRE'
    nom = parties[1].upper()        # 'DURAND'
    return f"{prenom} {nom}"
#(Alternative en une seule ligne : return patronyme.replace(".", " ").upper())

def main():
    while True:
        adresse_mail = input("Saisissez votre adresse mail : ")
        if valider_mail(adresse_mail):
            break
        print("Erreur : l'adresse doit contenir un '.' entre prénom et nom et un '@'. Réessayez.")
    identite = extraire_identite(adresse_mail)
    patro = format_identite(identite)
    print(f"Votre patronyme est : {patro}")

if __name__ == "__main__":
    main()