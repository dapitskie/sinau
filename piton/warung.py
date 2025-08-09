def start():
    while True:
        print('ini adalah warung piton')
        harga = int(input('Masukkan harga barang: '))
        
        if harga == 0:
            print('Terima kasih telah berbelanja di warung piton!')
            break
    
if __name__ == "__main__":
    start()