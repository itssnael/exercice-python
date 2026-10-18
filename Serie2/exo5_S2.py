# 2. Saisie et découpage
nombres = input("Choisissez une liste de nombres entier séparés par des virgules (par exemple : 1,2,3,4) : ")
decoupage = nombres.split(",")

liste_nombres = []
for element in decoupage:
    liste_nombres.append(int(element))
print(liste_nombres)

# 3. Somme de la liste calculée avec une boucle for
total = 0
for n in liste_nombres:
    total += n
print(f"Le total des nombres de la liste est {total}")
# En une ligne : total = sum(liste_nombres)

# 4. Moyenne
moyenne = total / len(liste_nombres)
print(f"La moyenne des nombres de la liste est {moyenne}")

# 5. Compteur des nombres supérieurs à la moyenne avec une boucle for
sup=0
for i in liste_nombres:
    if i > moyenne:
        sup += 1
print(f"Nombre de nombres supérieurs à la moyenne : {sup}")

# 6. Compteur des nombres pairs avec une bloucle while
nb_pairs = 0
f = 0
while f < len(liste_nombres):
    index = liste_nombres[f]
    if index % 2 == 0:
        nb_pairs += 1
    f += 1
print(f"Nombre de nombres pairs : {nb_pairs}")