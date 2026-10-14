# Pengelolaan nilai 10 mahasiswa
# Bobot: tugas 30%, UTS 30%, UAS 40%

jumlah_mahasiswa = 10

jml_a = 0
jml_b = 0
jml_c = 0
jml_d = 0
jml_e = 0

total_s = 0
tertinggi = -1
terendah = 100001
nama_tertinggi = ""
nama_terendah = ""

print("=== Pengelolaan Nilai Mahasiswa ===")

i = 1
while i <= jumlah_mahasiswa:
    print("\nMahasiswa ke-", i, sep="")
    nama = input("Nama        : ")
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
            nama = input("Nama        : ")

    # Nilai tugas (k=0), UTS (k=1), UAS (k=2)
    k = 0
    while k < 3:
        if k == 0:
            label = "Nilai tugas : "
        elif k == 1:
            label = "Nilai UTS   : "
        else:
            label = "Nilai UAS   : "

        teks = input(label)
        salah = True
        while salah:
            salah = False
            bulat = 0          # bagian sebelum pemisah
            pecahan = 0        # bagian sesudah pemisah
            jml_pecahan = 0    # banyak angka sesudah pemisah
            ada_pemisah = False
            ada_angka = False

            j = 0
            while j < len(teks):
                c = teks[j]
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
                pecahan = pecahan * 10   # 97,3 -> 30 per seratus

            nilai = bulat * 100 + pecahan   # satuan 1/100
            if nilai > 10000:
                salah = True

            if salah:
                print("Nilai tidak valid (angka 0-100, boleh desimal , atau .), ulangi.")
                teks = input(label)

        if k == 0:
            tugas = nilai
            teks_tugas = teks
        elif k == 1:
            uts = nilai
            teks_uts = teks
        else:
            uas = nilai
            teks_uas = teks
        k = k + 1

    # Nilai akhir dalam satuan 1/1000
    s = 3 * tugas + 3 * uts + 4 * uas

    # Kategori (batas 85, 75, 65, 50 -> dikali 1000)
    if s >= 85000:
        kategori = "A"
        jml_a = jml_a + 1
    elif s >= 75000:
        kategori = "B"
        jml_b = jml_b + 1
    elif s >= 65000:
        kategori = "C"
        jml_c = jml_c + 1
    elif s >= 50000:
        kategori = "D"
        jml_d = jml_d + 1
    else:
        kategori = "E"
        jml_e = jml_e + 1

    # Hasil per mahasiswa (nilai akhir 2 desimal, dipotong tanpa pembulatan)
    desimal = (s % 1000) // 10
    print("--- Hasil ---")
    print("Nama        :", nama)
    print("Nilai tugas :", teks_tugas)
    print("Nilai UTS   :", teks_uts)
    print("Nilai UAS   :", teks_uas)
    if desimal < 10:
        print("Nilai akhir : ", s // 1000, ".0", desimal, sep="")
    else:
        print("Nilai akhir : ", s // 1000, ".", desimal, sep="")
    print("Kategori    :", kategori)

    total_s = total_s + s

    if s > tertinggi:
        tertinggi = s
        nama_tertinggi = nama
    if s < terendah:
        terendah = s
        nama_terendah = nama

    i = i + 1

print("\n=== Rekap Kelas ===")
print("Jumlah nilai A :", jml_a)
print("Jumlah nilai B :", jml_b)
print("Jumlah nilai C :", jml_c)
print("Jumlah nilai D :", jml_d)
print("Jumlah nilai E :", jml_e)

d_tinggi = (tertinggi % 1000) // 10
if d_tinggi < 10:
    print("Nilai akhir tertinggi : ", tertinggi // 1000, ".0", d_tinggi,
          " (", nama_tertinggi, ")", sep="")
else:
    print("Nilai akhir tertinggi : ", tertinggi // 1000, ".", d_tinggi,
          " (", nama_tertinggi, ")", sep="")

d_rendah = (terendah % 1000) // 10
if d_rendah < 10:
    print("Nilai akhir terendah  : ", terendah // 1000, ".0", d_rendah,
          " (", nama_terendah, ")", sep="")
else:
    print("Nilai akhir terendah  : ", terendah // 1000, ".", d_rendah,
          " (", nama_terendah, ")", sep="")

# Rata-rata = total_s / 1000 / jumlah_mahasiswa = total_s / 10000
rata_bulat = total_s // 10000
rata_desimal = (total_s % 10000) // 100
if rata_desimal < 10:
    print("Rata-rata nilai akhir : ", rata_bulat, ".0", rata_desimal, sep="")
else:
    print("Rata-rata nilai akhir : ", rata_bulat, ".", rata_desimal, sep="")