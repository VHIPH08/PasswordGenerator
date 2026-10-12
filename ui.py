import argparse
import pathlib
import sys

import pyperclip


def _positive_int(value: str) -> int:
    try:
        number = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"'{value}' is not a valid number")
    if number <= 0:
        raise argparse.ArgumentTypeError("value must be bigger than 0")
    return number


class InpOut:
    @staticmethod
    def build_parser() -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser(
            prog="passgen",
            description="Password generator",
        )
        parser.add_argument("-l", "--length", type=_positive_int, default=12,
                            help="password length (default: 12)")
        parser.add_argument("-n", "--count", type=_positive_int, default=1,
                            help="how many passwords to generate (default: 1)")
        parser.add_argument("-u", "--upper", action="store_true",
                            help="use upper-case letters")
        parser.add_argument("-d", "--lower", action="store_true",
                            help="use lower-case letters")
        parser.add_argument("-N", "--numbers", action="store_true",
                            help="use digits")
        parser.add_argument("-p", "--punct", action="store_true",
                            help="use punctuation")
        parser.add_argument("-b", "--banletters", action="store_true",
                            help="exclude ambiguous letters (ban letters)")
        parser.add_argument("-c", "--clipboard", action="store_true",
                            help="copy the last password to the clipboard")
        return parser

    @staticmethod
    def get_config(argv: list[str] | None = None) -> dict:
        """Читає аргументи командного рядка й повертає готовий config
        (числа як int, прапорці як bool)."""
        args = InpOut.build_parser().parse_args(argv)

        # Якщо жоден набір символів не обрано — беремо розумний дефолт.
        if not (args.upper or args.lower or args.numbers or args.punct):
            args.upper = args.lower = args.numbers = True

        return {
            "howlong": args.length,
            "howmuch": args.count,
            "isup": args.upper,
            "isdown": args.lower,
            "isnumber": args.numbers,
            "ispunct": args.punct,
            "banletters": args.banletters,
            "save_in_copyboard": args.clipboard,
        }

    @staticmethod
    def output(passwords: list[str], config: dict) -> None:
        if config["save_in_copyboard"]:
            pyperclip.copy(passwords[-1])

        # По одному паролю на рядок — зручно для pipe (| grep, > file)
        for password in passwords:
            print(password)

    @staticmethod
    def warning_message(string: str) -> None:
        # Попередження йдуть у stderr, щоб не засмічувати stdout з паролями
        print(string, file=sys.stderr)

    @staticmethod
    def load_key(name_of_file: str) -> bytes | None:
        try:
            return pathlib.Path(name_of_file).read_bytes()
        except FileNotFoundError:
            return None

    @staticmethod
    def save_key(name_of_file: str, key: bytes) -> None:
        pathlib.Path(name_of_file).write_bytes(key)
