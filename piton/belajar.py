from cuypy import start1
from libs import opening, exitprogram
from warung import start as warung_start
from facecuy.main import mulaiambilgambar


def options():
    option = int(input("Pilih opsi:\n1. Mulai permainan Cuypy\n2. apanjirini\n3. selfie jirlah\n Masukkan pilihan Anda (1/2/3): "))
    if option == 1:
        print("Memulai permainan Cuypy...")
        start1()
    elif option == 2:
        print("Memulai warung piton...")
        warung_start()
    elif option == 3:
        print("Memulai deteksi wajah...")
        mulaiambilgambar()
        
def main():
    opening()
    options()
    exitprogram()

if __name__ == "__main__":
    main()