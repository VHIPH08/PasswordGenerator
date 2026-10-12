import string
import secrets

class PasswordGenerator:

    @staticmethod
    def generate_passwords(config: dict, alphabet: str) -> list[str]:
        active: list = []
        bool_field: list = [config["isup"], config["isdown"], config["isnumber"], config["ispunct"]]
        alpha: list = [
            string.ascii_uppercase,
            string.ascii_lowercase,
            string.digits,
            string.punctuation
        ]

        if config["banletters"]:
            banlist: list = list("&|;`()<>#%?/+@=[]{},:")

            for i in banlist:
                if i in alphabet:
                    alphabet = list(alphabet)
                    alphabet.remove(i)
                    alphabet = "".join(alphabet)

            # Фільтруємо кожен окремий набір символів (alpha[i]),
            # щоб забанені символи не потрапили і в "required" теж
            alpha = ["".join(c for c in s if c not in banlist) for s in alpha]

        if alphabet == "":
            raise ValueError("Alphabet is empty after removing banned letters!")

        for i in range(0, len(bool_field)):
            if bool_field[i]:
                if alpha[i] == "":
                    raise ValueError(
                        "One of the selected character sets became empty "
                        "after removing banned letters!"
                    )
                active.append(alpha[i])

        required: str = "".join([secrets.choice(s) for s in active])
        password: str = ""
        passwords: list[str] = []

        for i in range(0, config["howmuch"]):
            password += required

            for j in range(0, config["howlong"] - len(required)):
                password += secrets.choice(alphabet)

            password = list(password)
            secrets.SystemRandom().shuffle(password)
            password = "".join(password)

            passwords.append(password)
            password = ""

        return passwords

class Alphabet:
    @staticmethod
    def creating_alphabet(config: dict) -> str:
        bool_field: dict = {
            "isup": config["isup"],
            "isdown": config["isdown"],
            "isnumber": config["isnumber"],
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
            if bool_field[i]:
                alphabet += char_sets[j]
            j += 1

        if alphabet == "":
            raise ValueError("Alphabet is empty!")

        return alphabet