"""
Nicholas Lovera
Cybersecurity Lab 1
05/24/2024
"""
import csv



# First we set a constant dictonary for each option of pages


DATABASE = {"1": "Admin Controls", "2": "Finances", "3": "Scheduling", "4": "Time Cards"}


# This is our function for the user interface, such as signing in and getting to each page, Java OOP had an effect on me


def user_interface():
    # User data is an empty dictionary right now, we will input the data we get from the CSV file in the next lines 
    user_data = {}
    ''' Open the CSV file and read from it'''
    with open("userpass.csv", newline = '') as csvfile:
        # Using DictReader function to save username and password combos, learned from https://www.geeksforgeeks.org/working-csv-files-python/?ref=lbp
        reader = csv.DictReader(csvfile)
        for row in reader:
            username = row['username']
            password = row['password']
            # Update OUR user database with the data from the CSV file, good for if the CSV file is updated later on
            user_data[username] = password
    # Boolean used to ensure the program is used right
    validation = True
    while validation:
        username = input("Enter your username: ")
        # Check if username provided is valid, if so move onto password and set validation to false
        if username in user_data:
            validation = False
            # Another validation check for password
            validation2 = True
            while validation2:
                password = input("Enter your password: ")
                # If validation is correct, load into the webpage with the following page options, set validation2 to false
                if user_data[username] == password:
                    validation2 = False
                    # Final validation check to ensure the user does not break the server
                    validation3 = True
                    while validation3:
                        # Webpage
                        print("---------------------------")
                        print("1.      Admin Controls     ")
                        print("2.        Finances         ")
                        print("3.       Scheduling        ")
                        print("4.       Time Cards        ")
                        print("---------------------------")
                        selection = input("Please selection an access level: ")
                        # First case is checking that the input is even valid, aka in our DATABASE dictionary
                        if selection not in DATABASE.keys():
                            print("Not a valid option")
                        # Second case is checking if the user is UserA, if so
                        # there is no need to check what they selected since
                        # they have access to every page
                        elif username == "UserA":
                            print(f"Welcome to the {DATABASE[selection]} Page")
                            validation3 = False
                        # Third case to check if it is UserB, since UserB should only have
                        # access to some of the pages unlike UserA, we also check if they have
                        # access to their selection using a dictionary so that it cannot be changed
                        elif username == "UserB" and selection in {"2", "3", "4"}:
                            print(f"Welcome to the {DATABASE[selection]} Page")
                            validation3 = False
                        # Same thing as before but for UserC
                        elif username == "UserC" and selection in {"3", "4"}:
                            print(f"Welcome to the {DATABASE[selection]} Page")
                            validation3 = False
                        # else case would be the user does not have access to the page
                        # because of their access level
                        else:
                            print("You do not have access to this page")

                # else condition saying the password was wrong
                else:
                    print("Wrong Password")
        # else conditon saying the username was wrong
        else:
            print("Wrong Username")


# main
if __name__ == '__main__':
    user_interface()

    # As we add more functionality to this, we can create more functions that
    # place like building blocks into user_interface(), so I imagine
                            
    
        
            
        

