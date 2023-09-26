'''
Nama : Abyan Shidqi Hidayat
NPM	 : 210014
'''
import numpy as np

# Fungsi untuk menghasilkan matriks invers modulo 26
def mod_inverse_matrix(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))  # Hitung determinan
    det_inv = pow(det, -1, modulus)  # Hitung invers determinan modulo 26

    # Hitung matriks adjoint
    adjoint = np.array([[matrix[1][1], -matrix[0][1]],
                        [-matrix[1][0], matrix[0][0]]])

    # Hitung matriks invers modulo 26
    inverse_matrix = (det_inv * adjoint) % modulus
    return inverse_matrix

# Fungsi untuk mengenkripsi teks
def encrypt(plain_text, key_matrix):
    encrypted_text = ""
    plain_text = plain_text.upper().replace(" ", "")

    # Pastikan panjang teks adalah kelipatan 2
    if len(plain_text) % 2 != 0:
        plain_text += "X"

    # Loop melalui teks dengan jarak 2 karakter
    for i in range(0, len(plain_text), 2):
        pair = plain_text[i:i+2]
        pair_as_numbers = [ord(char) - ord('A') for char in pair]

        # Kalikan dengan matriks kunci
        result = np.dot(key_matrix, pair_as_numbers) % 26

        # Konversi hasil kembali ke karakter
        encrypted_pair = ''.join([chr(num + ord('A')) for num in result])
        encrypted_text += encrypted_pair

    return encrypted_text

# Fungsi untuk mendekripsi teks
def decrypt(encrypted_text, key_matrix):
    decrypted_text = ""

    # Inversi matriks kunci
    key_matrix_inverse = mod_inverse_matrix(key_matrix, 26)

    # Loop melalui teks dengan jarak 2 karakter
    for i in range(0, len(encrypted_text), 2):
        pair = encrypted_text[i:i+2]
        pair_as_numbers = [ord(char) - ord('A') for char in pair]

        # Kalikan dengan matriks kunci invers
        result = np.dot(key_matrix_inverse, pair_as_numbers) % 26

        # Konversi hasil kembali ke karakter
        decrypted_pair = ''.join([chr(num + ord('A')) for num in result])
        decrypted_text += decrypted_pair

    return decrypted_text

# Main program
if __name__ == "__main__":
    key_matrix = np.array([[7, 6],
                            [2, 5]])

    plain_text = input("Masukkan teks yang ingin dienkripsi: ")
    encrypted_text = encrypt(plain_text, key_matrix)
    print(f"Teks terenkripsi: {encrypted_text}")

    decrypted_text = decrypt(encrypted_text, key_matrix)
    print(f"Teks terdekripsi: {decrypted_text}")
