import sqlite3
from sqlite3 import OperationalError

def connect():
    return sqlite3.connect('filmflix.db')

def update_films():
    try:
        conn = connect()
        cursor = conn.cursor()

        filmID = int(input("Enter the filmID to update a record: "))
        cursor.execute(f"SELECT * FROM tblFilms WHERE filmID = ?", (filmID,))
        row = cursor.fetchone()

        if row is None:
            print(f"No record with the filmID {filmID} exists")
        else:
            fieldname = input("Enter the field (yearReleased or Title or Genre): ").title()
            fieldValue = input(f"Enter the value for {fieldname}: ")

            cursor.execute(f"UPDATE tblFilms SET {fieldname} = ? WHERE filmID = ?", (fieldValue, filmID))
            conn.commit()
            print(f"{filmID} updated")
    except OperationalError as e:
        print(f"Failed because: {e}")
    except sqlite3.Error as se:
        print(f"Not working because: {se}")
    finally:
        conn.close()
        print("DB operation performed")

if __name__ == "__main__": 
    update_films()
