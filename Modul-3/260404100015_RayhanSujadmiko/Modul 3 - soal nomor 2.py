teks = input("Masukkan tinggi setengah menara (2-15): ")

# Ulangi selama bukan angka, atau angkanya di luar rentang 2-15
while not teks.isdigit() or int(teks) < 2 or int(teks) > 15:
    print("Input-an tidak valid, ulangi.")
    teks = input("Masukkan tinggi setengah menara (2-15): ")

n = int(teks)

baris = 1
while baris <= 2 * n - 1:

    # Nomor baris efektif: membesar sampai n, lalu mengecil
    if baris <= n:
        r = baris
    else:
        r = 2 * n - baris

    # Spasi di kiri supaya rata tengah
    spasi = 0
    while spasi < n - r:
        print(" ", end="")
        spasi = spasi + 1

    # Angka naik dari 1 sampai r (hanya digit terakhir)
    angka = 1
    while angka <= r:
        print(angka % 10, end="")
        angka = angka + 1

    # Angka turun dari r-1 kembali ke 1
    angka = r - 1
    while angka >= 1:
        print(angka % 10, end="")
        angka = angka - 1

    print()
    baris = baris + 1