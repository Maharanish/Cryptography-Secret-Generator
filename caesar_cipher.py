class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift

    def enkripsi(self, plaintext):
        result = ""
        for char in plaintext:
            if char.isalpha():
                ascii_offset = ord('a') if char.islower() else ord('A')
                result += chr((ord(char) - ascii_offset + self.shift) % 26 + ascii_offset)
            else:
                result += char
        return result

    def dekripsi(self, ciphertext):
        result = ""
        for char in ciphertext:
            if char.isalpha():
                ascii_offset = ord('a') if char.islower() else ord('A')
                result += chr((ord(char) - ascii_offset + 26 + self.shift) % 26 + ascii_offset)
            else:
                result += char
        return result