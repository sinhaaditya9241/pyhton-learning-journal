import psycopg2

def table():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="Adit@92ya41", host="localhost", port="5432")
    cursor = conn.cursor()
    cursor.execute('''create table if not exists employees(name text,number int,ID int,age int);''')
    print('Table created successfully')
    conn.commit()
    conn.close()

def data():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="Adit@92ya41", host="localhost", port="5432")
    cursor = conn.cursor()
    name = input("Enter your name: ")
    number = int(input("Enter your number: "))
    ID = int(input("Enter your ID: "))
    age = int(input("Enter your age: "))

    query = '''insert into employees(name, ID, age)values (%s,%s,%s);'''
   
    cursor.execute(query,(name,ID,age))
    print('Data added successfully')
    conn.commit()
    conn.close()


table()
data()
