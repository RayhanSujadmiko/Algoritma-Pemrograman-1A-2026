print("Masukan kode Digit 3 angka : ")
kode = int(input())
digit1 = int(float(kode) / 100)
digit2 = int(float(kode) / 10) % 10
digit3 = kode % 10
print("Digit pertama = " + str(digit1))
print("Digit kedua = " + str(digit2))
print("Digit ketiga = " + str(digit3))
pelacakAwal = digit1 * digit3
print("Nilai pelacak awal = " + str(pelacakAwal))
if digit2 % 2 == 1:
    pelacak1 = pelacakAwal + 25
else:
    pelacak1 = pelacakAwal - digit2
print("Pelacak setelah perubahan tahap 1 = " + str(pelacak1))
if pelacak1 % 3 == 0:
    pelacak2 = int(float(pelacak1) / 3)
else:
    pelacak2 = pelacak1 * 2
print("Pelacak setelah perubahan tahap 2 (nilai akhir) = " + str(pelacak2))
if pelacak2 > 50:
    print("sKrasny terdeteksi sebagai Kategori A")
else:
    if pelacak2 > 20:
        print("sKrasny terdeteksi sebagai Kategori B")
    else:
        print("sKrasny Ditolak")
if pelacak2 % 2 == 0:
    print("Siklus Genap")
else:
    print("Siklus Ganjil")
