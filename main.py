from generator import PasswordGenerator, Alphabet
from ui import InpOut
from validate import Validator
import crypto
from Storage import *

if __name__ == "__main__":
    password_generator = PasswordGenerator()
    console = InpOut()
    valid = Validator()
    alphabet_generator = Alphabet()

    key = console.load_key("key")

    if not key:
        key = crypto.Cipher.generate_key()
        console.save_key("key", key)

    cryptog = crypto.Cipher(key)

    config = {"howlong" : console.input_str("How long you wanna your password be?(Default is 12)"),
            "howmuch" : console.input_str("How many passwords you want?(Default is 1)"),
            "isup" : console.input_str("Do you want upper letters?(Y/N)"),
            "isdown" : console.input_str("Do you want lower letters?(Y/N)"),
            "isnumber" : console.input_str("Do you want numbers?(Y/N)"),
            "ispunct" : console.input_str("Do you want punctuations?(Y/N)"),
            "banletters" : console.input_str("Do you want banletters?(Y/N)"),
            "save_in_copyboard" : console.input_str("Do you want save in copyboard?(Y/N)")}


    first_valid_data = valid.validating(config)
    final_valid_data = valid.validate_length_vs_requirements(first_valid_data)

    alphabet = alphabet_generator.creating_alphabet(final_valid_data)
    password = password_generator.generate_passwords(final_valid_data, alphabet)
    encrypt_password = cryptog.encrypt(password)
    encrypt_password_string = []

    for i in range(len(encrypt_password)):
        encrypt_password_string.append(encrypt_password[i].decode("utf-8"))

    #save(encrypt_password_string)
    #decrypt_password = cryptog.decrypt(load_all())
    delete(4)
    print(len(load_all()))

    console.warning_message("Warning: Saved to copyboard will be only last password!")
    console.output(password, final_valid_data)
