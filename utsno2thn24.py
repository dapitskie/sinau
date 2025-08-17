noproduk = int(input("Pilih produk (1: Soda - 10.000, 2: Snack - 5.000):"))
jumlah = int(input("Jumlah produk: "))

match noproduk:
    case 1:
        hargatotal = 10000 * jumlah
        print(f"Total harga Soda: {hargatotal}")
    case 2:
        hargatotal = 5000 * jumlah
        print(f"Total harga Snack: {hargatotal}")

jumlahbayar = int(input("Jumlah bayar: "))

while jumlahbayar < hargatotal:
    print("Jumlah bayar kurang, silakan masukkan jumlah yang cukup.")
    jumlahbayar = int(input("Jumlah bayar: "))
kembalian = jumlahbayar - hargatotal
print(f"Kembalian Anda: {kembalian}")
if kembalian < 0:
    print ("Transaksi berhasil, selamat menikmati produk Anda!")
print ("Transaksi berhasil, selamat menikmati produk Anda!")