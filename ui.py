import pyperclip
import pathlib

class InpOut:
    @staticmethod
    def input_str(text:str) -> str:
        text_input = input(text)
        return text_input

    @staticmethod
    def output(passwords: list[str], config: dict) -> None:
        if config["save_in_copyboard"]:
            pyperclip.copy(passwords[-1])

        print(f"Your password(s): {passwords}")

    @staticmethod
    def warning_message(string: str) -> None:
        print(string)

    @staticmethod
    def load_key(name_of_file: str) -> bytes:
        try:
            path_to_file = pathlib.Path(name_of_file)
            return path_to_file.read_bytes()
        except FileNotFoundError:
            print(f"File not found: {name_of_file}")

    @staticmethod
    def save_key(name_of_file:str, key:bytes) -> None:
        path_to_file = pathlib.Path(name_of_file)
        path_to_file.write_bytes(key)
