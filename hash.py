class Hash:
    def __init__(self, m):
        self.m = m

    def hash_func(self, key):
        # Menghitung jumlah dari representasi ASCII setiap karakter dalam key
        print(ord(char) for char in key)
        key_sum = sum(ord(char) for char in key)
        # Menggunakan fungsi hash h(K) = K mod m
        hashed_value = key_sum % self.m
        return hashed_value