# Untuk input berupa teks (tidak boleh kosong)
def input_teks(pesan):
    while True:
        teks = input(pesan).strip()
        if teks == "":
            print("Peringatan: Input tidak boleh kosong! Silakan coba lagi.")
        else:
            return teks

def tampilkan_menu():
    print("\n=== MENU TO-DO LIST ===")
    print("1. Tambah Tugas")
    print("2. Tampilkan Semua Tugas")
    print("3. Tandai Tugas Selesai")
    print("4. Hapus Tugas")
    print("5. Jumlah Tugas Selesai & Belum")
    print("6. Keluar")

def main():
    todo_list = {}
    while True:
        tampilkan_menu()
        pilihan = input_teks("Pilih menu (1-6): ")
        if pilihan == "1":
            tugas = input_teks("Masukkan nama tugas: ")
            if tugas in todo_list:
                print("Tugas tersebut sudah ada di dalam daftar.")
            else:
                todo_list[tugas] = "Belum Selesai"
                print(f"Tugas '{tugas}' berhasil ditambahkan.")
        elif pilihan == "2":
            print("\n--- DAFTAR TUGAS ---")
            if len(todo_list) == 0:
                print("Belum ada tugas.")
            else:
                nomor = 1
                for tugas, status in todo_list.items():
                    print(f"{nomor}. {tugas} [{status}]")
                    nomor += 1
        elif pilihan == "3":
            tugas = input_teks("Masukkan nama tugas yang sudah selesai: ")
            if tugas in todo_list:
                todo_list[tugas] = "Selesai"
                print(f"Tugas '{tugas}' berhasil ditandai Selesai.")
            else:
                print("Error: Tugas tidak ditemukan!")
        elif pilihan == "4":
            tugas = input_teks("Masukkan nama tugas yang ingin dihapus: ")
            if tugas in todo_list:
                del todo_list[tugas]
                print(f"Tugas '{tugas}' berhasil dihapus.")
            else:
                print("Error: Tugas tidak ditemukan!")
        elif pilihan == "5":
            selesai = 0
            belum = 0
            for status in todo_list.values():
                if status == "Selesai":
                    selesai += 1
                else:
                    belum += 1
            print(f"\nJumlah tugas Selesai       : {selesai}")
            print(f"Jumlah tugas Belum Selesai : {belum}")
        elif pilihan == "6":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Peringatan: Pilihan tidak valid, masukkan angka 1-6.")

main()