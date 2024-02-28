from connect import *

def search_films_by_genre():
    try:
                #ask for the field to search by
            field = input("Search by filmID, Title, yearReleased, Genre: ")
 
            if field == "filmID":
                # search by filmID
                idInput = int(input("Enter filmID: "))
                dbCursor.execute("SELECT * FROM films WHERE filmID = ?", (idInput,))
                row = dbCursor.fetchone()
 
                if row is None:
                    # if the filmID entered is not in the table
                    print(f"No record with filmID {idInput} exists")
                else:
                    # if the filmID entered is exiata in the table
                    for all_films in row:
                        print(all_films)
 
            elif field in ["Title", "yearReleased", "Genre"]:
                # search by Title, YearReleased, Genre
                strInput= input(f"Enter the value for the field {field}: ")
                #SELECT * FROM films WHERE "Title", "yearReleased", "Genre"  LIKE "The BFG" or "2016" or "Fantasy"?
                
                dbCursor.execute(f"SELECT * FROM films WHERE {field} LIKE '%{strInput}%'")
 
                rows = dbCursor.fetchall()
                if not rows:
                    print(f"No record with field {field} matching '{strInput} ")
                else:
                    # display all matched records for the search field
                    for records in rows:
                        print(records)
 
            else: # where the search input is not  filmID, Title, yearReleased, Genre
                print(f"Search field {field} invalid !")
    except sql.OperationalError as e:
            print(f"Failed because: {e}")
    except sql.ProgrammingError as pe:
            print(f"Not working because: {pe}")
    finally:
            print("DB operation performed")    
if __name__ == "__main__":
        
    search_films_by_genre()