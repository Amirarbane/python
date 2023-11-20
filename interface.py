from PySide6 import QtWidgets, QtCore
import subprocess
import time
from scanmap import ScanMacAddress, ScanIpAddress,Nomfabricant

class MaFenetre(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.resize(700, 500)
        self.setWindowTitle("Scan Réseau")
        self.create_layouts()
        self.create_widgets()
        self.addWigets_to_layouts()
        self.setup_connections()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.rafraichir)

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
        self.text_edit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)

        self.progress_bar = QtWidgets.QProgressBar()
        self.progress_bar.setRange(0, 100)

    def addWigets_to_layouts(self):
        self.layoutH0.addWidget(self.btn_Analyser)
        self.layoutH1.addWidget(self.btn_Rafraichir)
        self.layoutH2.addWidget(self.btn_Quitter)

        self.layoutV.addLayout(self.layoutH0)
        self.layoutV.addLayout(self.layoutH1)
        self.layoutV.addLayout(self.layoutH2)
        self.layoutV.addWidget(self.progress_bar)

        # Ajouter un QLabel pour afficher les informations
        self.label_info = QtWidgets.QLabel("  id""\t        Adresse IP"" \t\t  Adresse Mac""\t           Nom Fab")
        self.label_info.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.layoutV.addWidget(self.label_info)
        self.layoutV.addWidget(self.text_edit)
        self.setLayout(self.layoutV)
    def setup_connections(self):
        self.btn_Quitter.clicked.connect(quit)
        self.btn_Analyser.clicked.connect(self.analyser)
        self.btn_Rafraichir.clicked.connect(self.rafraichir)

    def analyser(self):
        self.text_edit.setReadOnly(True)
        self.progress_bar.setValue(0)  # Réinitialiser la barre de progression
        adresses_ip_liste = ScanIpAddress()
        adresses_mac_liste = ScanMacAddress()
        nom_fabl_iste = Nomfabricant()

        max_len_mac = max(len(mac) for mac in adresses_mac_liste)
        espacement = 20

        # Construction de la chaîne avec plus d'espacement et ajout du compteur
        texte_final = ""
        total_items = len(adresses_ip_liste)

        for i, (ip, mac,fab) in enumerate(zip(adresses_ip_liste, adresses_mac_liste,nom_fabl_iste), start=1):
            espace_mac = " " * (max_len_mac - len(mac) + espacement)
            texte_final += f"{i}.\t{ip.ljust(15)}\t{mac}\t{fab}\n"

            # Mise à jour de la valeur de la barre de progression
            progress_value = int((i / total_items) * 100)
            self.progress_bar.setValue(progress_value)

            # Rafraîchir l'interface graphique
            QtWidgets.QApplication.processEvents()

            # Ajouter une pause (simulant le traitement d'une entrée)
            time.sleep(0.03)  # Ajustez la durée de pause

        self.text_edit.setPlainText(texte_final)

    def rafraichir(self):
        self.text_edit.setReadOnly(True)
        self.progress_bar.setValue(0)  # Réinitialise la barre de progression
        try:
            commande = "echo ciel | sudo -S arp-scan --localnet > scanmap.txt"
            subprocess.run(commande, shell=True, check=True, input=b'ciel\n')
        except subprocess.CalledProcessError as e:
            print(f"Erreur lors de l'exécution de la commande")

        adresses_ip_liste = ScanIpAddress()
        adresses_mac_liste = ScanMacAddress()
        nom_fab_liste = Nomfabricant()

        max_len_ip = max(len(ip) for ip in adresses_ip_liste)
        max_len_mac = max(len(mac) for mac in adresses_mac_liste)
        max_len_fab = max(len(fab) for fab in nom_fab_liste)
        espacement = 20

        # Construction de la chaîne avec plus d'espacement et ajout du compteur
        texte_final = ""
        total_items = len(adresses_ip_liste)
        for i, (ip, mac, fab) in enumerate(zip(adresses_ip_liste, adresses_mac_liste, nom_fab_liste), start=1):
            espace_ip = " " * (max_len_ip - len(ip) + espacement)
            espace_mac = " " * (max_len_mac - len(mac))
            texte_final += f"{i}.\t{ip.ljust(15)}\t{mac}\t{fab}\n"

            # Update progress bar value
            progress_value = int((i / total_items) * 100)
            self.progress_bar.setValue(progress_value)
            time.sleep(0.01)  # Ajustez la durée de pause
            self.text_edit.clear()
            self.text_edit.setPlainText(texte_final)


app = QtWidgets.QApplication([])
form = MaFenetre()
form.show()
app.exec()