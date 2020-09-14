poids = int(input("poids : "))
quantité = int(input("quantité"))
n = 4
lions = [198000,
        198000]
tigres = [180000,
         170000]
elephants = [250000,
            200000]
guépards = [130000,
           100000]
liste = [
         lions,
         tigres,
         elephants,
         guépards
        ]

compteur = 0
haruhi = quantité / poids
for i in liste :
        rapport = i[1] / i[0]
        if rapport > haruhi :
            compteur += 1
        else :
            compteur = compteur