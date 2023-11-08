import psycopg2

def showData():
    con=psycopg2.connect(dbname='postgres',user='postgres',host='localhost',port='5432',password='755872')
    cur=con.cursor()
    cur.execute("select *from users;")
    records= cur.fetchall()
    con.commit()
    con.close()
    print("--------Your Data-----------")
    data=(set(records))
    return data


def insertData(usname,uspass):
    con=psycopg2.connect(dbname='postgres',user='postgres',host='localhost',port='5432',password='755872')
    cur=con.cursor()
    cur.execute("INSERT INTO users (username,password)VALUES(%s,%s);",(usname,uspass))
    # records= cur.fetchall()
    con.commit()
    con.close()
    print("Insertion Succesful")

print(showData())