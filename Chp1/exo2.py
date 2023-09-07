
note1 =int(input("Enter une note de math:  "))
note2 =int(input("Enter une note de français:  "))
note3 =int(input("Enter une note d anglais :  "))


moyenne= int((note1+note2+note3)/3)

print("votre moyenne est de : " ,moyenne)

if moyenne>= 18 :
    
    print("Exellent!")

if 14<= moyenne< 18 :
    
    print("tres bien!")

if 10<= moyenne < 14:
    
    print("assez bien")

if 5<= moyenne < 10:
    
    print("insuffisant")

if moyenne < 5 :
    
    print("Catastrophique")
