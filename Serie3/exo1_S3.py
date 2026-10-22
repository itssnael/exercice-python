# Définition de la fonction salaire_mensuel
def salaire_m(salaire_a):
    return salaire_a/12

# Définition de la fonction salaire_hebdomadaire
def salaire_hb(salaire_m):
    return salaire_m/4

# Définition de la fonction salaire_horaire
def salaire_hr(salaire_hb, heures_travail):
    return salaire_hb/heures_travail

def main():
    annuel = float(input("Saisissez votre salaire annuel : "))
    heures = float(input("Saisissez votre nombre d'heures travaillées par semaine : "))
    # Calcul du salaire horaire
    mensuel = salaire_m(annuel)
    hebdo = salaire_hb(mensuel)
    horaire = salaire_hr(hebdo, heures)
    print(f"Votre salaire horaire est de {horaire:.2f} euros.")

if __name__ == "__main__":
    main()
