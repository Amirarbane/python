import sqlite3

# def creer_bdd():
#         conn = sqlite3.connect("madatabase.db")
#         c = conn.cursor()
#         c.execute("""
#         CREATE TABLE IF NOT EXISTS personne
#         (
#             prenom text,
#             nom text

#         )
#         """)


#         conn.commit()
#         conn.close()
#         print("La table a été créée")

# creer_bdd()

conn = sqlite3.connect("madatabase.db")
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS personne
(
    prenom text,
    nom text

)
""")

conn.commit()
conn.close()
print("La table a été créée")