import os

from datetime import datetime


menu = ('1. insert', '2. update', '3. delete', '0. stop')
def load_data(filename='data.csv'):
    data = list()
    try:
        with open(filename, 'r') as filecsv:
            for item in filecsv.readlines():
                text = item.replace('\n', '')
                txt_splitted = text.split(',')
                data.append(txt_splitted)
    except IOError as e:
        print(e)
    return data

def store_data(data, filename='data.csv'):
    try:
        tmp = list()
        for item in data:
                tmp.append(','.join(item)+'\n')
        with open(filename, 'w') as filecsv:
            filecsv.writelines(tmp)
    except IOError as e:
        print(e)

def show_data(data):
    os.system('cls')
    print('{0:^48}'.format('Daftar Transaksi'))
    print('{0:^48}'.format('='*48))
    print('{0:2s} {1:10s} {2:10} {3:6s} {4:10s} {5:20s}'.format('No','Tanggal', 'Nama', 'Jumlah', 'harga', 'Total Harga'))
    for i in range(len(data)):
        total = int(data[i][4])
        format_total = 'Rp {:,}'.format(total)
        print('{0:2d} {1:10s} {2:10s} {3:6s} {4:10s} {5:20s}'.format(i+1, data[i][0], data[i][1], data[0][2], data[i][3],format_total))


def insert(data):
    print('form transaksi')
    date = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
    nama = input("Masukkan nama barang: ")
    jumlah = input("Masukkan jumlah barang : ")
    harga = input("Masukkan harga barang: ")
    total = int(harga)*int(jumlah)
    total = str(total)
    date = datetime.now().strftime('%y-%m-%d')
    data.append([date, nama, jumlah, harga, total])
    store_data(data)


def update(data):
    index = int(input("Data pada nomor berapa yang akan diubah? "))
    index -= 1
    preview(data, index)
    nama = input("Masukkan nama: ")
    jumlah = input("Jumlah: ")
    harga  = input("Harga: ")
    confirm = input("apakah anda yakin ingin merubah data?[y/n] ")
    if confirm == 'y':
        data[index][1] = nama
        data[index][2] = jumlah
        data[index][3] = harga
        data[index][4] = jumlah * harga
        store_data(data)
    print("update Data Berhasil")

def delete(data):
    index = int(input("Data pada nomor berapa yang akan dihapus? "))
    index -= 1
    preview(data, index)
    confirm = input("Apakah anda yakin akan menghapus data?[y/n" )
    if confirm == 'y':
        data.pop(index)
        store_data(data)


def preview(data, index):
    os.system('cls')
    print('{0:2s} {1:10s} {2:10} {3:6s} {4:10s} {5:20s}'.format('No','Tanggal', 'Nama', 'Jumlah', 'harga', 'Total Harga'))
    print('{0:^48}'.format('='*48))
    for i in range(len(data)):
        total = int(data[i][4])
        format_total = 'Rp {:,}'.format(total)
        print('{0:2d} {1:10s} {2:10s} {3:6s} {4:10s} {5:20s}'.format(i+1, data[i][0], data[i][1], data[0][2], data[i][3], format_total))

data = load_data()
while True:
    show_data(data)
    print('\n', ' '.join(menu))
    command = int(input("Pilih menu: "))
    if command == 1:
        insert(data)
    elif command == 2:
        update(data)
    elif command == 3:
        delete(data)
    elif command == 0:
        break