angka = int(input("masukkan angka:"))

for i in range(1,angka +1):
    if(i % 2 == 0):
        print('*')
    else:
        print(i)