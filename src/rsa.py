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
