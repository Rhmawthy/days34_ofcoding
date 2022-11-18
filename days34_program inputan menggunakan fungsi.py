#program menampilkan angka inputan menggunakan fungsi dan percaabangan


def number (nilai):
    if nilai %2 == 0:
         for i in range(2,nilai+1,2):
              print(i)
              
    elif nilai %2 != 0:
         for i in range(1,nilai+1,2):
              print(i)             
number(nilai = int(input("masukkan nilai")))

