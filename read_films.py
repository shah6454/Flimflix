import connect 
import sqlite3

def all_films():
    try:
        # Execute the SQL statement to select all films
        connect.dbCursor.execute("SELECT * FROM tblFilms")
 
        # Fetch all selected data (rows)
        all_films = connect.dbCursor.fetchall()
 
        if all_films:
            # Format output
            print("filmID | Title | yearReleased | Genre")
            print("-" * 50)
 
            for film in all_films:  # Iterate over each fetched film
                print(f"{film[0]:<7} | {film[1]:<10} | {film[2]:<7} | {film[3]:<5}")
        else:
            print("No films found in the tblFilms table")
    except sqlite3.OperationalError as e:
        print(f"Failed because: {e}")
    except sqlite3.ProgrammingError as pe:
        print(f"Not working because: {pe}")
    finally:
        print("DB operation performed")

if __name__ == "__main__":
    all_films()
