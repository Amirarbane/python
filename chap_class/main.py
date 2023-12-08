from exo1 import Device
import uuid


macAdress = (hex(uuid.getnode()))

routeur = Device("192.168.1.20","Cisco 1945",macAdress[2:])
routeur.afficher()