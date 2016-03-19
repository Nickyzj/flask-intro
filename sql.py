import sqlite3

with sqlite3.connect("sample.db") as connection:
    c = connection.cursor()
    c.execute("""drop table posts""")
    c.execute("""create table posts(title TEXT, description TEXT)""")
    c.execute('insert into posts values("Good", "I am good.")')
    c.execute('insert into posts values("Well", "I am well.")')