# Program Dekripsi Ciphertext ROT13
# Tugas Kriptografi

# Ciphertext dari soal
ciphertext = "Gur dhvpx oebja sbk whzcf bire gur ynml qbt"

# Fungsi ROT13
def rot13(teks):
    hasil = ""

    for huruf in teks:
        if 'A' <= huruf <= 'Z':   # Huruf besar
            hasil += chr((ord(huruf) - ord('A') + 13) % 26 + ord('A'))
        elif 'a' <= huruf <= 'z': # Huruf kecil
            hasil += chr((ord(huruf) - ord('a') + 13) % 26 + ord('a'))
        else:
            hasil += huruf  # Spasi / tanda baca tetap

    return hasil

# Proses dekripsi
plaintext = rot13(ciphertext)

# Output
print("Ciphertext :", ciphertext)
print("Plaintext  :", plaintext)
