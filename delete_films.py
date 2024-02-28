from connect import *

def delete_films():
    try:
           #check if the film id exists
        filmID  = int(input("Enter the filmID to delete arecord : "))
        dbCursor.execute(f"SELECT * FROM films WHERE SongID = {filmID}")
 
        row = dbCursor.fetchone()
 
        if row == None:
            print(f"SongID {filmID} does not exits")
        else:
            dbCursor.execute("DELETE FROM films WHERE SongID = ?", (filmID,))
            dbCon.commit()
            print(f"The record {filmID} deleted from the films table")
    except sql.OperationalError as e:
        print(f"Failed because: {e}")
    except sql.ProgrammingError as pe:
        print(f"Not working because: {pe}")
    finally:
       print("DB operation performed")

if __name__ == "__main__": 
    delete_films()

