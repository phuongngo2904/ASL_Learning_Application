import sqlite3

def run_db():
    con = sqlite3.connect('users.db')
    mycursor = con.cursor()
    mycursor.execute("DROP TABLE IF EXISTS users.user_table;")

    mycursor.execute("""
    CREATE TABLE IF NOT EXISTS user_table (
                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    username TEXT NOT NULL,
                    email TEXT NOT NULL,
                    fname TEXT NOT NULL,
                    minit TEXT,
                    lname TEXT NOT NULL,
                    password TEXT NOT NULL);""")

    mycursor.execute("INSERT INTO user_table(username, email,fname,minit,lname,password) VALUES"
                 "('admin','phuong.ngo@sjsu.edu','Phuong','L','Ngo','helloworld');")
    con.commit()
    con.close()

