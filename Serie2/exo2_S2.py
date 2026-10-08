name= input("Saisissez votre prénom : ")

if name == "Julie":
    print(f"Bienvenue {name}")
else:
    print("Dehors")

note=int(input("Saisissez votre note : "))

if note < 12:
    print("Pas de mention")
elif note >= 12 and note < 14:
    print("Assez bien")
elif note >= 14 and note < 16:
    print("Bien")
else:
    print("Très bien")