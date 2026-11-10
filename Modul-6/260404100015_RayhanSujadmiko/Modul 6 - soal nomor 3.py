# Memeriksa Inputan Integer
def input_integer_positif(pesan):
    while True:
        try:
            teks = input(pesan).strip()
            if teks == "":
                raise ValueError("Input tidak boleh kosong!")
            try:
                angka = int(teks)
            except ValueError:
                raise ValueError("Input tidak sesuai! Harus berupa angka bulat (integer).")
            
            if angka < 0:
                raise ValueError("Input tidak sesuai! Tidak boleh bernilai negatif.")
            
            if angka == 0:
                raise ValueError("Input tidak sesuai! Jumlah harus lebih dari 0.")
            return angka
        except ValueError as pesan_error:
            print(f"[Peringatan] {pesan_error} Coba lagi.\n")


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
            print(f"[Peringatan] {pesan_error} Coba lagi.\n")


# Memastikan nama PC berupa teks:"PC-01" atau "Lab 2", bukan angka, dan mengandung minimal satu huruf
def input_nama_pc(pesan):
    while True:
        try:
            nilai = input(pesan).strip()
            if nilai == "":
                raise ValueError("Input tidak boleh kosong!")
            try:
                int(nilai)
                angka = True
            except ValueError:
                angka = False
            
            if angka:
                raise ValueError("Input tidak sesuai! Nama harus berupa teks (string), bukan angka.")
            
            ada_huruf = False
            for karakter in nilai.lower():
                if "a" <= karakter <= "z":
                    ada_huruf = True
            if not ada_huruf:
                raise ValueError("Input tidak sesuai! Nama harus mengandung huruf.")
            return nilai
        except ValueError as pesan_error:
            print(f"[Peringatan] {pesan_error} Coba lagi.\n")

# Fungsi Evaluasi PC
def evaluasi_pc(status, ram_input):
    ram_angka = int(ram_input)
    if ram_angka < 0:
        return "Tidak Layak"
    if status.lower() == "normal" and ram_angka >= 8:
        return "Layak"
    else:
        return "Tidak Layak"

def program_utama():
    inventaris = []
    print("=== SISTEM PENDATAAN INVENTARIS PC ===")
    jumlah_pc = input_integer_positif("Masukkan jumlah PC yang ingin didata: ")

    for i in range(jumlah_pc):
        print(f"\n--- Data PC ke-{i + 1} ---")
        nama = input_nama_pc("Nama PC: ")
        status = input_string("Status (Normal/Rusak): ")
        ram = input_integer_positif("Kapasitas RAM (GB): ")
        inventaris.append([nama, status, ram])

    print("\n=== HASIL EVALUASI SELURUH PC ===")
    for pc in inventaris:
        nama_pc = pc[0]
        status_pc = pc[1]
        ram_pc = pc[2]

        try:
            kelayakan = evaluasi_pc(status_pc, ram_pc)
        except (ValueError, TypeError):
            kelayakan = "Format RAM Kacau"
        print(f'{{ "PC": "{nama_pc}", "Status": "{kelayakan}" }}')


program_utama()