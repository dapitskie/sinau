from cuypy import start
from libs import opening, exitprogram
from warung import start as warung_start

def options():
    option = int(input("Pilih opsi:\n1. Mulai permainan Cuypy\n2. apanjirini\nMasukkan pilihan Anda (1/2): "))
    if options ==1:
        print("Memulai permainan Cuypy...")
        start()
    elif option == '2':
        print("Memulai warung piton...")
        warung_start()
        
def main():
    opening()
    options()
    exitprogram()

if __name__ == "__main__":
    main()