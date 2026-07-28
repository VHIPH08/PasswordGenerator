import pyperclip

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
