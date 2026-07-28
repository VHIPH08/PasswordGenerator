class Validator:
    @staticmethod
    def validating(vdic: dict) -> dict:
        numeric_field: dict = {"howlong": vdic["howlong"], "howmuch": vdic["howmuch"]}
        bool_field: dict = {
            "isup": vdic["isup"],
            "isdown": vdic["isdown"],
            "isnumber": vdic["isnumber"],
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
                    bool_field[i] = bool_field[i].strip().upper()
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

    @staticmethod
    def validate_length_vs_requirements(config: dict) -> dict:
        required_count :int = sum([config["isup"], config["isdown"], config["isnumber"], config["ispunct"]])
        if config["howlong"] < required_count:
            print(f"Попередження: довжина пароля збільшена з {config['howlong']} "
                  f"до {required_count}, оскільки обрано {required_count} типів символів.")
            config["howlong"] = required_count

        return config