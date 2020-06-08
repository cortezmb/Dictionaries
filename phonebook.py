#You will write a command line program to manage a phone book. 
# When you start the phonebook.py program, it will print out a menu and ask the user to enter a choice.

# phonebook_dict = {'Alice': '(703) 493-1834','Bob': '(857) 384-1234','Elizabeth': '(484) 584-2923'}
 
# Load the data 
import pickle
with open('phonebook.pickle', 'rb') as fh:
    #creating a new variable in the file
    phonebook_dict = pickle.load(fh)
    #you can access keys and values in the this dictionary
    # print(data)




while True:
    # Print out menu and ask for an input 1-5
    menu = int(input("\nElectronic Phone Book \n********************** \n\n 1. Look up an entry \n 2. Set an entry \n 3. Delete an entry \n 4. List all entries \n 5. Quit \n\n What do you want to do (1-5?) "))
# Menu Option #1: If they choose to look up an entry, you will ask them for the person's name, and then look up the person's phone number by the given name and print it to the screen.    
    if menu == int("1"):
        # Need to make it so the name will have a first letter capital by using .capitalize
        name = input("\n What is the person's name? ").capitalize()
        if name in phonebook_dict:
            print(f"\n {name}'s phone number is {phonebook_dict[name]}\n")
        pass 
# Menu Option #2: If they choose to set an entry, you will prompt them for the person's name and the person's phone number

    if menu == int("2"):
        name = input("\n In order to set an entry, I need few pieces of information.\n\n What is the person's name? ").capitalize()
        phone = input("\n What is the person's number? ")
        # This will add the input name and number to the phone book.
        phonebook_dict[name] = phone
        print(f"\n {name}'s phone number of {phonebook_dict[name]} has been added to the phone book.\n")
    break    
        # This is a check to confirm the name and number were added to dictionary
        # print(phonebook_dict)

# Menu Option #3: If they choose to delete an entry, you will prompt them for the person's name and delete the given person's entry.
    if menu == int("3"):
        # Need to make it so the name will have a first letter capital by using .capitalize
        name = input("\n What is the person's name? ").capitalize()
        print(f"\n You have deleted {name} from the phone book.\n")
        del phonebook_dict[name]
        import pickle
    break
 # This is a check to confirm the name and number were deleted from dictionary
    # print(phonebook_dict)

# Menu Option #4: If they choose to list all entries, you will go through all entries in the dictionary and print each out to the terminal.
    if menu == int("4"):
        print("\n You have chosen to see a list of all the contacts. Here you go....\n")
        for key, value in phonebook_dict.items():
            print(f" {key}........{value}")
    break      
# Menu Option #5: If they choose to quit, end the program.
    if menu == int("5"):
        print("\n You have chosen to quit. Have an awesome day!\n\n")
    break
with open('phonebook.pickle', 'wb') as fh:
    # This will dump data in binary from data file
    pickle.dump(phonebook_dict, fh)


