import string
import secrets
import pyperclip
from random import shuffle

class PasswordGenerator:

    def get_input(self) -> dict:
        howlong = input("How long you wanna your password be?(Default is 12)")
        howmuch = input("How many passwords you want?(Default is 1)")

        isup = input("Do you want upper letters?(Y/N)")
        isdown = input("Do you want lower letters?(Y/N)")
        isnum = input("Do you want numbers?(Y/N)")
        ispunct = input("Do you want punctuation?(Y/N)")
        banletters = input("Do you want to use banletter list in alphabets?(Y/N)")
        print("Warning! If you want more than 1 password, you should know that only last password will be copied into copyboard.")
        save_in_copyboard = input("Do you want to save your password in copyboard?(Y/N)")

        config = {
            "howlong": howlong,
            "howmuch": howmuch,
            "isup": isup,
            "isdown": isdown,
            "isnum": isnum,
            "ispunct": ispunct,
            "banletters": banletters,
            "save_in_copyboard": save_in_copyboard
        }

        return config

    def validating(self, vdic: dict) -> dict:
        numeric_field: dict = {"howlong": vdic["howlong"], "howmuch": vdic["howmuch"]}
        bool_field: dict = {
            "isup": vdic["isup"],
            "isdown": vdic["isdown"],
            "isnum": vdic["isnum"],
            "ispunct": vdic["ispunct"],
            "banletters": vdic["banletters"],
            "save_in_copyboard": vdic["save_in_copyboard"]
        }
        defaults: dict = {"howlong": 12, "howmuch": 1}

        for i in numeric_field.keys():
            if numeric_field[i].strip() == "":
                numeric_field[i] = defaults[i]
                continue
            else:
                while True:
                    if numeric_field[i].isdigit():
                        if int(numeric_field[i]) > 0:
                            numeric_field[i] = int(numeric_field[i])
                            break
                        else:
                            numeric_field[i] = input("Please enter a number bigger than 0!")
                    else:
                        numeric_field[i] = input("Please enter a valid number!")

        for i in bool_field:
            if bool_field[i].strip() == "":
                bool_field[i] = True
                continue
            else:
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

        config: dict = numeric_field | bool_field
        return config

    def creating_alphabet(self, config: dict) -> str:
        bool_field: dict = {
            "isup": config["isup"],
            "isdown": config["isdown"],
            "isnum": config["isnum"],
            "ispunct": config["ispunct"]
        }
        char_sets: list = [
            string.ascii_uppercase,
            string.ascii_lowercase,
            string.digits,
            string.punctuation
        ]
        alphabet: str = ""
        j: int = 0

        for i in bool_field.keys():
            if bool_field[i] == True:
                alphabet += char_sets[j]
            j += 1

        if alphabet == "":
            raise ValueError("Alphabet is empty!")

        return alphabet

    def generate_passwords(self, config: dict, alphabet: str) -> list[str]:
        active: list = []
        bool_field: list = [config["isup"], config["isdown"], config["isnum"], config["ispunct"]]
        alpha: list = [
            string.ascii_uppercase,
            string.ascii_lowercase,
            string.digits,
            string.punctuation
        ]

        if config["banletters"] == True:
            banlist: list = list("&|;`()<>#%?/+@=[]{},:")
            for i in banlist:
                if i in alphabet:
                    alphabet = list(alphabet)
                    alphabet.remove(i)
                    alphabet = "".join(alphabet)

        for i in range(0, len(bool_field)):
            if bool_field[i] == True:
                active.append(alpha[i])

        required: str = "".join([secrets.choice(s) for s in active])
        password: str = ""
        passwords: list[str] = []

        for i in range(0, config["howmuch"]):
            password += required

            for j in range(0, config["howlong"] - len(required)):
                password += secrets.choice(alphabet)

            password = list(password)
            shuffle(password)
            password = "".join(password)

            passwords.append(password)
            password = ""

        return passwords

    def output(self, passwords: list[str], config: dict) -> None:
        if config["save_in_copyboard"] == True:
            pyperclip.copy(passwords[-1])

        print(f"Your password(s): {passwords}")

    def password_saver(self, written: list[str]) -> None:
        with open("passwords.txt", "a") as f:
            for password in written:
                f.write(password + "\n")


if __name__ == "__main__":
    Password_Generator = PasswordGenerator()
    inputs = Password_Generator.get_input()
    valid = Password_Generator.validating(inputs)
    alphabets = Password_Generator.creating_alphabet(valid)
    password = Password_Generator.generate_passwords(valid, alphabets)
    output = Password_Generator.output(password, valid)
