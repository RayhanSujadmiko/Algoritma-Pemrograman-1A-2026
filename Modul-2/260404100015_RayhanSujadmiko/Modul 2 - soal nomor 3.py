#Reaktor Nuklir Chernobyl
#diketahui jika suhu > 1000 derajat 
#Cek tekanan > 50 Bar = Peringatan MELTDOWN! SEGERA EVAKUASI!
#Cek tekanan < 50 Bar = Bahaya Suhu, Segera Turunkan Daya!
#jika suhu < 1000 dan > 500
#Cek tekanan > 30 Bar = Tekanan tidak stabil, jika < 30 Bar = Tekanan stabil
#Jika suhu <= 500 derajat = Reaktor belum cukup panas

def baca_angka(pesan, nama):
    while True:
        teks = input(pesan).strip()
        if teks == "" :
            print(f"(nama) tidak boleh kosong. Silahkan isi angka!")
            continue
        try:
            nilai = float(teks.replace(".","."))
        except ValueError:
            print(f"(teks) bukan angka. Tolong Masukkan angka!")
            continue
        return nilai

#Inputan suhu dan tekanan
suhu = float(input("Masukkan suhu reaktor (Celcius): "))
tekanan = float(input("Masukkan tekanan gas (Bar): "))

#Pengecekan kondisi reaktor
if suhu > 1000:
    if tekanan > 50:
        status = "MELTDOWN! SEGERA EVAKUASI!"
    else:
        status = "Bahaya Suhu, Segera Turunkan Daya!"
elif suhu < 1000 and suhu> 500:
    if tekanan > 30:
        status = "Peringatan, Tekanan tidak stabil"
    else:
        status = "Operasi Reaktor Normal"
else:
    status = "Reaktor Belum Cukup Panas"

#Tenary Operator untuk status pompa air
pompa = "Pompa Maksimal" if suhu > 800 else "Pompa Normal"

#Output hasil
print("\n=== LAPORAN REAKTOR ===")
print("Suhu Reaktor = ",suhu,"Celcius")
print("Tekanan Gas = ",tekanan,"Bar")
print("Status Bahaya = ",status)
print("Status Pompa Air = ",pompa)

#SELESAI 