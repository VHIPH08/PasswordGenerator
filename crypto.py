from cryptography.fernet import Fernet

class Cipher:
    def __init__(self, key:bytes) -> None:
        self.key = key
        self.fernet = Fernet(key)

    @staticmethod
    def generate_key():
        return Fernet.generate_key()

    def check_or_create_key(self) -> None:
        if not self.key:
            self.key = Fernet.generate_key()
            self.fernet = Fernet(self.key)

    def encrypt(self, password:list[str]) -> list[bytes]:
        self.check_or_create_key()
        encrypted_password = []
        for i in range(len(password)):
            encrypted_password.append(self.fernet.encrypt(password[i].encode()))

        return encrypted_password

    def decrypt(self, encrypted_password:list[bytes]) -> list[bytes]:
        decrypted_password = []

        for i in range(len(encrypted_password)):
            decrypted_password.append(self.fernet.decrypt(encrypted_password[i]).decode("utf-8"))

        return decrypted_password

