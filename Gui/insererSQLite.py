import sqlite3

def ajouter_bdd():    
        conn = sqlite3.connect("madatabase.db")
        c = conn.cursor()

        c.execute("INSERT INTO personne (nom,prenom) VALUES ('Laurent','Louis')")
        c.execute("INSERT INTO personne (nom,prenom) VALUES ('Nantois','Antony')")
        c.execute("INSERT INTO personne (nom,prenom) VALUES ('Schmitt','Charly')")
        c.execute("INSERT INTO personne (nom,prenom) VALUES ('Schmitt','Bruno')")
        c.execute("INSERT INTO personne (nom,prenom) VALUES ('Dauger','Steeve')")
        c.execute("INSERT INTO personne (nom,prenom) VALUES ('Nurmagedov','Khabib')")

        conn.commit()
        conn.close()
        
ajouter_bdd()