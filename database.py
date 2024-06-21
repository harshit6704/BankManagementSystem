# database.py
import mysql.connector

def connect():
    return mysql.connector.connect(host='localhost', user='root', password='9654558088', database='banky')

def close_connection(conn):
    conn.close()