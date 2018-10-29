pizza = 750
studentrabatt = 0.2
tips = 0.08
total = (pizza*(1 + tips)*(1 - studentrabatt))
print("total pris", total)
deltakere = int (input ("Hvor mange deltok på middagen?"))
print ("Ettersom dere var", deltakere, "personer, så må hver person betale", total / deltakere, "kroner")
