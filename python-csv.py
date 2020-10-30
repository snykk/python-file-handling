#pertama import packages csv ke dalam source code terlebih dahulu
import csv

#tampilkan output yang nantinya akan dijadikan petunjuk oleh pengguna untuk transaksi
print("""
=============> Fitur Menu <=============
|  1. Melihat data Transaksi           |
|  2. Menambahkan data barang          |
|  3. Menghapus salah satu data barang |
|  4. Menghentikan transaksi serta     |
|     melihat data akhir               |
=======> Pilih Integer 1,2,3,4  <=======
""")

#membuat variabel 'total_pembelian' dimana isinya nanti total harga barang yang berhasil dibeli
total_pembelian = 0

#kita menggunakan perulangan while True agar sistem berhenti tepat ketika kita menginginkannya
while True:
    fiturMenu = int(input("L..> Masukkan angka!:\n [1]/[2]/[3]/[4]~~>")) #buat variabel yang berisi integer 1,2,3,4 sesuai ketentuan diawal
    
    #di percabangan ini pengguna dapat melihat barang apa saja yang sudah dibeli pada saat ini ketika menginputkan integer 1
    if fiturMenu == 1:
        # membaca file terlebih dahulu dengan function with open serta path file absolute disusul dengan format 'r' disimpan sementara di variabel 'filecsv'
        with open('dataTransaksi.csv', 'r') as filecsv: 
            #buat variabel bacaFile(sesuaiselera), delimiter yaitu format pemisah kolom saat di csv(sesuai format yang ada di laptop bisa diganti di control panel) saya saat ini pakai koma di beberapa kasus menggunakan semicolon, baca text dict menggunakan 'DictReader'
            bacaFile = csv.DictReader(filecsv, delimiter=',')
            #menampilkan isi file csv saat ini, di sini saya menggunakan colon sebagai pengganti operator space seperti spasi dan tab(\t)
            print(f"{'nama_barang' : <20}{'jumlah_barang' :<17}{'harga_barang' :<17}{'total_harga' :<20}{'tanggal_pembayaran' :10}")
            print('---------------------------------------------------------------------------------------------------------------')
            for sampel in bacaFile: #di sini saya menggunakan perulangan untuk memanggil dictionary pada setiap variabel sampel
                #dalam memanggil data dictionari menggunakan perulangan nantinya sintax seperti di bawah ini
                print('{:<25}{:<15}{:<17}{:<17}{:<15}'. format(sampel['nama_barang'], sampel['jumlah_barang'], sampel['harga_barang'], sampel['total_harga'], sampel['tanggal_pembayaran']))

    #di percabangan ini pengguna dapat menambahkan barang ke dalam data dictionary ketika menginputkan integer 2
    elif fiturMenu == 2:
        dictVar = dict() #membuat dictionary dengan variabel 'dictVar'

        #import datetime ke variabel datetime untuk nantiya digunakan di nilai variabel tanggal
        from datetime import datetime
        #format datetime.now() saya jadikan variabel 'tanggal'
        tanggal = datetime.now()
        
        #memberi inputan sesuai variabel yang diinginkan, seperti nama, jumlah. dan harga
        nama = input('Masukkan nama barang: ')
        jumlah = int(input('Masukkan jumlah barang: '))
        harga = int(input('Masukkan harga barang: '))
        total_harga = jumlah*harga #variabel 'total_harga berisi hasil kali variabel 'jumlah' dan 'harga'
        total_pembelian += total_harga

        #membuat dictionary untuk keys dari inputan tadi yang nantinya dijadikan value 
        dictVar['nama_barang'], dictVar['jumlah_barang'], dictVar['harga_barang'], dictVar['total_harga'], dictVar['tanggal_pembayaran'] = nama, jumlah, harga, total_harga, tanggal

        #membuat list dari cerminan pada value data dictionary
        namaKolom = ['nama_barang', 'jumlah_barang', 'harga_barang', 'total_harga', 'tanggal_pembayaran']

        #print data yang akan ditambahkan
        print("data yang berhasil ditambahkan ==> ", dictVar) 

        #data ditambahkan di fase ini dengan function with open serta path file absolute serta disusul format 'a'
        with open('dataTransaksi.csv', 'a', newline='') as filecsv:
            #membuat varibel 'tambahFile' di filecsv dengan  format DictWriter, dengan fieldnames pada 'namaKolom'
            tambahFile = csv.DictWriter(filecsv, fieldnames=namaKolom)
            #variabel 'tambahFile' ditulis berdasarkan variabel 'dictVar'
            tambahFile.writerow(dictVar)

    #di percabangan ini pengguna dapat mengeliminasi data berdasarkan nama barang yang sudah masuk ke dalam data transaksi ketika menginputkan integer 3
    elif fiturMenu == 3:

        #membuat list dari cerminan dari value data dictionary yang nantinya dieksekusi di fieldnames
        namaKolom = ['nama_barang','jumlah_barang','harga_barang','total_harga','tanggal_pembayaran']

        #membaca file terlebih dahulu dengan function with open serta path file absolute disusul dengan format 'r'
        with open('dataTransaksi.csv', 'r') as filecsv:
            #membuat variabel bacaFile dengan format DictReader pada filecsv menggunakan delimiter semicolon(sesuai laptop)
            bacaFile = csv.DictReader(filecsv, delimiter=',')

            #menampilkan isi file csv saat ini untuk memudahkan pengguna dalam mengeleminasi data transaksi di sini saya menggunakan colon sebagai pengganti operator space seperti spasi dan tab(\t)
            print(f"{'nama_barang' : <20}{'jumlah_barang' :<17}{'harga_barang' :<17}{'total_harga' :<20}{'tanggal_pembayaran' :10}")
            print('---------------------------------------------------------------------------------------------------------------')
            for sampel in bacaFile: #menggunakan perulangan pada setiap variabel 'sampel' dalam variabel 'bacaFile'
                #dalam memanggil data dictionari menggunakan perulangan nantinya sintax seperti di bawah ini
                print('{:<25}{:<15}{:<17}{:<17}{:<15}'. format(sampel['nama_barang'], sampel['jumlah_barang'], sampel['harga_barang'], sampel['total_harga'], sampel['tanggal_pembayaran']))

        #kita bisa membuat variabel baru yang nantinya dijodokan dengan value yang ada di dict untuk dihapus datanya(perbaris)
        namaBarangUntukDihapus = input('Masukkan nama barang untuk dihapus: ')  

        #buat list terlebih di variabel 'penampung' untuk nantinya dieksekusi
        penampung = list()
        #saty lagi di variabel 'akanDihapus'
        akanDihapus = list()

        #menghimpun data yang tidak diinputka oleh pengguna di variebl 'namaBarangUntukDihapus' untuk dipisahkan
        with open('dataTransaksi.csv', 'r') as filecsv: #file csv dibaca dahulu
            bacaFile = csv.DictReader(filecsv, delimiter=',') #menggunakan DictReader data dari filecsv dimasukkan ke dalam variabel 'bacaFile'
            for sampel in bacaFile: #perulangan pada setiap sampel dalam variabel 'bacaFile'
                if sampel['nama_barang'] == namaBarangUntukDihapus: #pencocokan data berdasarkan value dictionary dengan inputan pengguna
                    total_pembelian -= int(sampel['total_harga']) #di sini ketika value dict. terseleksi maka variabel'total_pembelian akan dikurangi dengan value dari dictionary di keys 'total_harga'
                    akanDihapus.append(sampel) #akan dimasukkan ke dalam variabel 'akanDihapus' nantinya akan ditampilan setelah percabangan berakhir
                    continue #dilewati
                else: #nah data akan masuk ke else jika value dari keys yang ada dalam dict. tidak sesuai dengan inputan pengguna
                    penampung.append(sampel) #data akan ditampung ke dalam variabel 'penampung' untuk ditulis ulang di proses selanjutnya

        #menulis ulang data yang tidak sesuai dengan inputkan oleh pengguna di sini menggunakan path absolute dan format 'w' serta newline agar nanti data tidak terpisah oleh enter
        with open('dataTransaksi.csv', 'w', newline='') as filecsv: 
            tulisFile = csv.DictWriter(filecsv, fieldnames=namaKolom) #menggunakan DictWriter yang nantinya dimasukkan ke dalam variabel tulisFile
            tulisFile.writeheader() 
            #menggunakan writerows(tidak perlu perulangan ketika menulis dictionary) yang ditambakan dari list penampung
            tulisFile.writerows(penampung)

        #menampilan baris data yang berhasil dieleminasi/dihapus
        print("========== Data yang berhasil dihapus ==========\n=>", akanDihapus)

    #di percabanga ini ketika pengguna menginputkan integer 4 maka program akan berhenti dijalankan dan menampilan data akhir transaksi
    elif fiturMenu == 4:
        # file dibaca dahulu sebelum ditampilan ke dalam terminal
        with open('dataTransaksi.csv', 'r') as filecsv:
            #buat variabel bacaFile(sesuaiselera), delimiter yaitu format pemisah kolom saat di csv(sesuai format yang ada di laptop bisa diganti di control panel)
            bacaFile = csv.DictReader(filecsv, delimiter=',') #menggunakan DictReader karena kita menggunakan format dictionary 
            #menampilkan isi file csv saat ini di sini saya menggunakan colon sebagai pengganti operator space seperti spasi dan tab(\t)
            print("\n\n===================================>  Struk Pembelian  <====================================\n")
            print(f"{'nama_barang' : <20}{'jumlah_barang' :<17}{'harga_barang' :<17}{'total_harga' :<20}{'tanggal_pembayaran' :10}")
            print('--------------------------------------------------------------------------------------------')
            for sampel in bacaFile:#menggunakan perulangan pada setiap variabel 'sampel' dalam variabel 'bacaFile'
                #dalam memanggil data dictionari menggunakan perulangan nantinya sintax seperti di bawah ini
                print('{:<25}{:<15}{:<17}{:<17}{:<15}'. format(sampel['nama_barang'], sampel['jumlah_barang'], sampel['harga_barang'], sampel['total_harga'], sampel['tanggal_pembayaran']))
            print(f"{'Total Pembayaran'}{' ' : <40}",'Rp', "{:,}".format(total_pembelian)) #untuk menghitung total pembayaran saya menggunakan format ribuan dan colon sebagai operator space supaya nantinya nilai akan lurus di bawah keys 'total_harga' pada terminal 
            print("========================> Terimakasi telah berkunjung di toko kami <=========================") #kalimat tampilan terakhir dari sistem ketika program akan berhenti
            break #fungsi 'break' untuk menghentikan looping utama pada while

