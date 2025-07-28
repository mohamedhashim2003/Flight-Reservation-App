import sqlite3
import os

class Database:
    def __init__(self):
        self.db_name = 'flights.db'
        self.init_database()
    
    def init_database(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS reservations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                flight_number TEXT NOT NULL,
                departure TEXT NOT NULL,
                destination TEXT NOT NULL,
                date TEXT NOT NULL,
                seat_number TEXT NOT NULL
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def create_reservation(self, name, flight_number, departure,destination, date, seat_number):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO reservations 
            (name, flight_number, departure, destination, date, seat_number)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (name, flight_number, departure, destination, date, seat_number))
        
        conn.commit()
        conn.close()
    
    def get_all_reservations(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM reservations')
        reservations = cursor.fetchall()
        
        conn.close()
        return reservations
    
    def update_reservation(self, reservation_id, name, flight_number, departure, destination, date, seat_number):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE reservations 
            SET name=?, flight_number=?, departure=?, 
                destination=?, date=?, seat_number=?
            WHERE id=?
        ''', (name, flight_number, departure, destination, 
              date, seat_number, reservation_id))
        
        conn.commit()
        conn.close()
    
    def delete_reservation(self, reservation_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('DELETE FROM reservations WHERE id=?', (reservation_id,))
        
        conn.commit()
        conn.close()