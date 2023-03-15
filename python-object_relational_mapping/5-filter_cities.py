#!/usr/bin/python3
"""Script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa"""
import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    statename = sys.argv[4]
    connection = MySQLdb.connect(host="localhost", port=3306, user=username,
                                 passwd=password, db=database)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM cities\
                INNER JOIN states\
                ON cities.state_id = states.id\
                ORDER BY cities.id")
    cities = cursor.fetchall()
    print(", ".join([city[2] for city in cities if city[4] == statename]))

    cursor.close()
    connection.close()
