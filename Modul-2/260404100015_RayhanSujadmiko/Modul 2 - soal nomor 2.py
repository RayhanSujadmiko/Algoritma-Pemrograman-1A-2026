#Supermarket KOPERASI NDESO 
#diketahui kasir menyebutkan jika total belanjaan siti merupakan = 
#Kelipatan Rp.100.000 = seluruh belanjanya digratiskan
#Kelipatan Rp.50.000 = seluruh belanjanya diskon 50%
#kelipatan Rp10.000 = seluruh belanjanya diskon 20%
#jika total belanja >= Rp.200.000 (bukan kelipatan) = diskon 10%
#jika tidak memenuhi syarat diatas maka tidak ada diskon/membayar harga normal

#Memasukan total belanjaan
def total_belanja(pesan):
    while True:
        teks = input(pesan).strip()
        if teks == "":
            print("Input-an tidak boleh kosong, silahkan isi angka")
            continue
        try:
            nilai = int(teks)
        except ValueError:
            print("(teks) bukan bilangan bulat...")
            continue
        if nilai < 0:
            print("Total belanja tidak boleh negatif")
            continue
        return nilai

def rupiah(angka):
    return "Rp" + f"(angka:,.of)".replace(",",".")

subtotal = total_belanja("Masukan total belanja (Rp): ")

#Pengecekan kelipatan dan diskon
if subtotal % 100000 == 0:
    diskon = 100
    kondisi = "Kelipatan Rp100.000 (seluruh belanjanya digratiskan)"
elif subtotal % 50000 == 0:
    diskon = 50
    kondisi = "Kelipatan Rp50.000 (seluruh belanjanya diskon 50%)"
elif subtotal % 10000 == 0:
    diskon = 20
    kondisi = "Kelipatan Rp10.000 (seluruh belanjanya diskon 20%)"
elif subtotal >= 200000:
    diskon = 10
    kondisi = "Total belanja >= Rp200.000 (diskon 10%)"
else:
    diskon = 0
    kondisi = "Tidak memenuhi syarat diskon"

#Menghitung total belanja setelah diskon
setelah_diskon = subtotal * (diskon / 100)
total = subtotal - setelah_diskon

#Tenary Operator Status Poin Keanggotaan
status_poin = "Poin Bertambah" if total > 0 else "Tidak Ada Poin"

#Output hasil
print("\n=== STRUK BELANJA ===")
print("Total Belanja Awal = Rp.",subtotal)
print("Promo/Diskon = ",kondisi)
print("Diskon = ", diskon, "%")
print("Total Belanja Setelah Diskon = Rp.",int(total))
print("Status Poin Keanggotaan = ",status_poin)

#SELESAI