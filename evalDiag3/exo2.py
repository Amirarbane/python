class DispositifEclairage:
    def __init__(self, identifiant, type_dispositif):
        self.identifiant = identifiant
        self.type_dispositif = type_dispositif
        

    def allumer(self):
        print(f"{self.identifiant} : {self.type_dispositif}")


class AmpouleIntelligente(DispositifEclairage):
    def __init__(self, identifiant, type_dispositif,intensite_luminosite):
        super().__init__(identifiant, type_dispositif )
        self.intensite_luminosite = intensite_luminosite

    def allumer(self):
        print(f" {self.identifiant} {self.intensite_luminosite} lux")


class BandeLEDIntelligente(DispositifEclairage):
    def __init__(self, identifiant, type_dispositif,longeur):
        super().__init__(identifiant, type_dispositif)
        self.longeur = longeur

    def allumer(self):
        print(f" {self.identifiant} {self.longeur} cm")


print("*" * 20 + "Classe DispositifEclairage")
monDispo = DispositifEclairage("Acer", "RGB")
monDispo.allumer()

print("*" * 20 + "Classe AmpouleIntelligente")
monAmpoule= AmpouleIntelligente("Acer : ","RGB",200)
monAmpoule.allumer()

print("*" * 20 + " Classe BandeLEDIntelligente")
maBande = BandeLEDIntelligente("Acer : ","RGB",12)
maBande.allumer()