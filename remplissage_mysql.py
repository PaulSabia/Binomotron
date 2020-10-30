import MySQLdb

db = MySQLdb.connect(host="localhost",  
                     user="root",  
                     passwd="root",  
                     db="binomotron",
                     port=8081)  

print("Connection réussie")

cursor = db.cursor()

#Remplir la base de donnée:
prenoms = ['Luigi', 'Amaury', 'Thomas', 'Erwan', 'Julien', 'Céline', 'Pereg', 'Jamal', 'Christelle', 'Baptiste', 'Baptiste', 'Jérémy',
'Patricia', 'Ludivine', 'Christian', 'Eva', 'Aude', 'Ronan', 'Paul', 'Guillaume']

noms= ['BOKALLI','BONNEAU','CHAIGNEAU','CLOATRE','FURIGA','GUILLEN',"HERGOUALC'H",'IBANNI','KARFAOUI','LE BERRE','LE GOFF', 'LE JONCOUR',
'LE MOAL','MAINTIER','MBARGA MVOGO','MOULARD','PERTRON','RIOUAL','SABIA','VERPOEST']

SQL = ("INSERT INTO apprenants(id_apprenant, nom_apprenant, prenom_apprenant) VALUE(%s, %s, %s)")

for i in range(20):
    value = (None, noms[i], prenoms[i])
    cursor.execute(SQL, value)
    db.commit()

groupes = ["Groupe 1", "Groupe 2", "Groupe 3", "Groupe 4", "Groupe 5", "Groupe 6", "Groupe 7", "Groupe 8", "Groupe 9", "Groupe 10" ,
 "Groupe 11", "Groupe 12", "Groupe 13", "Groupe 14", "Groupe 15", "Groupe 16", "Groupe 17", "Groupe 18", "Groupe 19", "Groupe 20"]

SQL2 = ("INSERT INTO groupes(id_groupe, libelle_groupe) VALUE(%s,%s)")

for i in range(20):
    value2 = (None, groupes[i])
    cursor.execute(SQL2, value2)
    db.commit()

db.close()
print("Connection fermé")