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
