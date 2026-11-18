# Untuk input berupa teks (tidak boleh kosong)
def input_teks(pesan):
    while True:
        teks = input(pesan).strip()
        if teks == "":
            print("Peringatan: Input tidak boleh kosong! Silakan coba lagi.")
        else:
            return teks

def tampilkan_menu():
    print("\n=== PENGELOLA PLAYLIST MUSIK ===")
    print("1. Buat Playlist Baru")
    print("2. Tambah Lagu ke Playlist")
    print("3. Tampilkan Semua Playlist & Lagu")
    print("4. Cari Lagu")
    print("5. Hapus Lagu dari Playlist")
    print("6. Hapus Playlist")
    print("7. Keluar")

def main():
    playlists = {}
    while True:
        tampilkan_menu()
        pilihan = input_teks("Pilih menu (1-7): ")
        if pilihan == "1":
            nama_pl = input_teks("Masukkan nama playlist baru: ")
            if nama_pl in playlists:
                print("Playlist tersebut sudah ada!")
            else:
                playlists[nama_pl] = {}
                print(f"Playlist '{nama_pl}' berhasil dibuat.")
        elif pilihan == "2":
            nama_pl = input_teks("Masukkan nama playlist tujuan: ")
            if nama_pl in playlists:
                judul = input_teks("Masukkan judul lagu: ")
                penyanyi = input_teks("Masukkan nama penyanyi: ")
                playlists[nama_pl][judul] = penyanyi
                print(f"Lagu '{judul}' - {penyanyi} ditambahkan ke '{nama_pl}'.")
            else:
                print("Error: Playlist tidak ditemukan!")
        elif pilihan == "3":
            print("\n--- DAFTAR PLAYLIST ---")
            if len(playlists) == 0:
                print("Belum ada playlist.")
            else:
                for nama_pl, daftar_lagu in playlists.items():
                    print(f"\nPlaylist: {nama_pl}")
                    if len(daftar_lagu) == 0:
                        print("  (Belum ada lagu)")
                    else:
                        for judul, penyanyi in daftar_lagu.items():
                            print(f"  - {judul} oleh {penyanyi}")
        elif pilihan == "4":
            cari = input_teks("Masukkan judul lagu yang dicari: ")
            ditemukan = False
            for nama_pl, daftar_lagu in playlists.items():
                for judul, penyanyi in daftar_lagu.items():
                    if judul.lower() == cari.lower():
                        print(f"Ditemukan di playlist '{nama_pl}': {judul} - {penyanyi}")
                        ditemukan = True
            if not ditemukan:
                print("Lagu tidak ditemukan di playlist mana pun.")
        elif pilihan == "5":
            nama_pl = input_teks("Masukkan nama playlist: ")
            if nama_pl in playlists:
                judul = input_teks("Masukkan judul lagu yang ingin dihapus: ")
                if judul in playlists[nama_pl]:
                    del playlists[nama_pl][judul]
                    print(f"Lagu '{judul}' berhasil dihapus dari '{nama_pl}'.")
                else:
                    print("Error: Lagu tidak ditemukan di playlist tersebut!")
            else:
                print("Error: Playlist tidak ditemukan!")
        elif pilihan == "6":
            nama_pl = input_teks("Masukkan nama playlist yang ingin dihapus: ")
            if nama_pl in playlists:
                del playlists[nama_pl]
                print(f"Playlist '{nama_pl}' berhasil dihapus.")
            else:
                print("Error: Playlist tidak ditemukan!")
        elif pilihan == "7":
            print("Keluar dari program playlist.")
            break
        else:
            print("Peringatan: Pilihan tidak valid, masukkan angka 1-7.")

main()