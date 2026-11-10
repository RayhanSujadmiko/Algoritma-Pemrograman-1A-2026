BESAR = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
KECIL = "abcdefghijklmnopqrstuvwxyz"

# Mengecek input
def semua_angka(teks):
    # Mengecek angka 0-9
    for huruf in teks:
        if huruf < "0" or huruf > "9":
            return False
    return True

def semua_huruf(teks):
    # Mengecek huruf atau spasi
    for karakter in teks:
        ketemu = False
        for i in range(26):
            if karakter == BESAR[i] or karakter == KECIL[i] or karakter == " ":
                ketemu = True
        if not ketemu:
            return False
    return True

def input_nama(pesan):
    # Meminta nama dengan benar
    while True:
        nama = input(pesan)

        if nama == "":
            print("Nama tidak boleh kosong! Coba lagi.")
        elif not semua_huruf(nama):
            print("Nama hanya boleh huruf (tidak boleh angka/simbol)! Coba lagi.")
        else:
            return nama

def input_nilai(pesan):
    # Meminta nilai bilangan bulat 0 - 100
    while True:
        teks = input(pesan)

        if teks == "":
            print("Nilai tidak boleh kosong! Coba lagi.")
        elif teks[0] == "-":
            print("Nilai tidak boleh negatif! Coba lagi.")
        elif not semua_angka(teks):
            print("Nilai harus berupa angka bulat! Coba lagi.")
        elif int(teks) > 100:
            print("Nilai maksimal 100! Coba lagi.")
        else:
            return int(teks)

# Hitung nilai akhir
def hitung_nilai(nama, tugas, uts, uas):
    nilai_akhir = tugas * 0.3 + uts * 0.3 + uas * 0.4

    # Cek Nilai
    if nilai_akhir >= 85:
        grade = "A"
    elif nilai_akhir >= 70:
        grade = "B"
    elif nilai_akhir >= 55:
        grade = "C"
    else:
        grade = "D"

    # Cek Status
    if grade == "D":
        status = "Tidak Lulus"
    else:
        status = "Lulus"

    print()
    print("HASIL NILAI")
    print("Nama        :", nama)
    print("Nilai Tugas :", tugas)
    print("Nilai UTS   :", uts)
    print("Nilai UAS   :", uas)
    print("Nilai Akhir :", nilai_akhir)
    print("Grade       :", grade)
    print("Status      :", status)

print("=== Program Nilai Akhir Mahasiswa ===")
nama = input_nama("Masukkan nama mahasiswa: ")
tugas = input_nilai("Masukkan nilai tugas (0-100): ")
uts = input_nilai("Masukkan nilai UTS (0-100): ")
uas = input_nilai("Masukkan nilai UAS (0-100): ")

hitung_nilai(nama, tugas, uts, uas)