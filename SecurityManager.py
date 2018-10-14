from Crypto import Random
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
import secrets
import string


class SecurityManager:
    defaultLength = 16

    def __init__(self, master_pass):
        password = master_pass.encode('utf-8')
        self.__shaKey = SHA256.new(password)

    def decipher_field(self, encoded_field):
        iv = encoded_field[:AES.block_size]
        key = self.__shaKey.hexdigest()[:int(len(self.__shaKey.hexdigest())/2)]
        cipher = AES.new(key, AES.MODE_CFB, iv)
        field = cipher.decrypt(encoded_field[AES.block_size:])
        return field

    def cipher_field(self, field):
        iv = Random.new().read(AES.block_size)
        key = self.__shaKey.hexdigest()[:int(len(self.__shaKey.hexdigest())/2)]
        cipher = AES.new(key, AES.MODE_CFB, iv)
        encoded_field = iv + cipher.encrypt(field.encode('utf-8'))
        return encoded_field

    def generate_password(self, length=defaultLength):
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        return self.cipher_field(password)
