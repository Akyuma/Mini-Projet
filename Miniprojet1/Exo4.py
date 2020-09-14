
prix_HT = float(input("prix HT : "))
tax = 0.2
TTC = 0
fin = 1
while fin != 0 :
    tax = prix_HT * tax
    TTC = prix_HT + tax
    fin = 0
print(TTC," €")