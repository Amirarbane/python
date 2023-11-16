import os
import re
import subprocess

def ScanMacAdress():
    chemin = r"Scanmap.txt"
    contenu = ""

    with open(chemin, "r") as f:
        contenu = f.read()

    adresses_mac = re.findall(r"([0-9A-Fa-f]{2}(?:[:-][0-9A-Fa-f]{2}){5})", contenu)
    adresses_mac_complet = [f" {mac}" for mac in adresses_mac]
    print(adresses_mac_complet)

    return adresses_mac_complet

def ScanIpAdress():
        chemin = r"Scanmap.txt"
        contenu = ""

        with open(chemin, "r") as f:
            contenu = f.read()

        adresses_ip = re.findall(r"((?:[0-9]{1,3}\.){3}[0-9]{1,3})", contenu)
        adresses_ip_complet = [f"{ip}" for ip in adresses_ip]
        print(adresses_ip_complet)
        return adresses_ip_complet


ScanMacAdress()
ScanIpAdress()




