import sqlite3
conn=sqlite3.connect("student.db")
print("successfully import module")
print("database successfully created");print(type(conn))
cursor = conn.cursor()

cursor.execute(
    """
    SELECT * FROM Students
"""
)
items=cursor.fetchall()
print("first name" + "\t surname" +"\t email" +" \t\t\t\t  course\n"f"{'.'*100}")
print("----------" + "\t--------" +"\t---------" + "\t\t----------")

for item in items:
    first_name,last_name,email ,course = item
    print(f"{first_name:16}\t{last_name:16}{email:30}\t\t{course}")
  
conn.commit()
conn.close()
