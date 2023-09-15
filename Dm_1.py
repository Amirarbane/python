print("********Bienvenue au restaurant PyFood**********")





print("les entrees")
print("1- Salade de chef                  12 euros")
print("2- Salade niçoise                  10 euros")
print("3- Salade grecque                  9 euros")
print("4- Salade italienne                11 euros")


choix_entree = 0

while choix_entree == 0:
    choix_entree_str= input("\n Choisiser votre entrée :   ")
    try :

        choix_entree= int(choix_entree_str)
    except:
        print("Pas de lettre stp")
    else:
        if choix_entree == 0:
            print("zéro")
        elif choix_entree > 4:
            print("Aucun choix correspondant")
            choix_entree = 0
        elif choix_entree < 0:
            print("Négatif")
            choix_entree = 0
        else:




            if choix_entree == 1 : 
                print("Vous avez choisi: la Salade de chef.  ")
                prix_entree=12

            elif choix_entree == 2:
                print("Vous avez choisi: la Salade niçoise.  ")
                prix_entree=10

            elif choix_entree == 3:
                print("Vous avez choisi: la  Salade grecque . ")
                prix_entree=9

            elif choix_entree == 4:
                print("Vous avez choisi: la Salade italienne.  ")
                prix_entree=11


print("\n les plats")
print("1- friture de poisson                  25 euros")
print("2- Bavette de veau                     19 euros")
print("3- Saumon a la plancha                 22 euros")
print("4- Boeuf bourguignon                   16 euros")



choix_plat= input("\n Choisiser: votre entree :  ")

if choix_plat== "1" : 
    print("Vous avez choisi: la friture de poisson . ")
    prix_plat=25

elif choix_plat == "2":
    print("Vous avez choisi: la Bavette de veau . ")
    prix_plat=19

elif choix_plat == "3":
    print("Vous avez choisi: la  Saumon a la plancha .")
    prix_plat=22

elif choix_plat == "4":
    print("Vous avez choisi: la Boeuf bourguignon.")
    prix_plat=16


print(" \n les dessert")
print("1- creme brulée                  7 euros")
print("2- Tiramissu                     8 euros")
print("3- Glace au choix                9 euros")
print("4- Panacota                      6 euros")



choix_dessert= input("\n  Choisiser: votre entree :  ")

if choix_dessert== "1" : 
    print("Vous avez choisi: la creme brulée  ")
    prix_dessert=7

elif choix_dessert== "2":
    print("Vous avez choisi: le Tiramissu   ")
    prix_dessert=8

elif choix_dessert == "3":
    print("Vous avez choisi: une Glace au choix   ")
    prix_dessert=9

elif choix_dessert == "4":
    print("Vous avez choisi: un Panacota  ")
    prix_dessert=6


Total = prix_entree + prix_plat + prix_dessert

print("Total a payer : " ,Total,"€")


