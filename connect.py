import sqlite3 as sql # import the sqlite3 module and assigned an alias

try:
    # to use the sqlite module we start by creating a variable(object) to hold the path to the folder
    with sql.connect("Filmflix/filmflix.db") as dbCon:
        #use the dbcon variable tp manipulate (sql queries) tables in the database
        dbCursor = dbCon.cursor() # use to execute sql statement
except sql.OperationalError as e: # raise sqlerror
    # handle the exception
    print(f"Connection failed: {e}")        
