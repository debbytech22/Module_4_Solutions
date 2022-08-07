import sqlite3
print("successful")
conn = sqlite3.connect("celebb_infor.db")
c = conn.cursor()
# c.execute("""CREATE TABLE Celebrity_info(
#      NAME TEXT,
#      GENRE TEXT,
#      NUM_ALBUM INTEGER,
#      AGE INTEGER,
#      AWARD INTEGER,
#      YEARS_IN_INDUSTRY INTEGER)
#  """)

celebrity_record =[
    ("Micheal_Jackson","hip_pop",10,45,54,15),
    ("Reminesce","Apala",5,32,3,15),
    ("olamide","Regea",5,46,8,16),
    ("Wizkid","Afrobeat",6,18,12,3),
    ("Davido","Juju",2,22,6,5),
    ("Tiwa_Savage","Afrobeat",5,36,7,8),
    ("Palace","Samba",5,44,7,14),
    ("Mercy","Makossa",10,64,20,35),
    ("Faze","jazz",14,40,11,23),
    ("Falz","pop",5,33,6,11),
    ("Beyonce","Juju",10,40,15,12),
    ("Rihanna","Afro_pop",20,38,17,10),
    ("sound_sultan","juju",15,44,20,15),
    ("Recado","reggea",5,47,8,9),
    ("Dbanj","apala",19,40,20,25),
    ("Kiss_kid","jazz",13,28,9,14),
    ("wasiu_ayinde","juju",47,23,30,15),
    ("pasuma","juju",17,50,30,36),
    ("Timaya","blues",27,49,21,18)
]
c.executemany(
    "INSERT INTO Celebrity_info VALUES (?,?,?,?,?,?)", celebrity_record
)
print("suceesfully installed")


#The most decorated celebrity
c.execute("""
SELECT NAME,MAX(AWARD)
fROM Celebrity_info
""")
item = c.fetchall()
print(item)

#The oldest celebrity
c.execute("""
SELECT NAME,MAX(AGE)
fROM Celebrity_info
""")
item = c.fetchall()
print(item)


c.execute("""
SELECT NAME,MAX(YEARS_IN_INDUSTRY )
fROM Celebrity_info
""")
item = c.fetchall()
print(item)


#Celelebrity with with least number of albums
c.execute("""
SELECT NAME,MIN(NUM_ALBUM )
fROM Celebrity_info
""")
item = c.fetchall()
print(item)

c.execute("""
SELECT MAX(GENRE )
fROM Celebrity_info
""")
item = c.fetchall()
print(item)
conn.commit()
conn.close()
