class CaesarCipher():
    def __init__(self, text):
        self.text = text
        self.shift = 3

    def encrypt(self):
        result = ""
        for char in self.text:
            if char.isupper():
                result += chr((ord(char) + self.shift - 65) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) + self.shift - 97) % 26 + 97)
            else:
                result += char
        return result

    def decrypt(self):
        result = ""
        for char in self.text:
            if char.isupper():
                result += chr((ord(char) - self.shift - 65) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) - self.shift - 97) % 26 + 97)
            else:
                result += char
        return result
