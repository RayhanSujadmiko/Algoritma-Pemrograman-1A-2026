# Untuk input angka (tidak boleh kosong, tidak boleh huruf, tidak boleh negatif)
def input_angka_positif(pesan):
    while True:
        data = input(pesan).strip()
        if data == "":
            print("Peringatan: Input tidak boleh kosong! Silakan masukkan angka.")
            continue
        try:
            angka = int(data)
            if angka < 0:
                print("Peringatan: Nilai tidak boleh negatif! Silakan masukkan angka 0 atau lebih.")
            else:
                return angka
        except ValueError:
            print("Peringatan: Input tidak sesuai! Harus berupa bilangan bulat (angka), bukan huruf/teks.")

# Untuk input nama orang (tidak boleh kosong dan tidak boleh berupa angka)
def input_nama_orang(pesan):
    while True:
        nama = input(pesan).strip()
        if nama == "":
            print("Peringatan: Nama tidak boleh kosong! Silakan coba lagi.")
        else:
            try:
                float(nama)
                print("Peringatan: Input tidak sesuai! Nama harus berupa teks/huruf, bukan angka.")
            except ValueError:
                return nama

def isi_data_set(nama_kategori):
    data_set = set()
    jumlah = input_angka_positif(f"\nMasukkan jumlah {nama_kategori}: ")
    for i in range(jumlah):
        nama = input_nama_orang(f"Masukkan nama ke-{i+1}: ")
        data_set.add(nama)
    return data_set

def main():
    undangan = isi_data_set("Daftar Undangan")
    webinar_a = isi_data_set("Peserta Webinar A")
    webinar_b = isi_data_set("Peserta Webinar B")

    print("\n=== HASIL ANALISIS KEHADIRAN WEBINAR ===")
    semua_peserta = webinar_a | webinar_b
    print("1. Semua peserta kedua webinar       :", semua_peserta)  # Union Function
    hadir_keduanya = webinar_a & webinar_b
    print("2. Peserta hadir di keduanya         :", hadir_keduanya) # Intersection Function
    salah_satu = webinar_a ^ webinar_b
    print("3. Peserta hanya di salah satu       :", salah_satu) # Symmetric Difference Function
    tidak_hadir = undangan - semua_peserta
    print("4. Undangan yang tidak hadir         :", tidak_hadir)    # Difference Function

main()