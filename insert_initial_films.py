from connect import dbCursor, dbCon
from read_films import all_films

def multiple_records():
    tblFilms = [
        ('Commando', 1985, 'Action'),
        ('Hero', 2002, 'Action'),
        ('Unfaithful', 2002, 'Romance'),
        ('Blue valentine', 2010, 'Romance drama'),
        ('Apollo 13', 1995, 'Historical Event')
    ]

    try:
        # Use the cursor to execute the SQL statement
        dbCursor.executemany("INSERT INTO tblFilms(Title, yearReleased, Genre) VALUES(?,?,?)", tblFilms)
        dbCon.commit()
        
        # Now call the all_films function from the read_films file to display updated records
        all_films()
    except Exception as e:
        print("Error:", e)

# Call the multiple_records function
if __name__ == "__main__":
    multiple_records()
