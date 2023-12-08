class RSA:
    def __init__(self, p, q, public_key):
        self.n = p * q
        self.phi = (p - 1) * (q - 1)
        self.public_key = public_key
        self.private_key = self.get_private_key()

    def get_private_key(self):
        d = pow(self.public_key, -1, self.phi)
        return d

    def enkripsi(self, plaintext):
        return pow(plaintext, self.public_key, self.n)

    def dekripsi(self, ciphertext):
        return pow(ciphertext, self.private_key, self.n)

# Example usage:
# rsa_instance = RSA(p=47, q=71, public_key=79)
# enkripsied_message = rsa_instance.enkripsi(42)  # 42 is just an example message
# dekripsied_message = rsa_instance.dekripsi(enkripsied_message)
# print("enkripsied:", enkripsied_message)
# print("dekripsied:", dekripsied_message)
