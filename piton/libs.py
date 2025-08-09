import socket
from time import sleep
pcname = socket.gethostname()

def opening():
    style = "*" * (len(pcname)+4)
    print(style)
    print(f"**{pcname}**")
    print(style)
    
def exitprogram():
    print("Terima kasih telah menggunakan program ini. Sampai jumpa lagi!")
    sleep(1)
    print("Keluar dari program...") 
    
if __name__ == "__main__":
    opening()
    exitprogram()