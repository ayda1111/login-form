import sqlite3
class Database1:
    def __init__(self,address):
        self.con=sqlite3.connect(address)
        self.cur=self.con.cursor()
        self.cur.execute('''create table if not exists login (firstname
                             text , lastname text  , email text , password integer)''')
        self.con.commit()
    def insert(self,name,lastname,email,password):
        self.cur.execute('insert into login values (?,?,?,?)',(name,lastname,email,password))
        self.con.commit()
    def search(self,email,password):
        self.cur.execute('select * from login where email=? and password= ?',(email,password))
        return self.cur.fetchall()

