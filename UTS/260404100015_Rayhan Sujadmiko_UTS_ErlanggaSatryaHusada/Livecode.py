# TICKET ORDERING SYSTEM
print("---TICKET BIOSKOP---")
print("TICKET REGULER = Rp40.000")
print("TICKET VIP = Rp75.000")
print("TICKET VVIP = Rp100.000")
print("Ticket apa yang ingin anda beli?")

# Input Jenis Ticket
jenis_tiket = input("Tiket, (reguler,vip,vvip) : ")

# Pengecekan Kondisi Ticket
if jenis_tiket == "reguler":
    harga1 = 40000
    print("Harga Minuman : Rp10.000")
    minuman = input("Ingin menambahkan minuman, (y/n) : ")
    hargaM = 10000
    if minuman == "y" :
        subtotal = harga1 + minuman
    else:
        subtotal = harga1
elif jenis_tiket == "vip" :
    harga2 = 75000
    print("Minuman Gratis Untuk Ticket VIP")
    subtotal = harga2
elif jenis_tiket == "vvip" :
    harga3 = 100000
    print("Minuman Gratis Untuk Ticket VVIP")
    subtutal = harga3

# Pengecekan Member Bioskop
member = input("Apakah pelanggan memiliki Member Card, (y/n) :")
if member == "y" :
    diskon = subtotal * 15/100
    total = subtotal - diskon
else:
    total = subtotal

print("Total Harga Ticket : ","Rp",total)

"""
PENJELASAN CODE
Pertama terdapat Output yang memberitahu bahwa ini adalah program ticket bioskop, 
Lalu pada input-an pelanggan diminta untuk memilih ticket mana yang ingin dibeli,
Setelah pelanggan mengisi input-an program akan mengecek ticket yang ingin dibeli pelanggan dan menentukan berapa harganya,
pada jenis ticket pertama terdapat pilihan minuman yang akan masuk ke harga dari ticket pertama,
pada jenis ticket kedua karena pelanggan membeli ticket vip maka ia berhak mendapat minuman gratis begitu pula denga ticket vvip,
lalu mengecek apakah ia memiliki member card.
"""