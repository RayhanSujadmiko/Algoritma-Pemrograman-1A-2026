#Pintu Garasi Markas CIA
#diketahui Sistem pintu akan memecah ketiga digiit PIN
#PIN = kelipatan 5 (jika sebelum jam 12 = Garasi Pagi Terbuka), (jika setelah jam 12 = Garasi Malam Terbuka)
#PIN = bukan kelipatan 5 merupakan angka genap
#jumlah digit pertama dan digit ketiga = digit kedua (Garasi VIP Terbuka Khusus Bos)
#Jika polanya salah (Kode Genap Ditolak, Alarm Berbunyi!

def baca_pin(pesan):
    while True:
        teks = input(pesan).strip()
        if teks == "" :
            print("PIN tidak boleh kosong!. Silahkan isi 3 digit angka")
            continue
        if teks.startswith("-"):
            print("PIN tidak boleh negatif!")
            continue
        if not teks.isascii() or not teks.isdigit():
            print(f"'{teks}' bukan PIN yang valid. PIN hanya boleh berisi angka 0-9.")
            continue
        if len(teks) != 3:
            print(f"PIN harus tepat 3 digit (yang anda masukkan {len(teks)} digit)")
            continue
        return int(teks)

def baca_jam(pesan):
    while True:
        teks = input(pesan).strip()
        if teks == "" :
            print("Jam tidak boleh kosong. Silahkan isi angka 0-23")
            continue
        try:
            nilai = int(teks)
        except ValueError:
            print(f"'{teks}' bukan bilangan bulat. Masukkan angka 0-23")
            continue
        if nilai < 0:
            print("Jam harus di antara 0 sampai 23")
            continue
        if nilai > 23:
            print("Jam harus diantara 0 sampai 23")
            continue
        return nilai
    
#Memasukan PIN dan jam
pin = baca_pin("Masukkan PIN Garasi (3 digit): ")
jam = baca_jam("Masukkan jam kedatangan (0-23): ")

#Memisahkan digit secara matematis
digit1 = pin // 100
digit2 = (pin // 10) % 10
digit3 = pin % 10

if pin % 5 == 0:
    if jam < 12:
        status = "Garasi Pagi Terbuka"
    else:
        status = "Garasi Malam Terbuka, Lampu Dinyalakan"
elif pin % 2 == 0:
    if digit1 + digit3 == digit2:
        status = "Garasi VIP Terbuka Khusus Bos"
    else:
        status = "Kode Genap Ditolak, Alarm Berbunyi!"
else:
    status = "Akses Ditolak"

#Tenary Operator untuk status kamera CCTV
cctv = "Mode Malam Merekam" if jam > 18 else "Mode Siang Standby"

#Output hasil
print("\n=== LAPORAN GARASI CIA ===")
print("Digit Pertama = ",digit1)
print("Digit Kedua = ",digit2)
print("Digit Ketiga = ",digit3)
print("Status Pintu = ",status)
print("Status CCTV = ",cctv)

#SELESAI