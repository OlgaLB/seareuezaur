#!/usr/bin/env python3

import csv

from lib.credentials import Connection
import mysql.connector


from lib.airport import Airport


def populate_table(filename):
    """Populate table (airports) by data read from csv.

        Parameters
        ----------
        filename : str
            Path to csv file.
    """
    conn = mysql.connector.connect(user=Connection.MYSQL_USER, password=Connection.MYSQL_PASSWORD,
                              host=Connection.MYSQL_HOST,
                              database=Connection.MYSQL_DB)
    cursor = conn.cursor()
    
    with open(filename, "r") as f_input:
        csv_input = csv.DictReader(f_input)

        for row in csv_input:
            
            if row['iata_code'] != '':
                airport = Airport(row['name'].replace("'", "\\'"), row['iata_code'].replace("'", "\\'"), row['ident'].replace("'", "\\'"), row['municipality'].replace("'", "\\'"), row['iso_country'].replace("'", "\\'"), row['latitude_deg'].replace("'", "\\'"), row['longitude_deg'].replace("'", "\\'"))
                query = f'INSERT INTO airports (name, iata, icao, city, country, latitude, longitude) VALUES (\'{airport.name}\', \'{airport.iata}\', \'{airport.icao}\', \'{airport.city}\', \'{airport.country}\', {airport.latitude}, {airport.longitude});'
                cursor.execute(query)

                conn.commit()
    cursor.close()
    conn.close()
