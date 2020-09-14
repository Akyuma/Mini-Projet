def chasse(poules = int, chiens = int, vaches = int, amis = int) :
    total = poules + chiens + vaches + amis
    if total < 100 :
        print ("Il faudra payer 1 permis : 200 €")
    else :
        prix = total / 100
        prix = round(prix)
        prix = 200 * prix
        print ("Il faudra payer ",compteur,"permis : ",prix," €")



poules = int(input(" poules : "))
chiens = int(input(" chien : "))
vaches = int(input(" vache : "))
amis = int(input(" ami : "))
chiens = chiens * 3
vaches = vaches * 5
amis = amis * 10


print(chasse(poules , chiens , vaches , amis))
