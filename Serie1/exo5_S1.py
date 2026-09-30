fruits={"pomme":"rouge", "banane":"jaune", "orange":"orange"}
print(fruits)

fruits["kiwi"]="vert"
print(fruits)

couleur_banane=fruits["banane"]
print(f"La couleur de la banane est {couleur_banane}.")

fruits["pomme"]="vert"
print(fruits)

del fruits["banane"]
print(fruits)