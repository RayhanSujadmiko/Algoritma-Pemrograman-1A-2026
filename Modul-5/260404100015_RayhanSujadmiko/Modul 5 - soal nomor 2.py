BESAR = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
KECIL = "abcdefghijklmnopqrstuvwxyz"

# Mengecek input
def semua_huruf(teks):
    # Mengecek huruf A-Z / a-z
    for karakter in teks:
        ketemu = False
        for i in range(26):
            if karakter == BESAR[i] or karakter == KECIL[i]:
                ketemu = True
        if not ketemu:
            return False
    return True

def input_kata(pesan):
    # Meminta input kata
    while True:
        kata = input(pesan)

        if kata == "":
            print("Input tidak boleh kosong! Coba lagi.")
        elif not semua_huruf(kata):
            print("Input hanya boleh huruf (tidak boleh angka/simbol/spasi)! Coba lagi.")
        else:
            return kata

# Mengubah huruf besar jadi kecil
def ubah_kecil(kata):
    hasil = ""
    for karakter in kata:
        karakter_baru = karakter
        for i in range(26):
            if karakter == BESAR[i]:
                karakter_baru = KECIL[i]
        hasil = hasil + karakter_baru
    return hasil

# Mengecek palindrom
def palindrom(kata):
    kata = ubah_kecil(kata)

    # Membalik kata
    terbalik = ""
    for huruf in kata:
        terbalik = huruf + terbalik

    # Palindrom
    if kata == terbalik:
        return True
    else:
        return False

print("Cek Palindrom")
kata = input_kata("Masukkan sebuah kata: ")

if palindrom(kata):
    print("Hasil: True")
    print("Kata '" + kata + "' adalah palindrom.")
else:
    print("Hasil: False")
    print("Kata '" + kata + "' bukan palindrom.")