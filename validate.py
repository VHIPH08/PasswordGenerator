import sys


class Validator:
    @staticmethod
    def validating(config: dict) -> dict:
        """Перевіряє config, отриманий з CLI. Типи вже перевірив argparse,
        тут лише логічні перевірки. При помилці кидає ValueError."""
        if config["howlong"] <= 0:
            raise ValueError("Password length must be bigger than 0")
        if config["howmuch"] <= 0:
            raise ValueError("Number of passwords must be bigger than 0")
        if not any([config["isup"], config["isdown"], config["isnumber"], config["ispunct"]]):
            raise ValueError("Choose at least one character type")
        return config

    @staticmethod
    def validate_length_vs_requirements(config: dict) -> dict:
        required_count: int = sum([config["isup"], config["isdown"], config["isnumber"], config["ispunct"]])
        if config["howlong"] < required_count:
            print(f"Попередження: довжина пароля збільшена з {config['howlong']} "
                  f"до {required_count}, оскільки обрано {required_count} типів символів.",
                  file=sys.stderr)
            config["howlong"] = required_count

        return config
