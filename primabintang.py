n = int(input("masukkan nilai:"))

def cek_prima(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


for i in range (1,n+1):
    if cek_prima(i):
        print("*")
    else:
        print(i)