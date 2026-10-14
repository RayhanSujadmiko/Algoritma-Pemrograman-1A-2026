# Seleksi awal penerima beasiswa untuk 10 mahasiswa
# - IPK < 3.00                  -> tidak memenuhi syarat (continue)
# - Penghasilan <= 3.000.000    -> beasiswa penuh
# - 3.000.000 < Penghasilan <= 5.000.000 -> beasiswa sebagian
# - Penghasilan > 5.000.000     -> tidak mendapat beasiswa
# - Kuota beasiswa penuh 3 mahasiswa -> proses dihentikan (break)

jumlah_mahasiswa = 10
kuota_penuh = 3

penuh = 0
sebagian = 0
tidak_lolos_ipk = 0
tidak_dapat = 0

print("=== Seleksi Awal Beasiswa ===")

i = 0
while i < jumlah_mahasiswa:
    i = i + 1
    print("\nMahasiswa ke-", i, sep="")

    # Nama
    nama = input("Nama                    : ")
    salah = True
    while salah:
        salah = False
        if len(nama) == 0:
            salah = True
        j = 0
        while j < len(nama):
            if nama[j] >= "0" and nama[j] <= "9":
                salah = True
            j = j + 1
        if salah:
            print("Nama tidak valid (tidak boleh kosong/mengandung angka), ulangi.")
            nama = input("Nama                    : ")

    # IPK
    teks_ipk = input("IPK                     : ")
    salah = True
    while salah:
        salah = False
        bulat = 0
        pecahan = 0
        jml_pecahan = 0
        ada_pemisah = False
        ada_angka = False

        j = 0
        while j < len(teks_ipk):
            c = teks_ipk[j]
            if c >= "0" and c <= "9":
                ada_angka = True
                if ada_pemisah:
                    jml_pecahan = jml_pecahan + 1
                    if jml_pecahan <= 2:
                        pecahan = pecahan * 10 + int(c)
                    else:
                        salah = True
                else:
                    bulat = bulat * 10 + int(c)
            elif c == "," or c == ".":
                if ada_pemisah:
                    salah = True   # pemisah lebih dari satu
                ada_pemisah = True
            else:
                salah = True       # huruf / simbol lain
            j = j + 1

        if not ada_angka:
            salah = True
        if jml_pecahan == 1:
            pecahan = pecahan * 10   # 3,5 -> 50 per seratus

        ipk = bulat * 100 + pecahan   # satuan 1/100
        if ipk > 400:
            salah = True

        if salah:
            print("IPK tidak valid (angka 0-4, boleh desimal , atau .), ulangi.")
            teks_ipk = input("IPK                     : ")

    # Tidak memenuhi syarat IPK -> lewati mahasiswa ini
    if ipk < 300:
        print("Hasil:", nama, "- tidak memenuhi syarat (IPK < 3,00)")
        tidak_lolos_ipk = tidak_lolos_ipk + 1
        continue

    # Penghasilan orang tua
    teks_hasil = input("Penghasilan orang tua   : Rp")
    salah = True
    while salah:
        salah = False
        penghasilan = 0
        ada_angka = False
        j = 0
        while j < len(teks_hasil):
            c = teks_hasil[j]
            if c >= "0" and c <= "9":
                ada_angka = True
                penghasilan = penghasilan * 10 + int(c)
            elif c == "." or c == ",":
                pass   # titik/koma dianggap pemisah ribuan, diabaikan
            else:
                salah = True
            j = j + 1
        if not ada_angka:
            salah = True
        if salah:
            print("Penghasilan tidak valid (hanya angka; titik/koma boleh sebagai pemisah ribuan), ulangi.")
            teks_hasil = input("Penghasilan orang tua   : Rp")

    if penghasilan <= 3000000:
        print("Hasil:", nama, "- BEASISWA PENUH")
        penuh = penuh + 1
    elif penghasilan <= 5000000:
        print("Hasil:", nama, "- BEASISWA SEBAGIAN")
        sebagian = sebagian + 1
    else:
        print("Hasil:", nama, "- tidak mendapat beasiswa (penghasilan > Rp5.000.000)")
        tidak_dapat = tidak_dapat + 1

    # Kuota beasiswa penuh terpenuhi -> hentikan seleksi
    if penuh == kuota_penuh:
        print("\nKuota beasiswa penuh (", kuota_penuh, ") sudah terpenuhi. Seleksi dihentikan.", sep="")
        break

print("\n=== Rekap Seleksi ===")
print("Mahasiswa diproses          :", i)
print("Mahasiswa belum diproses    :", jumlah_mahasiswa - i)
print("Beasiswa penuh              :", penuh)
print("Beasiswa sebagian           :", sebagian)
print("Tidak memenuhi syarat IPK   :", tidak_lolos_ipk)
print("Tidak mendapat beasiswa     :", tidak_dapat)