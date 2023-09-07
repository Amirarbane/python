import random
nb1 = random.randint(1,100)
nb2 = random.randint(1,100)

saisie = int(input(f"Entrer la somme des deux nombre {nb1} et {nb2}: "))

if saisie == nb1 + nb2:
    print("Bravo")
else:
    print("Grrrrrrrrrrrrrrrrr")


