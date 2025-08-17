nomorarmstrong = int(input("masukkkan angka yang akan dideteksi sebagai armstrong:"))

banyakangka= len(str(nomorarmstrong))

awal = nomorarmstrong

total = 0

while nomorarmstrong > 0:
    digit = nomorarmstrong % 10
    total += digit ** banyakangka
    nomorarmstrong = nomorarmstrong // 10

if total == awal:
    print('angka anda terdeteksi armstrong')
else:
    print('angka anda tidak terdekteksi armstrong')