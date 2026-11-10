# Memeriksa Inputan String
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

def program_utama():
    daftar_anggota = []
    print("=== PENDAFTARAN ANGGOTA KLUB ROBOTIKA ===")
    while True:
        nama = input_string("Masukkan nama calon anggota (ketik 'selesai' untuk selesai): ")
        if nama.lower() == "selesai":
            if len(daftar_anggota) == 0:
                print("[Peringatan] Minimal harus ada 1 calon anggota sebelum selesai!\n")
                continue
            break
        daftar_anggota.append(nama)

    print("\n--- Evaluasi Nama Calon Anggota ---")
    for nama in daftar_anggota:
        if nama.lower() == "admin" or len(nama) < 1:
            print(f"Nama '{nama}' -> TIDAK VALID")
        else:
            print(f"Nama '{nama}' -> Valid")

    print("\n--- Penghapusan Anggota Penyusup ---")
    penyusup = input_string("Ketikkan satu nama penyusup yang ingin dihapus: ")
    try:
        daftar_anggota.remove(penyusup)
        print(f"Berhasil: Nama '{penyusup}' telah dihapus dari sistem.")
    except ValueError:
        print(f"Aman: Nama '{penyusup}' tidak ditemukan di dalam sistem. Program tidak crash.")

    print("\nDaftar Anggota Tersisa:", daftar_anggota)


program_utama()