# On importe uniquement les fonctions dont on a besoin depuis le fichier 2
from exo2_S3 import extraire_identite, format_identite

def valider_mail(mail):
    if "@" in mail:
        partie_gauche = mail.split("@")[0]
        return "." in partie_gauche
    return False

def main():
    while True:
        adresse_mail = input("Saisissez votre adresse mail : ")
        if valider_mail(adresse_mail):
            break
        print("Erreur : l'adresse doit contenir un '.' entre le prénom et le nom, ainsi qu'un '@'. Réessayez.")

    # On utilise directement les fonctions importées
    identite = extraire_identite(adresse_mail)
    patro = format_identite(identite)
    print(f"Votre patronyme est : {patro}")

# Ce bloc empêchera à son tour exo3 d'exécuter main() s'il est importé ailleurs
if __name__ == "__main__":
    main()