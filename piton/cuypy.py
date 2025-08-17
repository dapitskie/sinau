import random

cuypy_position = random.randint(1,4 ) 

def start1():
    while True :
        bentukgoa = "|_|"
        goakosong = [bentukgoa] * 4

        goa = goakosong.copy()
        goa[cuypy_position - 1] = "|o|"

        goskosong = "".join(goakosong)
        goa = "".join(goa)
        
        print(f"Selamat datang,  Coba perhatikan goa berikut: \n\n {goskosong}\n")

        pilihanuser = int(input("Pilih goa mana yang ingin Anda masuki (1-4): "))

        while pilihanuser < 1 or pilihanuser > 4:
            print("Pilihan tidak valid. Silakan pilih goa antara 1 dan 4.")
            pilihanuser = int(input("Pilih goa mana yang ingin Anda masuki (1-4): "))

        if pilihanuser == cuypy_position:
            print(f"Selamat! Anda menemukan Cuypy di goa {pilihanuser}!")
        else:
            print(f"Maaf. Cuypy tidak ada di goa {pilihanuser}.")
        
        import belajar
        playagain = input("Apakah Anda ingin bermain lagi? (y/n): ")
        if playagain.lower() != 'y':
            print("Terima kasih telah bermain! Sampai jumpa lagi!")
            belajar.options()

if __name__ == "__main__":
    start1()