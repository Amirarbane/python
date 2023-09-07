# Déclaration des variables:

age =  19          #entier                  ==> int
note = 19.5         #Flottant                ==> float
nom = "Amir"        #Chaine de caractères    ==> str
age_str1 = '19'     #Attention '19' est un str
age_str2 = "20"     #Attention "20" est un str

#Affichage de type de la variable avec la fonction type(variable)
print("\nLe type de la variable age",type(age))
print("Le type de la variable note",type(note))
print("Le type de la variable nom",type(nom))
print("Le type de la variable age_str1",type(age_str1))
print("Le type de la variable age_str1",type(age_str1))

#Affichage et formatage avec la fonction print
print("\nVous vous appelez", nom, "et vous avez", age, "ans.")# \n pour sauter une ligne
print("Vous vous appelez " + nom + " et vous avez " + str(age) + " ans.")
print("Vous vous appelez" + " " + nom +  " " + "et vous avez" + " " + str(age) +  " " + "ans.")
print("Vous vous appelez {} et vous avez {} ans.".format(nom, age ))
print("Vous vous appelez %s et vous avez %s ans."%(nom, age ))
# print(f"Vous vous appelez {nom} et vous avez {age} ans.") #A partir de python 3.6