
valeur = randint(0,100)
essai = int(input("essai : "))
compteur = 1
while essai != valeur :
    compteur = compteur + 1
    if essai < valeur :
        print("trop petit")
    else :
        print("trop grand")
    essai = int(input("essaye encore : "))
print ("Gagné")
print ("nombre d'essai : ",compteur)