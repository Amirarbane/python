from PySide6 import QtWidgets
from PySide6.QtCore import Qt
import subprocess
from ScanReseau import ScanMacAdress
from ScanReseau import ScanIpAdress

class MaFenetre(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.resize(700, 500)
        self.setWindowTitle("Scan Réseau")
        self.create_layouts()
        self.create_widgets()
        self.addWigets_to_layouts()
        self.setup_connections()

    def create_layouts(self):
        self.layoutV = QtWidgets.QVBoxLayout()
        self.layoutH0 = QtWidgets.QHBoxLayout()
        self.layoutH1 = QtWidgets.QHBoxLayout()
        self.layoutH2 = QtWidgets.QHBoxLayout()
        self.layoutH3 = QtWidgets.QHBoxLayout()

    def create_widgets(self):
        self.btn_Analyser = QtWidgets.QPushButton("Analyser")
        self.btn_Rafraichir = QtWidgets.QPushButton("Rafraichir")
        self.btn_Quitter = QtWidgets.QPushButton("Quitter")

        self.text_edit = QtWidgets.QTextEdit()
        self.text_edit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.text_edit2 = QtWidgets.QTextEdit()
        self.text_edit2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

    def addWigets_to_layouts(self):
        self.layoutH0.addWidget(self.btn_Analyser)
        self.layoutH1.addWidget(self.btn_Rafraichir)
        self.layoutH2.addWidget(self.btn_Quitter)
        self.layoutH3.addWidget(self.text_edit)
        self.layoutH3.addWidget(self.text_edit2)

        self.layoutV.addLayout(self.layoutH0)
        self.layoutV.addLayout(self.layoutH1)
        self.layoutV.addLayout(self.layoutH2)
        self.layoutV.addLayout(self.layoutH3)
        self.setLayout(self.layoutV)

    def setup_connections(self):
        self.btn_Quitter.clicked.connect(quit)
        self.btn_Analyser.clicked.connect(self.analyserMac)
        self.btn_Analyser.clicked.connect(self.analyserIp)
        self.btn_Rafraichir.clicked.connect(self.rafraichir)

    def rafraichir(self):
        try:
            commande = "echo ciel | sudo -S arp-scan --localnet > Scanmap.txt"
            subprocess.run(commande, shell=True, check=True, input=b'ciel\n')
            print("Commande exécutée avec succès.")
        except subprocess.CalledProcessError as e:
            print(f"Erreur lors de l'exécution de la commande : {e}")

        adresses_mac_liste = ScanMacAdress()
        texte_adresses_mac = "\n".join(adresses_mac_liste)
        self.text_edit.setPlainText(texte_adresses_mac)

        adresses_ip_liste = ScanIpAdress()
        texte_adresses_ip = "\n".join(adresses_ip_liste)
        self.text_edit2.setPlainText(texte_adresses_ip)

    def analyserMac(self):
        adresses_mac_liste = ScanMacAdress()
        texte_adresses_mac = "\n".join(adresses_mac_liste)
        self.text_edit.setPlainText(texte_adresses_mac)

    def analyserIp(self):
        adresses_ip_liste = ScanIpAdress()
        texte_adresses_ip = "\n".join(adresses_ip_liste)
        self.text_edit2.setPlainText(texte_adresses_ip)

app = QtWidgets.QApplication([])
form = MaFenetre()
form.show()
app.exec()