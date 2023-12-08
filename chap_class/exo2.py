class Device:
    

    def __init__(self,marque,taille,resolution) -> None:
        self._marque= marque 
        self._taille = taille
        self._resolution = resolution

    def _get_marque(self):

        return self._marque
    

    def _get_taille(self):

        return self._taille
    
    def _get_resolution(self):

        return self._resolution
    


    def _set_marque(self,newValue):

         self._marque = newValue


    def _set_taille(self,newValue):

         self._taille = newValue

    def _set_resolution(self,newValue):

         self._resolution = newValue

    def convertir(self):
      
        print(f"La taille en cm : {self._taille * 2.5}")
        return self._taille * 2,54 

    
    def afficher(self):
        print(f" marque de la TV : {self.marque} \n Taille : {self.taille} pouce \n resolution : {self.resolution}")

    



    marque = property(_get_marque,_set_marque)
    taille = property(_get_taille,_set_taille)
    resolution = property(_get_resolution,_set_resolution)


maTV = Device(f"SamSung",50,1080)
maTV.afficher()
maTV.convertir()
