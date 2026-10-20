def extraire_identite(mail):
    return mail.split("@")[0]

def format_identite(patronyme):
    parties = patronyme.split(".")  # Donne ['pierre', 'durand']
    prenom = parties[0].upper()     # 'PIERRE'
    nom = parties[1].upper()        # 'DURAND'
    return f"{prenom} {nom}"
#(Alternative en une seule ligne : return patronyme.replace(".", " ").upper())

def main():
    adresse_mail = input("Saisissez votre adresse mail : ")
    identite = extraire_identite(adresse_mail)
    patro = format_identite(identite)
    print(f"Votre patronyme est : {patro}")

if __name__ == "__main__":
    main()