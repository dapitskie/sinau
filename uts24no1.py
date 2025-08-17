
#membuat inputan untuk semua data sehingga dapat tervalidasi
suhu = float(input("Berapa suhu badan Anda? (dalam derajat Celcius, gunakan titik(.) jika suhu anda seperti 37.5 namun jika bulat maka isi seperti 37.0:"))
tekanan_darah = input("Bagaimana tekanan darah Anda? (rendah/normal/tinggi):")
batuk = input("Apakah Anda mengalami batuk? (ya/tidak):")
sesak_napas = input("Apakah Anda mengalami sesak napas? (ya/tidak): ")
sakit_tenggorokan = input("Apakah Anda mengalami sakit tenggorokan? (ya/tidak): ")
nyeriotot = input("Apakah Anda mengalami nyeri otot? (ya/tidak): ")
sakitkepala = input("Apakah Anda mengalami sakit kepala? (ya/tidak):")
mual = input("Apakah Anda mengalami mual? (ya/tidak):")
penglihatankabur = input("Apakah Anda mengalami penglihatan kabur? (ya/tidak):")
pusing = input("Apakah Anda mengalami pusing? (ya/tidak):")
diare = input("Anda mengalami diare? (ya/tidak):")

#membuat array untuk mengisi kondisi apa saja yang terpenuhi oleh inputan
diagnosis_sementara = []

if(suhu >= 37.5 and sesak_napas == "ya" and (tekanan_darah == "normal" or tekanan_darah == "tinggi")):
    diagnosis_sementara.append("Pneunomia")
if(37 <= suhu <= 37.5 and sakit_tenggorokan =="ya" and batuk == "ya"):
    diagnosis_sementara.append("Flu")
if(batuk == "ya" and nyeriotot == "ya" and suhu > 38.5):
    diagnosis_sementara.append("demam berdarah")
if(penglihatankabur == "ya" and mual == "ya" and sakitkepala == "ya"):
    diagnosis_sementara.append("Migrain")
if(sakitkepala == "ya" and mual == "ya" and pusing == "ya" and tekanan_darah == "rendah"):
    diagnosis_sementara.append("Vertigo")
if(36.0 <= suhu <= 37.5 and mual == "ya" and diare == "ya"):
    diagnosis_sementara.append("Keracunan Makanan")
if(suhu >= 37.5 and diare == "ya"):
    diagnosis_sementara.append("infeksi usus")
if(len(diagnosis_sementara) == 0):
    diagnosis_sementara.append("Penyakit tidak dikenali")

print("Diagnosis anda:")
for i in range(len(diagnosis_sementara)):
    print(diagnosis_sementara[i])
