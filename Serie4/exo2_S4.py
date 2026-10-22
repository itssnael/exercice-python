import salaire

def main():
    annuel = float(input("Saisissez votre salaire annuel brut : "))
    taux = float(input("Saisissez votre taux de prélevement : "))
    s_mensuel = salaire.salaire_m(annuel)
    net = salaire.salaire_net(s_mensuel, taux)
    print(f"Votre salaire mensuel net est de {net:.2f} euros.")

if __name__ == "__main__":
    main()
