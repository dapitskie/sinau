data_mahasiswa = []
def input_data_mahasiswa():
    m = int(input("masukkan jumlah mahasiswa yang ingin diinput:"))
    while len(data_mahasiswa) <m:
        nama = input("Masukkan nama mahasiswa: ")
        nilai = float(input("Masukkan nilai mahasiswa: "))
        
        data_mahasiswa.append({
            'nama': nama,
            'nilai': nilai
        })

def tampilkan_data_mahasiswa():
    if  len(data_mahasiswa) == 0 :
        print("Tidak ada data mahasiswa yang tersedia.")
        return
    
    print("\nData Mahasiswa:")
    for i in range(len(data_mahasiswa)):
        mahasiswa = data_mahasiswa[i]
        print(f"{i}. Nama: {mahasiswa['nama']}, Nilai: {mahasiswa['nilai']}")
        
def cari_mahasiswa():
    if len(data_mahasiswa) == 0:
        print("Tidak ada data mahasiswa yang tersedia.")
        return
    
    nomor_cari = input(float("Masukkan nilai untuk mencari mahasiswa ingin dicari: "))
    ditemukan = False
    
    for mahasiswa in data_mahasiswa:
        if mahasiswa['nilai'] == nomor_cari:
            print(f"Data ditemukan: Nama: {mahasiswa['nama']}, Nilai: {mahasiswa['nilai']}")
            ditemukan = True
            break
            
    if not ditemukan:
        print("Data mahasiswa tidak ditemukan.")
        
        
def data_top3_tertinggi():
    if len(data_mahasiswa) < 3:
        print("Jumlah mahasiswa kurang dari 3, tidak dapat menampilkan top 3.")
        return
    data_mahasiswa.sort(key = lambda x: x['nilai'], reverse = True)
    for i in range(3):
        print(f"Mahasiswa {i+1}: Nama: {data_mahasiswa[i]['nama']}, Nilai: {data_mahasiswa[i]['nilai']}")

def mendeteksilulus():
    for mahasiswa in data_mahasiswa:
        if mahasiswa['nilai'] >= 60:
            print(f"{mahasiswa['nama']} lulus dengan nilai {mahasiswa['nilai']}")
        else:
            print(f"{mahasiswa['nama']} tidak lulus dengan nilai {mahasiswa['nilai']}")

def mengurutkan_nilai():
    if len(data_mahasiswa) == 0:
        print("Tidak ada data mahasiswa yang tersedia.")
        return
    
    data_mahasiswa.sort(key=lambda x: x['nilai'], reverse=True)
    print("\nData Mahasiswa setelah pengurutan berdasarkan nilai:")
    tampilkan_data_mahasiswa()
    
while True:
    print("\n===== MENU UTAMA =====")
    print("1. Input Data Mahasiswa")
    print("2. Tampilkan Data Mahasiswa")
    print("3. Cari Mahasiswa berdasarkan Nilai")
    print("4. Tampilkan Top 3 Nilai Tertinggi")
    print("5. Deteksi Kelulusan")
    print("6. Urutkan Data berdasarkan Nilai")
    print("0. Keluar")

    pilihan = input("Pilih menu (0-6): ")

    if pilihan == "1":
        input_data_mahasiswa()
    elif pilihan == "2":
        tampilkan_data_mahasiswa()
    elif pilihan == "3":
        cari_mahasiswa()
    elif pilihan == "4":
        data_top3_tertinggi()
    elif pilihan == "5":
        mendeteksilulus()
    elif pilihan == "6":
        mengurutkan_nilai()
    elif pilihan == "0":
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")