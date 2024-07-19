def tambah(*args):
    hasil = 0
    for data in args:
        hasil += data
    print(hasil)

def kurang(*args):
    hasil = 0
    for data in args:
        hasil -= data
    print(hasil)

def kali(*args):
    hasil = 1
    for data in args:
        hasil *= data
    print(hasil)

def bagi(*args):
    try:
        hasil=args[0]
        for data in args[1:]:
            hasil /= data
        print(hasil)
    except ZeroDivisionError:  
        print("tidak bisa membagi dengan 0")

def pangkat(angka:int,n:int)-> int :
    hasil = angka**n
    print(hasil)
