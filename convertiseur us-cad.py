# Auteurs :  Thibaut Diabaka
# Date : 22 janvier 2026
# Description : Calcul du prix total en USD, conversion en CAD et ajout de commission.

# Demander à l'utilisateur de rentrer le nombre d'articles vendus
article = int(input("Entrez le nombre d'articles vendus : "))

# Demander à l'utilisateur de rentrer le prix d'un article en USD
prix_usd = float(input("Entrez le prix d'un article en USD : "))

# Demander à l'utilisateur de rentrer le taux de conversion de USD vers CAD
taux = float(input("Veuillez entrer le taux : "))

# Demander à l'utilisateur de rentrer le montant de la commission bancaire
com_fixe = float(input("Entrez le montant de la commission bancaire : "))

# --- TRAITEMENT (Calculs) ---

# 1. Calculer le montant total en USD
total_usd = article * prix_usd

# 2. Convertir immédiatement en CAD
total_cad = total_usd * taux

# 3. Calculer la commission bancaire
# La consigne dit : "par tranche complète de 100 CAD"
# On utilise // (division entière) sur le montant EN CAD
nb_tranches = total_cad // 100
montant_commission = nb_tranches * com_fixe

# 4. Calculer le total final à payer
total_final = total_cad + montant_commission

# --- AFFICHAGE (Sorties) ---
# Utilisation des f-strings pour limiter à 2 décimales
print(f"Le montant en USD est : {total_usd:.2f}")
print(f"Le montant en CAD est : {total_cad:.2f}")
print(f"La commission bancaire est : {montant_commission:.2f}")
print(f"Le montant total à payer en CAD est : {total_final:.2f}")