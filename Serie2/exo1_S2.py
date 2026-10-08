note=int(input("Saisissez la valeur :"))

if note <= 10:
    print("très faible")
elif note <= 30:
    print("faible")
elif note <= 60:
    print("moyen")
elif note <= 90:
    print("bien")
else:
    print("très bien")