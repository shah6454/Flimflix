import read_films, add_films, update_films, delete_films, search_films

def read_file(file_path):
    try:
        with open(file_path) as readfile:
            rf= readfile.read()
        return rf
    
    except FileNotFoundError as nf:
        print(f"file not found: {nf}")
# Testing file path    
# print(read_file("Filmflix"))

def films_menu():
    option = 0
    optionslist = ["1","2","3","4","5","6"]
    
    menu_choices = read_file("Filmflix/menuOptions.txt")
    
    # repeat the menu options until user select the to quit
    while option not in optionslist:
        print(menu_choices)
        # re-assign the option variable a string value 
        option = input("Enter an option from the menu choice above")
        # check if the input provided in options variable is not outside of 1,2,3,4,5,6
        if option not in optionslist:
            print(f"{option} is not a valid choice! ")
    return option

#testing
# print(filmgs_menu())
# create and use a bollean flag variable
mainprogram = True # toggle to flase to exit out of the while loop

while mainprogram: # while True
    # call the films_menu function and assign to a variable(main_menu)
    main_menu = films_menu()
    
    # use match case # same as swith in javascript
    match main_menu:
        case "1": # call the readsongs file and the function display all songs
            read_films.all_songs()
        case "2":
            add_films.insert_songs()
        case "3":
            update_films.update_songs()
        case "4":
            delete_films.delete_asong()
        case "5":
            search_films.search_song()
        case _:
            mainProgram = False # set mainProgram = False to exit the menu
input("Press enter to exit......")
       
    