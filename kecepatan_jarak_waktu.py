
#Dio kesusahan dalam mengerjakan soal fisikanya tentang mengetahui jarak(km),waktu(jam) dan kecepatan (km/jam)
#contoh soalnya

#1.Dio mengendarai mobilnya dari rumah ke kantor yang berjarak sekitar 20 km dengan waktu 2 jam di perjalanan.
# Maka berapakah kecepatan  dari mobil Dio tersebut ?
#2.Dio lari dengan kecepatan 30 km/jam 
# Maka, berapakah jarak yang ditempuh oleh Denis setelah 2 jam berlari ?
#3 jika Dio berkendara dengan kecepatan 80 km/jam,maka berapakah waktu yang dibutuhkan Dio dari kendari ke makasar 
#apabila jarak antar kedua kota tersebut adalah 1000 km,berapakah waktu yang dibutuhkan untuk sampai?

##buatlah sebuah program yang dapat di inputkan user untuk membantu Dio mengerjakan soal fisikanya
#yang dapat menghitung jarak,waktu dan kecepatan
''''' 
v = kecepatan (km/jam)
s = jarak (km)
t = waktu (jam)
rumus_kecepatan = s / t
rumus_jarak     = t * v
rumus_waktu     = s / v
'''''
#input  : v = kecepatan ; s = jarak  ; t = waktu 

#proses :
# mencari kecepatan dalam soal no 1 
#mencari jarak dalam soal no 2
#mencari waktu dalam soal no 3


#output :
''''' mengetahui kecepatan sesuai inputan ; mengetahui jarak sesuai inputan ; mengetahui waktu sesuai inputan '''''
print("==== Halo saya suka fisika ====")
print("ketik 1 untuk mencari kecepatan ")
print("ketik 2 untuk mencari jarak ")
print("ketik 3 untuk mencari waktu ")
pill = int(input("masukkan pilihan :"))

if pill == 1 :
    s = int(input("masukkan jarak :"))
    t = int(input("masukkan waktu :"))
    rumus_kecepatan = s // t
    print("kecepatan yang dibutuhkan adalah",rumus_kecepatan,"km/jam")

elif pill == 2 :
    t = int(input("masukkan waktu :"))
    v = int(input('masukkan kecepatan :'))
    rumus_jarak = t * v
    print("jarak yang dibutuhkan adalah",rumus_jarak,"km")

elif pill == 3 :
    s = int(input("masukkan jarak :"))
    v = int(input("masukkan kecepatan :"))
    rumus_waktu = s // v
    print("waktu yang dibutuhkan adalah",rumus_waktu,"jam")

else :
    print("pilihan salah !!")