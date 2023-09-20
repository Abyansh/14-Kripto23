'''
Nama : Abyan Shidqi Hidayat
NPM	 : 210014
'''


def encrypt(text, s):
    result = ""
    for char in text:
        if char.isalpha():  # Memeriksa apakah karakter adalah huruf alfabet
            is_upper = char.isupper()  # Mengecek apakah karakter adalah huruf kapital
            offset = ord('A') if is_upper else ord('a')
            result += chr(((ord(char) - offset + s) % 26) + offset)
        else:
            result += char  # Karakter non-alfabet dan spasi tidak berubah
    return result


def decrypt(text,s):
    return encrypt(text,-s)
print("Program Shift Chiper\n")
text = input("Isi teks : ")
s = int(input("Masukkan pergeseran (kunci) sebagai bilangan bulat:  "))

Enkripsi = encrypt(text,s)
print ("\nEnkripsi: " + Enkripsi)
Dekripsi = decrypt(Enkripsi,s)
print ("Dekripsi: " + Dekripsi)

