from generator import PasswordGenerator, Alphabet
from ui import InpOut
from validate import Validator

if __name__ == "__main__":
    password_generator = PasswordGenerator()
    console = InpOut()
    valid = Validator()
    alphabet_generator = Alphabet()

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

    console.warning_message("Warning: Saved to copyboard will be only last password!")
    console.output(password, final_valid_data)


