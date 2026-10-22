def salaire_net(mensuel, prelevement):
    deduction = mensuel*(prelevement/100)
    net = mensuel - deduction
    return net

def salaire_m(salaire_a):
    return salaire_a/12

def salaire_hb(salaire_m):
    return salaire_m/4

def salaire_hr(salaire_hb, heures_travail):
    return salaire_hb/heures_travail