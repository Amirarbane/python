import re


def ScanMacAddress():
    chemin = r"scanmap.txt"
    contenu = ""

    with open(chemin, "r") as f:
        contenu = f.read()

    adresses_mac = re.findall(r"([0-9A-Fa-f]{2}(?:[:-][0-9A-Fa-f]{2}){5})", contenu)
    adresses_mac_complet = [f" {mac}" for mac in adresses_mac]
    print(adresses_mac_complet)

    return adresses_mac_complet

def ScanIpAddress():
        chemin = r"scanmap.txt"
        contenu = ""

        with open(chemin, "r") as f:
            contenu = f.read()

        adresses_ip = re.findall(r"((?:[0-9]{1,3}\.){3}[0-9]{1,3})", contenu)
        adresses_ip_complet = [f"{ip}" for ip in adresses_ip]
        print(adresses_ip_complet)
        return adresses_ip_complet


def Nomfabricant():
    chemin = r"scanmap.txt"
    contenu = ""

    with open(chemin, "r") as f:
        contenu = f.read()

    nom_fab = re.findall(r'\b((?:[A-Z][a-z]+\s?){1,2})', contenu)
    nom_fab_complet = [f"{fab}" for fab in nom_fab]
    print(nom_fab_complet)
    return nom_fab_complet


#ScanMacAddress()
#ScanIpAddress()
#Nomfabricant()



