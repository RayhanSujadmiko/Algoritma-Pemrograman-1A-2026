# Mengecek input
def semua_angka(inputan):
    # Mengecek angka 0-9
    for huruf in inputan:
        if huruf < "0" or huruf > "9":
            return False
    return True

def input_bulat(pesan):
    # Meminta input bilangan bulat
    while True:
        inputan = input(pesan)

        if inputan == "":
            print("Input tidak boleh kosong! Coba lagi.")
        elif inputan[0] == "-":
            print("Input tidak boleh negatif! Coba lagi.")
        elif not semua_angka(inputan):
            print("Input harus berupa angka bulat! Coba lagi.")
        else:
            return int(inputan)

# Fungsi rekursif
def pelanggan(n):
    # Hari ke-1 dan ke-2 jumlahnya 1 orang
    if n == 1 or n == 2:
        return 1
    # Hari lainnya = hari kemarin + hari kemarin lusa
    return pelanggan(n - 1) + pelanggan(n - 2)

print("Jumlah Pelanggan Toko Kue Bu Lastri")

# Hari dibatasi 1 sampai 30 supaya program tidak terlalu lama
while True:
    n = input_bulat("Masukkan hari ke-N (1 - 30): ")
    if n < 1:
        print("Hari minimal 1! Coba lagi.")
    elif n > 30:
        print("Hari maksimal 30! Coba lagi.")
    else:
        break

hasil = pelanggan(n)
print("Jumlah pelanggan pada hari ke-" + str(n) + " adalah " + str(hasil) + " orang")