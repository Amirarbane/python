






class Device:

    """
    ceci est un commentaire
    





    """
    

    def __init__(self,ipAdress,nom,macAdress) -> None:
        self._ipAdress = ipAdress
        self._nom = nom
        self._macAdress = macAdress

    def _get_ipAdress(self):

        return self._ipAdress
    

    def _get_nom(self):

        return self._nom
    
    def _get_macAdress(self):

        return self._macAdress
    


    def _set_ipAdress(self,newValue):

         self._ipAdress = newValue


    def _set_nom(self,newValue):

         self._nom = newValue

    def _set_macAdress(self,newValue):

         self._macAdress = newValue


    def __getattr__(self,valeur):
        return f"WARNING !!!! l atribut {valeur} est incorrect"

    def __doc__(self):
       
       pass

    def __str__(self):
        return f"Votre routeur ce nomme {self.nom} \nSon ip est : {self.ipAdress} \nL'ip mac est {self.macAdress}" 
    

    
    
    
    ipAdress = property(_get_ipAdress,_set_ipAdress)
    nom = property(_get_nom,_set_nom)
    macAdress = property(_get_macAdress,_set_macAdress)






        

