# Auteurs :  Thibaut Diabaka
# Date : 22 janvier 2026


# Demander à l'utilisateur d'entré son nom minimum 3  lettres
nom= str(input("Entrez votre nom : "))

# Demander à l'utilisateur d'entré son prénom minimum 2  lettres
prenom=str(input("Entrez votre prénom : "))

# Demander à l'utilisateur d'entré son année de naissance minimum 4 chiffres
daten = int(input("Entrez votre date de naissance : "))

# Afficher
print("merci!")
print(f"votre nom d'utilisateur est :{nom.upper()}_{ prenom[0]}{daten} ")
print(f"votre mot de passe est :{prenom.upper()[:2]}{ nom[3:]}{daten%100} ")