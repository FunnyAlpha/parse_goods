import datetime

print(datetime.datetime.now().strftime("%Y-%m-%d"))

print("https://goods.ru/catalog/details/voda-mineralnaya-novoterskaya-gazirovannaya-15-l-plastik-100022961239/"[-13:-1])

import psycopg2

hostname = 'localhost'
username = 'postgres' # the username when you create the database
password = 'Fender1580' #change to your password
database = 'goods_parsing'

def queryQuotes( conn ) :
    cur = conn.cursor()
    cur.execute( """select * from products""" )
    rows = cur.fetchall()

    print("vse_ok")

    for row in rows :
        print (row[1])

conn = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
queryQuotes( conn )
conn.close()