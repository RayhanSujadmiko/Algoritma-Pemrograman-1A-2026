jumlah_penumpang = 0
total_pendapatan = 0
jarak_terjauh = 0
total_jarak = 0

print("=== Kasir Terminal Bus Sidoarjo ===")
print("Masukkan jarak (km). Masukkan 0 untuk selesai.")

teks = input("Jarak penumpang (km): ")

# Ulangi sampai pengguna memasukkan "0"
while teks != "0":
    if not teks.isdigit():
        # Menangani huruf, input kosong, angka minus, dan desimal
        print("Input-an tidak valid, ulangi.")
    else:
        jarak = int(teks)
        jumlah_penumpang = jumlah_penumpang + 1

        # Hitung tarif berdasarkan jarak
        if jarak <= 5:
            tarif = 3000
        elif jarak <= 15:
            tarif = 3000 + 1000 * (jarak - 5)
        else:
            tarif = 13000 + 500 * (jarak - 15)

        # Diskon 50% untuk penumpang ke-5, ke-10, dst.
        if jumlah_penumpang % 5 == 0:
            tarif = tarif // 2
            print("Penumpang ke-", jumlah_penumpang, ": diskon 50% -> Rp", tarif)
        else:
            print("Penumpang ke-", jumlah_penumpang, ": Rp", tarif)

        total_pendapatan = total_pendapatan + tarif
        total_jarak = total_jarak + jarak

        if jarak > jarak_terjauh:
            jarak_terjauh = jarak

    teks = input("Jarak penumpang (km): ")

print("=== Rekap ===")
print("Jumlah penumpang :", jumlah_penumpang)
print("Total pendapatan : Rp", total_pendapatan)
if jumlah_penumpang > 0:
    print("Jarak terjauh    :", jarak_terjauh, "km")
    print("Rata-rata jarak  :", total_jarak / jumlah_penumpang, "km")
else:
    print("Jarak terjauh    : -")
    print("Rata-rata jarak  : -")