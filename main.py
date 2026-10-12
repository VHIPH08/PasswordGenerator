import sys
from generator import PasswordGenerator, Alphabet
from ui import InpOut
from validate import Validator
import crypto
from Storage import *


def main() -> None:
    password_generator = PasswordGenerator()
    console = InpOut()
    valid = Validator()
    alphabet_generator = Alphabet()

    key = console.load_key("key")

    if not key:
        key = crypto.Cipher.generate_key()
        console.save_key("key", key)

    cryptog = crypto.Cipher(key)

    # Параметри беруться з аргументів командного рядка
    config = console.get_config()

    try:
        first_valid_data = valid.validating(config)
    except ValueError as error:
        sys.exit(f"Error: {error}")
    final_valid_data = valid.validate_length_vs_requirements(first_valid_data)

    alphabet = alphabet_generator.creating_alphabet(final_valid_data)
    password = password_generator.generate_passwords(final_valid_data, alphabet)
    encrypt_password = cryptog.encrypt(password)

    if final_valid_data["save_in_copyboard"]:
        console.warning_message("Warning: Saved to copyboard will be only last password!")
    console.output(password, final_valid_data)


if __name__ == "__main__":
    main()
