#!/usr/bin/env python3

from lib.credentials import Connection
from flask import Flask, request, json, jsonify
import mysql.connector

from lib.airport import Airport


app = Flask(__name__)


@app.route('/api/IATA', methods=['GET'])
def IATA_search():
    """Endpoint to search airports by IATA

        Parameters
        ----------
        iata : str
            IATA code.

        Output:
            Array of jsons with found airports.
    """
    if not request.args.get('iata'):
        raise ValueError('Missing iata')
    else:
        _iata = request.args.get('iata')

    conn = mysql.connector.connect(host=Connection.MYSQL_HOST, user=Connection.MYSQL_USER, password = Connection.MYSQL_PASSWORD, db = Connection.MYSQL_DB)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM airports WHERE iata LIKE " + "'" + _iata + "'")
    airports_data = cursor.fetchall()

    found_airports = []
    if airports_data is not None:
        for record in airports_data:
            airport = Airport(record[0], record[1], record[2], record[3], record[4], record[5], record[6])
            found_airports.append({
                'name':airport.name, 
                'iata': airport.iata, 
                'icao': airport.icao, 
                'city':  airport.city, 
                'country':airport.country, 
                'latitude': airport.latitude, 
                'longitude': airport.longitude
            })

    cursor.close()
    conn.close()

    return json.dumps(found_airports)


@app.route('/api/name', methods=['GET'])
def name_search():
    """Endpoint to search airports by name

        Parameters
        ----------
        name : str
            Airport name or its part.

        Output:
            Array of jsons with found airports.
    """
    if not request.args.get('name'):
        raise ValueError('Missing name')
    else:
        _name = request.args.get('name')

    conn = mysql.connector.connect(host=Connection.MYSQL_HOST, user=Connection.MYSQL_USER, password = Connection.MYSQL_PASSWORD, db = Connection.MYSQL_DB)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM airports WHERE name LIKE " + "'" + '%' + _name + '%' + "'")
    airports_data = cursor.fetchall()

    found_airports = []
    if airports_data is not None:
        for record in airports_data:
            airport = Airport(record[0], record[1], record[2], record[3], record[4], record[5], record[6])
            found_airports.append({
                'name':airport.name, 
                'iata': airport.iata, 
                'icao': airport.icao, 
                'city':  airport.city, 
                'country':airport.country, 
                'latitude': airport.latitude, 
                'longitude': airport.longitude
            })

    cursor.close()
    conn.close()

    return json.dumps(found_airports)


if __name__ == "__main__":
    
    app.run()
