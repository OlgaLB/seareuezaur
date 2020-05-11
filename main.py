#!/usr/bin/env python3

from lib.credentials import Connection
from populate import populate_table
import os
import mysql.connector


if __name__ == "__main__":
    conn = mysql.connector.connect(host=Connection.MYSQL_HOST, 
                                   user=Connection.MYSQL_USER_ROOT, 
                                   password = Connection.MYSQL_PASSWORD_ROOT, 
                                   db = Connection.MYSQL_DB)
    cursor = conn.cursor()

    queries_list = []
    with open(os.path.join('db', 'airports_db_v1.0.0.sql')) as queries_file:
        queries = queries_file.read()
        queries_list = queries.split(';\n')
        queries_list = list(filter(None, queries_list))

    for query in queries_list:
        cursor.execute(query)

    cursor.close()
    conn.close()

    populate_table(os.path.join('db','airports.csv'))
