ng = input("Choisissez le premier nombre : ")
nd = input("Choisissez le deuxième nombre : ")

if not (ng.isnumeric() and nd.isnumeric()):
    print("Erreur : les nombres doivent être des nombres entiers")
    exit()

ng = int(ng)
nd = int(nd)

resultat = 0

operation = input("Choisissez un opérateur (+, -, *, /) : ")
match operation:
    case "+":
        resultat = ng + nd
        print(f"La somme de {ng} et {nd} est {resultat}.")
    case "-":
        resultat = ng - nd
        print(f"La soustraction de {ng} et {nd} est {resultat}.")
    case "*":
        resultat = ng * nd
        print(f"La multiplication de {ng} et {nd} est {resultat}.")
    case "/":
        if nd != 0:
            resultat = ng / nd
            print(f"La division de {ng} et {nd} est {resultat}.")
        else:
            print("Erreur : impossible de diviser par zéro.")
            exit()
    case _:
        print("Erreur : le symbole d'opération doit être '+', '-', '*' ou '/'.")
        exit()