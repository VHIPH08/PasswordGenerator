import string
import secrets
import time
import pyperclip

class PasswordGenerator:
    def __init__(self, level, hw_pass, choose):
        self.level = level
        self.hw_pass = hw_pass
        self.choose = choose

    def password_gen(self):
        passwords = []
        banword = ["0", "O", "o", "l", "I", "1", "5", "S", "B", "8", "Z", "2", ","]
        if self.choose == "Yes":
            hl = input("How long u wanna ur password be?")
            while not hl.isdigit():
                hl = input("Pls try a number!")
            hl = int(hl)
        else:
            hl = secrets.choice(range(4, 12))

        for n in range(0, self.hw_pass):
            password = ""
            if self.level == "easy":
                for i in range(0, hl):
                    password += secrets.choice(string.ascii_letters + string.digits)

            elif self.level == "middle":
                for i in range(0, hl):
                    password += secrets.choice(string.printable)

            elif self.level == "hard":
                for i in range(0, hl):
                    chosen_one = secrets.choice(string.ascii_letters + string.digits + string.punctuation)
                    if chosen_one not in banword:
                        password += chosen_one
                    else:
                        hl += 1
            else:
                return print("Try to input: easy, middle, hard")

            passwords.append(password)

        if self.hw_pass == 1:
            answer = input("Do u wanna copy password into ur copy buffer?")
            if answer == "Yes":
                pyperclip.copy(password)
                print("Ur password will be deleted from there in 1 minute")
                time.sleep(60)
                pyperclip.copy("")

        return passwords

    def password_saver(self, written):
        with open("file.txt", "a") as f:
             for password in written:
                f.write(password + "\n")


if __name__ == "__main__":
    Password_Generator = PasswordGenerator("hard", 1, "Yes")
    alala = Password_Generator.password_gen()
    Password_Generator.password_saver(alala)