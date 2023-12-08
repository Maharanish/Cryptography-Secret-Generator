from rsa import RSA
from caesar_cipher import CaesarCipher
from hash import Hash

# Langkah 1: Meminta pengguna memasukkan username
username = input("Masukkan username (tanpa spasi): ")

# Langkah 2: Mengubah username menjadi ASCII dan menghitung sum
username_sum = sum(ord(char) for char in username)
# Memastikan bahwa username tidak mengandung spasi
if ' ' in username:
    raise ValueError("Username tidak boleh mengandung spasi.")

# Membuat objek Hash dengan m = 100 untuk hash username_sum
hash_obj = Hash(m=100)
hashed_username_sum = hash_obj.hash_func(str(username_sum))
print(hashed_username_sum)
print()
# Memeriksa kecocokan hashed_username_sum dengan hash dari password
while True:
    input_password = input("Masukkan password: ")
    if input_password == str(hashed_username_sum):
        print("Password benar.")
        break
    else:
        print("Password salah. Silakan coba lagi.")

# Langkah 4: Meminta pengguna untuk memilih enkripsi atau dekripsi
choice = input("Pilih 'e' untuk enkripsi atau 'd' untuk dekripsi: ")

# Langkah 5: Melakukan enkripsi atau dekripsi sesuai dengan pilihan pengguna
if choice == 'e':
    # Meminta pengguna memasukkan teks yang akan dienkripsi
    plaintext = input("Masukkan teks yang akan dienkripsi: ")

    # Enkripsi dengan Caesar Cipher
    caesar_cipher = CaesarCipher(shift=3)  # Ganti shift sesuai kebutuhan
    encrypted_caesar = caesar_cipher.enkripsi(plaintext)
    #print("encrypt caesar: ", encrypted_caesar)
    # Mengubah setiap karakter pada teks hasil enkripsi dari Caesar Cipher menjadi ASCII
    ascii_values = [ord(char) for char in encrypted_caesar]

    # Enkripsi dengan RSA
    rsa = RSA(p=61, q=53, public_key=17)  # Ganti parameter sesuai kebutuhan
    encrypted_rsa = [rsa.enkripsi(value) for value in ascii_values]

    print("Hasil enkripsi: ", encrypted_rsa)
    print("Kunci publik: ", rsa.public_key)

elif choice == 'd':
    # Meminta pengguna memasukkan teks yang akan didekripsi
    ciphertext = input("Masukkan teks yang akan didekripsi: ")

    # Meminta pengguna memasukkan public key dan private key
    public_key = int(input("Masukkan public key: "))
    private_key = int(input("Masukkan private key: "))

    # Dekripsi dengan RSA
    rsa = RSA(p=61, q=53, public_key=public_key)
    rsa.private_key = private_key

    # Membuat objek CaesarCipher di sini
    caesar_cipher = CaesarCipher(shift=3)  # Ganti shift sesuai kebutuhan

    # Dekripsi RSA untuk mendapatkan list nilai ASCII
    decrypted_rsa = [rsa.dekripsi(value) for value in eval(ciphertext)]
    #print("Decrypted RSA:", decrypted_rsa)

    # Mengubah nilai ASCII ke teks dengan Caesar Cipher
    caesar_text = "".join(chr(value) for value in decrypted_rsa)
    #print("Caesar text: ", caesar_text)

    # Dekripsi dengan Caesar Cipher
    decrypted_caesar = caesar_cipher.dekripsi(caesar_text)

    print("Hasil dekripsi:", decrypted_caesar)


else:
    print("Pilihan tidak valid.")
