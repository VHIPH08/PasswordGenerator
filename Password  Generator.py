import string
import secrets
import time
import pyperclip


class PasswordGenerator:
    def get_input(self):
        # inputing a data
        howlong = input("How long u wanna ur password be?(Default is 12)")
        howmuch = input("How many passwords u want?(Default is 1)")

        isup = input("Do you want upper letters?(Y/N)")
        isdown = input("Do you want lower letters?(Y/N)")
        isnum = input("Do you want numbers?(Y/N)")
        ispunct = input("Do you want punctuation?(Y/N)")
        banletters = input("Do you want to use banletter list in alphabets?(Y/N)")
        # keywords = input("Do you want any keywords?(Y/N)")

        config = {"howlong": howlong, "howmuch": howmuch, "isup": isup, "isdown": isdown, "isnum": isnum,
                  "ispunct": ispunct, "banletters": banletters}


        return config

    # validating the data
    def validating(self, vdic):
        numeric_field = {"howlong": vdic["howlong"], "howmuch": vdic["howmuch"]}
        bool_field = {"isup": vdic["isup"], "isdown": vdic["isdown"], "isnum": vdic["isnum"], "ispunct": vdic["ispunct"], "banletters": vdic["banletters"]}
        defaults = {"howlong": 12, "howmuch": 1}

        #checking for defaults
        for i in numeric_field.keys():
            if numeric_field[i].strip() == "":
                numeric_field[i] = defaults[i]
                continue

        #validating long and much
            while True:
                if numeric_field[i].isdigit():
                    if int(numeric_field[i]) > 0:
                        numeric_field[i] = int(numeric_field[i])
                        break
                    else:
                        numeric_field[i] = input("Please enter a number bigger than 0!")
                else:
                    numeric_field[i] = input("Please enter a valid number!")

        # checking for defaults in bools
        for i in bool_field:
            if bool_field[i].strip() == "":
                bool_field[i] = True
                continue

        #validating bools
            while True:
                if bool_field[i].isalpha():
                    bool_field[i] = bool_field[i].upper()
                    if bool_field[i] == "Y":
                        bool_field[i] = True
                        break
                    elif bool_field[i] == "N":
                        bool_field[i] = False
                        break
                    else:
                        bool_field[i] = input("Please enter a Y or N!")

        config = numeric_field | bool_field
        return config

    #creating alphabet
    def creating_alphabet(self, config):
        bool_field = {"isup": config["isup"], "isdown": config["isdown"], "isnum": config["isnum"], "ispunct": config["ispunct"]}
        dic3 = [string.ascii_uppercase, string.ascii_lowercase, string.digits, string.punctuation]
        alphabet = ""
        j = 0
        for i in bool_field.keys():
            if bool_field[i] == True:
                alphabet += dic3[j]
            j += 1

        if alphabet == "":
            raise ValueError("Alphabet is empty!")

        return alphabet

#creating a password
    def generate_passwords(self, config, alphabet):
        passwords = []
        password = ""
        numeric_field = {"howlong": config["howlong"], "howmuch": config["howmuch"]}
        banword = ["0", "O", "o", "l", "I", "1", "5", "S", "B", "8", "Z", "2", ","]
        #if banlist in use
        if config["banletters"] == True:
            for i in range(0, int(numeric_field["howmuch"])):
                for j in range(0, int(numeric_field["howlong"])):
                    letter = secrets.choice(alphabet)
                    if letter in banword:
                        continue
                    password += letter
                passwords.append(password)
                password = ""
        #not in use
        else:
            for i in range(0, int(numeric_field["howmuch"])):
                passwords.append("".join(secrets.choice(alphabet) for i in range(0, numeric_field["howlong"])))

        return passwords

    def output(self, passwords):
    #Coping a password into a copyboard
        if len(passwords) == 1:
            print("Your password was copied into your clipboard!")
            pyperclip.copy(passwords[0])
            print("It will be deleted from your clipboard in 60 seconds. Hurry up!")
            time.sleep(60)
            pyperclip.copy("")
        else:
            print("Your passwords:", passwords)

    #Saving into a file
    def password_saver(self, written):
        with open("file.txt", "a") as f:
            for password in written:
                f.write(password + "\n")


if __name__ == "__main__":
    Password_Generator = PasswordGenerator()
    inputs = Password_Generator.get_input()
    valid = Password_Generator.validating(inputs)
    alphabets = Password_Generator.creating_alphabet(valid)
    password = Password_Generator.generate_passwords(valid, alphabets)
    output = Password_Generator.output(password)
