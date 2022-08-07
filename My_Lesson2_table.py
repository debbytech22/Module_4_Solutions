import sqlite3
conn=sqlite3.connect("student.db")
print("successfully import module")
print("database successfully created");print(type(conn))
cursor = conn.cursor()
# cursor.execute("""
#  CREATE TABLE Students(
#       first_name text,
#       last_name text,
#       email text,
#       course text
#   )
#   """
#   )
conn.commit()

Students_List = [
("Abubakar","Adisa","adisaabubakar@gmail.com","Data science"),
("Adebisi","Afolabi","wasola.afolabi@yahoo.com","Data science"),
("Adedoyin","Abass","doyinabass@gmail.com","Data science"),
("Awonaike","Tawa","purpleduralumin@gmail.com","Data science"),
("Babajide","Adesugba","jide@hotmail.com","Data science"),
("Bukola","Ajayi","bukolam.ajayi@gmail.com","Data science"),
("Bintar","Umar","ubinta63@yahoo.com","Data science"),
("Christian","Uzondu","uzonduchristian2@gmail.com","Data science"),
("Cynthia","Awiya","awiyac@yahoo.com","Data science"),
("Deborah","Olorunishola","deboraholuwatobi247@gmail.com","Data science"),
("Eke","Ihuoma","ihuomaeke28@gmail.com","Data science"),
("Esther","Akpanowo","estherakpanowo@gmail.com","Data science"),
("Eniola","Osadare","dorcasosadare@gmail.com","Data science"),
("Etariami","Louis","etariamilouis@gmail.com","Data science"),
("Faith","Amure","amuretalodabif@gmail.com","Data science"),
("Ganiyat","Shittu","ganiyatas@gmail.com","Data science"),
("Gideon","Uko","ukogideon@gmail.com","Data science"),
("Idowu","Adesanya","idsworld22@yahoo.com","Data science"),
("Joyce","Ezeonwu","joyceokore@gmail.com","Data science"),
("Kehinde","Orolade","Kehindeorolade@gmail.com","Data science"),
("Kafayat","Ibrahim","kafayatadenike10@yahoo.com","Data science"),
("Lawrence","Aneshumoka","anelawrence1@gmail.com","Data science"),
("Mariam","Adeoti","adetutuadebola28@gmail.com","Data science"),
("Ogechi","Njemanze","ogejemz@gmail.com","Data science"),
("Omowumi","Awonirana","mowunmiii@gmail.com","Data science"),
("Placidus","Ali","placidusali@gmail.com","Data science"),
("Praise","Emmanuel","praiseemannuel9ic@gmail.com","Data science"),
("Prince","Ekeocha","prince.ekeocha@gmail.com","Data science"),
("Rasheedat","Sikiru","rasheedatsikiru@gmail.com","Data science"),
("ramotallah","Jubril","jubrilramotallah@gmail.com","Data science"),
("sheriff","azeez","Sheriffolaitan@gmail.com","Data science"),
("Stephen","Ogungbile","stephenfunso@gmail.com","Data science"),
("temitope","Bamidele","bamideletemitope24@gmail.com","Data science"),
("Theresa","karamor","teriekar@gmail.com","Data science"),
("Tina","Uyateide","tinauyats@gmail.com","Data science"),
("Victoria","Ckukwuno","Chukwunorvictoria@gmail.com","Data science")
]
print("created successfully")
cursor.executemany(
    "INSERT INTO Students VALUES (?,?,?,?)", Students_List    
)
print("we have inserted values into student table")
conn.commit()
conn.close()
