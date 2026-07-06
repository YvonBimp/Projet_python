# Auteurs :  Thibaut Diabaka
# Date : 22 janvier 2026


# Demander d'entrer le prix du billet enfant
enfant = float(input("Veuillez entrer le prix du billet enfant : "))

# Demander d'entrer le prix du billet Adulte
adulte = float(input("Veuillez entrer le prix du billet adulte : "))

# Demander d'entrer le prix du billet senior
senior = float(input("Veuillez entrer le prix du billet senior : "))

# Demander d'entrer le nombre de billets enfant vendus
x = float(input("Veuillez entrer  le nombre de billets enfant vendus : "))

# Demander d'entrer le nombre de billets Adulte vendus
y = float(input("Veuillez entrer  le nombre de billets Adulte vendus: "))

# Demander d'entrer le nombre de billets senior vendus
z = float(input("Veuillez entrer  le nombre de billets senior vendus: "))

# Afficher le montant total des ventes de la journée
total = enfant*x + adulte*y +senior*z
print("le total sans taxes des ventes pour la journée   :", total )

# calcule de taxes provinciale
pourcentage_p = 9.975
taxep=total*(pourcentage_p/100)

print(" taxe provincial:", taxep )
# calcule de taxes provinciale federale
pourcentage_f=5
taxef=total*(pourcentage_f/100)
print(" taxe fédéral:", taxef )

# Afficher le montant total des ventes de la journée avec les taxes
total2=total+taxep+taxef
print("le total sans taxes des ventes pour la journée   :", total2 )

