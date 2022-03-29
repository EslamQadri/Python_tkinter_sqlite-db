'''import sqlite3
db = sqlite3.connect("database")
cur=db.cursor()
cur.execute("create TABLE BOOK ( 'ID' text , 'BOOK_TITLE'  TEXT,  'Auther'  TEXT,  'Summery'  TEXT,  'price'  text)")
db.commit()'''


def reset ():
    import sqlite3
    db = sqlite3.connect("database")
    cur=db.cursor()
    cur.execute("DELETE  FROM BOOK ;")
    db.commit()

def delete_by_Id(id):
    import sqlite3
    db = sqlite3.connect("database")
    cur=db.cursor()
    cur.execute("DELETE FROM BOOK WHERE ID =(?)",(id))
    db.commit()




def insert_to_database(id ,booktitle,auther,summery,price):
    import sqlite3
    db = sqlite3.connect("database")
    cur=db.cursor()
    print(id,booktitle,auther,summery,price,sep="\n")
    cur.execute("INSERT INTO BOOK VALUES(?,?,?,?,?)",(id,booktitle,auther,summery,price))
    db.commit()


def save_database():
    import sqlite3
    db = sqlite3.connect("database")
    db.commit()

