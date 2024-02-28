from connect import *

def add_films(film_data):
    try:
        cursor = dbCon.cursor()
        cursor.execute("INSERT INTO tblFilms VALUES (NULL, ?, ?, ?, ?, ?)", film_data)
        dbCon.commit()
        print("Film added successfully.")
    except Exception as e:
        print("Error adding film:", e)
    finally:
        dbCon.close()


# Define the film data
film_data = ('The Muppets', 2022, 'PG', 116, 'Comedy')

# Call the add_film function with the film data
if __name__ == "__main__":
    add_films(film_data)
