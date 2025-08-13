import pymysql

try:
    db=pymysql.connect(host='localhost',user='root',password='',database='morningdb')
    print("Database connected!")
except Exception as e:
    print(e)

cr=db.cursor()
#Table Create
tbl_create="create table studinfo(id integer primary key auto_increment, name text, city text)"

try:
    cr.execute(tbl_create)
    print("Table created!")
except Exception as e:
    print(e)


#Insert Data
"""insert_data="insert into studinfo(name, city)values('sanket','rajkot'),('nirav','baroda'),('ashok','surat'),('hitesh','jamnagar')"

try:
    cr.execute(insert_data)
    db.commit()
    print("Record Inserted!")
except Exception as e:
    print(e)"""

#Show Data
show_data="select * from studinfo"
try:
    cr.execute(show_data)
    data=cr.fetchall()
    #print(data)

    for i in data:
        print(i)
except Exception as e:
    print(e)