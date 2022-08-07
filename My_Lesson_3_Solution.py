
import sqlite3
conn=sqlite3.connect("Studentt.db")
c=conn.cursor()
#c.execute("""CREATE TABLE studentts_data(
 #   First_Name TEXT,
  #  Last_Name TEXT,
  #  EMAIL TEXT
#)
#""")
print("sucessful")
Studentts_List = [
("Abubakar","Adisa","adisaabubakar@gmail.com"),
("Adebisi","Afolabi","wasola.afolabi@yahoo.com"),
("Adedoyin","Abass","doyinabass@gmail.com",),
("Awonaike","Tawa","purpleduralumin@gmail.com"),
("Babajide","Adesugba","jide@hotmail.com")]
c.executemany(

     "INSERT INTO Studentts_data VALUES (?,?,?)", Studentts_List    
)
print("inserted values")
c.execute("SELECT*FROM studentts_data")

items=c.fetchall()
print("FIRST_NAME"+ "\t\t\tLAST_NAME" + "\t\t\tE_MAIL " + "\t\t\tCourse")
print("________" + "\t\t\t__________" + "\t\t\t__________" + "\t\t\t")
for item in items:
     print(item[0]  +"\t\t\t" + item[1] +"\t\t\t" + item[2] )

c.execute("ALTER TABLE Studentts_data RENAME TO Studentts_infor")

c.execute("ALTER TABLE Studentts_infor ADD COLUMN Course TEXT")

c.execute("""UPDATE Studentts_infor
SET Course = "Software_Engineering"

""")
print(" Update sucessful")
c.execute("SELECT*FROM studentts_infor")

items=c.fetchall()
print("FIRST_NAME"+ "\t\t\tLAST_NAME" + "\t\t\tE_MAIL " + "\t\t\t\t\tCourse")
print("________" + "\t\t\t__________" + "\t\t\t__________" + "\t\t\t" + "__________")
for item in items:
     print(item[0]  +"\t\t\t" + item[1] +"\t\t\t" + item[2] + "\t\t\t" + item[3])

c.commit()
c.close()


