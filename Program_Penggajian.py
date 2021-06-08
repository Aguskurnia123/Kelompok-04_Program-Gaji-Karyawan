import csv

salam = "Selamat Datang dalam Program Penggajian Karyawan."
print("\n" + salam.center(50))
print("")
batas = "=" * 30
print(batas.center(50, "="))
log_in = "=" * 10 + ' HALAMAN LOG IN ' + "=" * 10
print(log_in.center(50))
print(batas.center(50,"="))

with open('Book1.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    database = []
    for row in reader:
        database.append(row)

def login():
    global Username
    global Password
    print("Silahkan Masukan Nama dan NIK.\n")
    loggedin = False
    while not loggedin:
        Username = input('Nama  : ')
        Password = input('NIK   : ')
        x = Username.upper()
        for row in database:
            Username_File = row['Nama'].upper()
            Password_File = row['NIK']
            if (Username_File == x and
                Password_File == Password ):
                loggedin = True
                print('Login Berhasil.')
        if loggedin is not True:
            print ('Data anda tidak terdaftar di dalam database silahkan : \n [1] masukkan kembali \n [2] hubungi admin ')
            p = int(input(">>"))
            if p == 1:
                return login()
            elif p ==2:
                print("Silahkan hubungi\n"
                      "1. Untai(02345678)\n"
                      "2. Miami(025678001)")
                exit()
            else:
                exit()

# Sign In #
login()

def identitas():
    global jab
    global h
    global status
    global gol
    jab = str(database[int(Password[3])]['Jabatan'])
    h = int(database[int(Password[3])]['Hari'])
    status = str(database[int(Password[3])]['Status'])
    gol = int(database[int(Password[3])]['Golongan'])
    print('='*30)
    print('SELAMAT DATANG KARYAWAN')
    print('='*30)
    print('Nama                 : %s '% str(database[int(Password[3])]['Nama']))
    print('NIK                  : %s '% str(database[int(Password[3])]['NIK']))
    print('Jabatan              : %s '% jab)
    print('Golongan             : %s '% gol)
    print('Status sekarang      : %s '% status )
    print('Masuk kerja(hari)    : %s '% h)

def display():
    identitas()
    tampilan_menu()

#1. Tunjangan
def tunjang():
    global tunjab
    global tang
    global tuntang
    global tunsta
    global tot_tun

    tang = int(database[int(Password[3])]['Tanggungan'])
    # TUNJANGAN DI DAPAT DARI JABATAN
    if gol == 1:                    # Tunjangan Jabatan
        tunjab = 250000             # Nilai tunjangan Direktur Utama masuk ke dalam golongan 1
    elif gol == 2:                  # Nilai tunjangan Direktur keuangan,Direktur Personalia, dan
        tunjab = 2000000            # Direktur Pemasaran masuk ke dalam golongan 2
    elif gol == 3:                  # Nilai tunjangan Direktur keuangan,Direktur Personalia, dan
        tunjab = 150000             # Direktur Pemasaran masuk ke dalam golongan 3
    else:
        tunjab = 0
    # TUNJANGAN DARI TANGGUNGAN
    if tang == 1:                   # Tunjangan Tanggungan
        tuntang = 200000            # Tunjangan diperoleh dari jumlah tanggungan
    elif tang == 2:                 # Apabila memiliki 1 tanggungan maka memperoleh tunjangan sebesar Rp. 200.000
        tuntang = 2 * 200000        # Apabila memiliki 2 tanggungan maka memperoleh tunjangan sebesar Rp. 400.000
    else:                           # Apabila memiliki 3 atau lebih tanggungan maka memperoleh tunjangan
        tuntang = 3 * 200000        # sebesar Rp. 600.000
    # TUNJANGAN DARI STATUS
    if status == 'Single':          # Tunjangan Status
        tunsta = 100000             # Tunjangan diperoleh dari status single atau Berkeluarga
    elif status == 'Keluarga':      # Apabila single beroleh tunjangan sebesar Rp 100.000
        tunsta = 300000             # Apabila Keluarga beroleh tunjangan sebesar Rp 300.000
    else:
        tunsta = 0

    tot_tun = int(tunjab + tuntang + tunsta)

#2. Bonus
def bonus():
    global Bonus
    global jam_lbur
    global tot_bonus
    global ach
    global achievement
    jam_lbur = int(database[int(Password[3])]['Jam Lembur'])

    #Bonus Jam Lembur
    if jab == "Direktur utama":
        if jam_lbur < 3:
            Bonus = 100000*jam_lbur
        else:
            Bonus = 100000*3
    elif jab == "Direktur keuangan":
        if jam_lbur < 5:
            Bonus = 75000*jam_lbur
        else:
            Bonus = 75000*5
    elif jab == "Direktur Personalia":
        if jam_lbur < 5:
            Bonus = 75000*jam_lbur
        else:
            Bonus = 75000*0
    elif jab == "Direktur Pemasaran":
        if jam_lbur < 3:
            Bonus = 75000*jam_lbur
        else:
            Bonus = 75000*3
    elif jab == "Manager Personalia":
        if jam_lbur < 3:
            Bonus = 50000*jam_lbur
        else:
            Bonus = 50000*3
    elif jab == "Admin":
        if jam_lbur < 4:
            Bonus = 50000*jam_lbur
        else:
            Bonus = 50000*4
    elif jab == "Manager Pemasaran":
        if jam_lbur < 5:
            Bonus = 50000*jam_lbur
        else:
            Bonus = 50000*5
    elif jab == "Manager Pabrik":
        if jam_lbur < 4:
            Bonus = 50000*jam_lbur
        else:
            Bonus = 50000*4
    elif jab == "Manager":
        if jam_lbur < 5:
            Bonus = 50000*jam_lbur
        else:
            Bonus = 50000*5
    elif jab == "Akuntan":
        if jam_lbur < 4:
            Bonus = 50000*jam_lbur
        else:
            Bonus = 50000*4
    elif jab == "Akuntan":
        if jam_lbur < 3:
            Bonus = 50000*jam_lbur
        else:
            Bonus = 50000*3
    #Bonus Achievement
    ach = int(database[int(Password[3])]['Ach'])
    if ach == 1:
        achievement= 100000
    elif ach == 2:
        achievement= 200000
    else:
        achievement= 300000
    #Total Bonus
    tot_bonus = int(Bonus+achievement)
    
#3. Kasbon
def kasbon():
    global bon
    bon = int(database[int(Password[3])]['Kasbon'])

#4. Gaji
def gaji():
    global gaber
    global gapok
    tunjang()
    bonus()
    kasbon()
    print('='*35)
    print('========== GAJI KARYAWAN ==========')
    print('='*35)
    sala = int(database[int(Password[3])]['Gaji'])
    gapok = int(h * sala)
    gaber = int((gapok+tot_tun+tot_bonus)-(bon))
    print("- Gaji Pokok              %d "% gapok)
    print("- Tunjangan                %d "% tot_tun)
    print("- Bonus                    %d "% tot_bonus)
    print("- Kasbon                  %d "% (bon*(-1)))
    print("------------------------------------- +")
    print("Gaji                   Rp. %d " % gaber)
    rekening()

#5. Menu edit
def edit_biodata():
    print("silakan mengisi formulir berikut sesuai perubahan biodata anda.")
    Jabatan = str(input("Jabatan :"))
    hari_kerja = str(input('Jumlah hari kerja : '))
    lembur = str(input('Jumlah jam lembur: '))
    Tanggung = str(input('Jumlah tanggungan: '))
    stat = str(input('Status perkawinan (single/berkeluarga):'))
    kasbn = str(input('Jumlah kasbon: '))
    x = '        Surat Permohonan Perubahan\n-------------------------------------------\n\nKepada\nYth. Pimpinan perusahaan\nDi\nTempat\n\nAssalamulaikum Wr Wb.\n\nDengan hormat,\nDengan ini Saya Selaku Karyawan dari perusahaan yang Bapak/Ibu pimpin, saya hendak mengajukan\npermohonan perubahan terkait infomasi ataupun biodata karyawan sebagai berikut.\nNama              : {}\nNIK               : {}\nJabatan           : {}\nJumlah hari kerja : {}\nJumlah jam lembur : {}\nJumlah tanggungan : {}\nStatus perkawinan : {}\nJumlah Kasbon     : {}\n\nDemikian surat pernyataan perubahan ini saya sampaikan, atas perhatiannya saya\nucapkan terima kasih.\n\nWassalamualaikum Wr Wb.\n\nDengan Hormat,\nKaryawan Perusahaan\n\n\n\n...............'.format(Username,Password,Jabatan,hari_kerja,lembur,Tanggung,stat,kasbn)
    with open('Surat_Edit_Data_Diri.txt','w') as sp:
        sp.write(x)
        sp.close()
    cetak_surat()
#Menu Untuk Mencetak Surat Pernyataan Perubahan Biodata
def cetak_surat():
    with open('Surat_Edit_Data_Diri.txt', 'r') as sp:
        read = sp.read()
        print("="*30)
        print(read)
        print("=" * 30)
        sp.close()
    h = 'k'
    while h !='':
        cek = input('Apakah perubahan sudah benar (y/n)? :')
        cek = cek.lower()
        if cek == 'y':
            print('Mohon mencetak file Surat_Edit_Data_Diri.txt')
            tampilan_menu()
        elif cek == 'n':
            edit_biodata()
        else:
            print('Pilihan tidak ada. Mohon mengisi kembali')


#Rekening
def rekening():
    print('Apakah ingin mengambil gaji?(y/n)')
    kep = input(">> ")
    if kep != "y":
        tampilan_menu()
    else :
        print("Pilih Metode Pembayaran\n"
              "[1] Cash\n"
              "[2] Transfer")
        pem = int(input('>> '))
        if pem == 1:
              cetak()
        elif pem == 2:
              bank = int(input('Rekening Bank : '))
              print("Terima kasih Gaji Anda akan segera kami kirim\n"
                    "Apabila belum terkirim dapat hubungi admin.")
              with open('buku_rekening.csv','a') as f :
                  data_rekening = csv.writer(f, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL )
                  data_rekening.writerow([[database[int(Password[3])]['Nama']], str(bank)])
    tampilan_menu()    

        #Menu dalam Program
def tampilan_menu():
    print("="*30)
    pil_menu= ('Tampilan Menu\n'
          '[1] Tunjangan\n'
          '[2] Bonus\n'
          '[3] Kasbon\n'
          '[4] Gaji\n'
          '[5] Edit Identitas\n'
          '[6] LOGOUT ')
    print(pil_menu)
    menu = int(input("Pilih Menu>>"))
    
    if menu == 1:    #Menu Tunjangan
        tunjang()
        print('========== TUNJANGAN ==========')
        print('- Tunjangan Jabatan         Rp. %d ' % tunjab)
        print('- Tunjangan Tanggungan      Rp. %d ' % tuntang)
        print('- Tunjangan Status          Rp. %d ' % tunsta)
        print('------------------------------------- +')
        print('Total Tunjangan didapat     Rp. %d ' % tot_tun)
        x = 'yummy'
        while x != ' ':
            back = input('Kembali ke menu? (y) = ')
            back = back.lower()
            if back == 'y':
                return tampilan_menu()
            else:
                continue
    elif menu == 2: #Menu Bonus
        bonus()
        print('========== BONUS ==========')
        print('- Bonus Lembur              Rp. %d ' % Bonus)
        print('- Penghargaan               Rp. %d ' % achievement)
        print('------------------------------------- +')
        print('Total Bonus didapat         Rp. %d ' % tot_bonus)
        x = 'yummy'
        while x != ' ':
            back = input('Kembali ke menu? (y) = ')
            back = back.lower()
            if back == 'y':
                return tampilan_menu()
            else:
                continue
    elif menu == 3:  #Menu Kasbon
        kasbon()
        print('========== KASBON ==========')
        print('Kasbon anda sebesar Rp. %d '% bon)
        x = 'yummy'
        while x != ' ':
            back = input('Kembali ke menu? (y) = ')
            back = back.lower()
            if back == 'y':
                return tampilan_menu()
            else:
                continue    
    elif menu == 4: #Menu Gaji
        gaji()
    elif menu == 5:  #Menu Edit
        edit_biodata()
    elif menu == 6: #Menu Log Out
        login()
        tampilan_menu()      
    else:
        print("Pilihan tidak ada")
        tampilan_menu()

#Mencetak slip
#Fungsi Untuk Mencetak Slip Gaji Metode Cash
def cetak():
    x = '           == SLIP GAJI KARYAWAN ==\n'\
        '       ===============================\n'\
        'Nama    : {}\n'\
        'NIK     : {}\n'\
        '============================================\n'\
        'Gaji pokok  : {}\n'\
        'Tunjangan   : {}\n'\
        'Bonus       : {}\n'\
        'Kasbon      : {}\n'\
        '--------------------------------------------\n'\
        'Gaji bersih : {}\n'\
        '      Mengetahui\n'\
        '    Direktur Utama\n\n\n'\
        '        Mika\n' \
        '       NIK.1000'.format(Username,Password,gapok,tot_tun,tot_bonus,bon,gaber)
    with open('Slip_gaji.txt', 'w') as sp:
        sp.write(x)
        sp.close()
    with open('Slip_gaji.txt', 'r') as slip:
        file_slip = slip.read()
        print("=" * 30)
        print(file_slip)
        print("=" * 30)
        slip.close()
    print('Mohon mencetak file Slip_gaji.txt')
    print('Jika terjadi kesalahan mohon hubungi admin untuk konfirmasi.\n'
            '1. Untai(02345678)\n'
            '2. Miami(02567800) ')
    tampilan_menu() 
                  
if __name__ == '__main__':
    while(True):
        display()
        break

