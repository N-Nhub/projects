#le passwurd managerrrrrrrrrrrr

import json

passwurdz={}

with open("le_passwurdz.json", "r") as file:
    passwurdz = json.load(file)

def main_menu():
    main_menuz = str(input("Welcome! type the following:\n q for quit \n n for new password \n s for search passwords \n"))

main_menuz = str(input("Welcome! type the following:\n q for quit \n n for new password \n s for search passwords \n"))


if main_menuz == "q":
    quit()
if main_menuz == "n":
    newlogin=str(input("introduce para que es la contraseña\n"))
    newpasswurd=str(input("introduce la nueva contraseña\n"))
    passwurdz[newlogin] = (newpasswurd)
    with open("le_passwurdz.json", "w") as file:
        json.dump(passwurdz, file, indent=4)
    main_menu()
if main_menuz == "s":
    search=input("que contraseña quieres?\n")
    if search in passwurdz:
        print(passwurdz[search])
    else:
        print("la contraseña no existe")