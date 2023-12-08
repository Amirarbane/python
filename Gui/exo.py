from PySide6 import QtWidgets
import sys

class MaFenetre(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.resize(300,100)
        self.setWindowTitle("BTS SNIR2 - QDialog")
        self.create_layouts()
        self.create_widgets()
        self.addWigets_to_layouts()
        self.setup_connections()
        # self.main_widget()


    def create_layouts(self):
        self.layoutV = QtWidgets.QVBoxLayout()
        self.layoutH1 = QtWidgets.QHBoxLayout()
        self.layoutH2 = QtWidgets.QHBoxLayout()

    def create_widgets(self):
        self.lbl_Nom = QtWidgets.QLabel("Nom")
        self.LEdit_Nom = QtWidgets.QLineEdit()
        self.LEdit_Nom.setPlaceholderText("Saisir votre nom")
        self.btn_Effacer = QtWidgets.QPushButton("Effacer")
        self.btn_Quitter = QtWidgets.QPushButton("Quitter")

    def addWigets_to_layouts(self):
        self.layoutH1.addWidget(self.lbl_Nom)
        self.layoutH1.addWidget(self.LEdit_Nom)
        self.layoutH2.addWidget(self.btn_Effacer)
        self.layoutH2.addWidget(self.btn_Quitter)
        self.layoutV.addLayout(self.layoutH1)
        self.layoutV.addLayout(self.layoutH2)
        self.setLayout(self.layoutV)

    # def main_widget(self):
    #     self.widget = QtWidgets.QWidget(self)  
    #     self.widget.setLayout(self.layoutV)
    #     self.setCentralWidget(self.widget)
       
    def setup_connections(self):
        self.btn_Quitter.clicked.connect(quit)
        self.btn_Effacer.clicked.connect(self.clear_Ledit)
         
    def clear_Ledit(self):
        self.LEdit_Nom.setText("")

    

if __name__ == '__main__':
    # Create the Qt Application
    app = QtWidgets.QApplication([])
    # Create and show the form
    form = MaFenetre()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())
    # app.exec()