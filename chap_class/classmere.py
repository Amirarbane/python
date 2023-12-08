class Equipement:
    def __init__(self,nom,modele) :
        self.nom = nom
        self.modele = modele
        
    
    def afficher(self):
        print("Ici je suis dans la classe Equipement")
        print(f" {self.nom} ")

        print(f" {self.modele}  ")

   


class Network_device(Equipement):
    def __init__(self,ip,masque,model,nom):
        super().__init__(nom,model)
        self.ip = ip
        self.masque = masque
        

    def afficher(self):
        print("Ici je suis dans la classe Network_device")

        print(f"Le {self.nom} {self.ip}")
        print(f"Le {self.nom} est un {self.masque} ")

    
        

    

class Switch(Network_device):
    def __init__(self, nom, modele,ip,masque,port):
        super().__init__(nom,modele,ip,masque)
        self.port = port
    
    def afficher(self):
        print("Ici je suis dans la classe Switch")

        print(f"Le {self.nom} a un {self.port}")


class server(Network_device):
    def __init__(self, nom, modele,ip,masque,port,os):
        super().__init__(nom,modele,ip,masque,port)
        self.os = os
    
    def afficher(self):
        print("Ici je suis dans la classe Server")
        print(f"Le {self.nom} a un {self.os}")


        
print("*"*20+"Classe Equipement")

monEquipement = Equipement("Computer", "HP")
monEquipement.afficher()


print("*"*20+"Classe Network8device")

monEquipement = Network_device("Raspberry","RPI4","192.168.1.100","/24")
monEquipement.afficher()



print("*"*20+"Classe Switch")

monEquipement = Switch("Cisco","1280","192.168.5.200","/24",24)
monEquipement.afficher()


print("*"*20+"Classe Switch")

monEquipement = Switch("Cisco","1280","192.168.5.200","/24",24,'Windows')
monEquipement.afficher()
