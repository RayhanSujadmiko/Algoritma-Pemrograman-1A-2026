# Memeriksa Inputan
def input_string(pesan):
    while True:
        try:
            nilai = input(pesan).strip()
            if nilai == "":
                raise ValueError("Input tidak boleh kosong!")
            for karakter in nilai.lower():
                if "0" <= karakter <= "9":
                    raise ValueError("Input tidak sesuai! Harus berupa teks (string), bukan angka.")
                elif not (("a" <= karakter <= "z") or karakter == " "):
                    raise ValueError("Input tidak sesuai! Hanya huruf yang diperbolehkan (tanpa simbol).")
            return nilai
        except ValueError as pesan_error:
            print(f"[Peringatan] {pesan_error} Silakan isi kembali.\n")


# Memeriksa Inputan Angka
def input_integer(pesan, minimum=1):
    while True:
        try:
            teks = input(pesan).strip()
            if teks == "":
                raise ValueError("Input tidak boleh kosong!")
            try:
                nilai = int(teks)
            except ValueError:
                raise ValueError("Input tidak sesuai! Harus berupa bilangan bulat (integer).")
            if nilai < 0:
                raise ValueError("Input tidak sesuai! Tidak boleh bernilai negatif.")
            if nilai < minimum:
                raise ValueError(f"Input tidak sesuai! Minimal harus {minimum}.")
            return nilai
        except ValueError as pesan_error:
            print(f"[Peringatan] {pesan_error} Silakan isi kembali.\n")

def program_utama():
    # Menginput nama asisten awal lalu dikunci (tuple)
    print("=== INPUT ASISTEN AWAL ===")
    jumlah_asisten = input_integer("Masukkan jumlah asisten awal: ", 1)

    list_asisten_awal = []
    for i in range(jumlah_asisten):
        nama = input_string(f"Masukkan nama asisten awal ke-{i + 1}: ")
        list_asisten_awal.append(nama)
    asisten_awal_terkunci = tuple(list_asisten_awal)

    # Menginput satu asisten tambahan dan menggabungkan dengan tuple asisten awal
    print("\n=== INPUT ASISTEN TAMBAHAN ===")
    asisten_tambahan = input_string("Masukkan satu nama asisten tambahan: ")
    asisten_akhir = asisten_awal_terkunci + (asisten_tambahan,)

    # Menginput nama hari tugas lalu dikunci (tuple)
    print("\n=== INPUT HARI TUGAS ===")
    jumlah_hari = input_integer("Masukkan jumlah hari tugas: ", 1)

    list_hari = []
    for i in range(jumlah_hari):
        hari = input_string(f"Masukkan nama hari tugas ke-{i + 1}: ")
        list_hari.append(hari)
    hari_terkunci = tuple(list_hari)

    # Menginput pengecualian shift
    print("\n=== INPUT PENGECUALIAN JADWAL ===")
    asisten_halangan = input_string("Masukkan nama asisten yang ada halangan: ")
    hari_halangan = input_string("Masukkan hari halangan tersebut: ")

    # Memasangkan asisten dengan hari menggunakan nested loop
    print("\n=== KOMBINASI JADWAL SHIFT ===")
    ada_jadwal = False
    for asisten in asisten_akhir:
        for hari in hari_terkunci:
            if (asisten.lower() == asisten_halangan.lower()
                    and hari.lower() == hari_halangan.lower()):
                continue
            print(f"{asisten} bertugas pada hari {hari}")
            ada_jadwal = True

    if not ada_jadwal:
        print("Tidak ada kombinasi jadwal yang tersedia.")


program_utama()