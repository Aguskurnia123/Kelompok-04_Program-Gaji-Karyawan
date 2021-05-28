import csv

print('SIGN IN')

with open('Book1.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    database = []
    for row in reader:
        database.append(row)

def login():
    global Username
    global Password
    #global row

    loggedin = False
    while not loggedin:
        Username = input('Nama  : ')
        Password = input('NIK   : ')
        for row in database:
            Username_File = row['Nama']
            Password_File = row['NIK']
            if (Username_File == Username and
                Password_File == Password ):
                loggedin = True
                print('Login Berhasil.')
        if loggedin is not True:
            print ('Login gagal, silahkan \n [1] masukkan kembali \n [2] hubungi admin ')
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
#Mencoba memanggil identitas karyawan
display()

#1. Tunjangan
def tunjang():
    global tunjab
    global tang
    global tuntang
    global tunsta
    global tot_tun

    tang = int(database[int(Password[3])]['Tanggungan'])
    #TUNJANGAN DI DAPAT DARI JABATAN
    if gol == 1:
        tunjab = 200000
    elif gol == 2:
        tunjab = 150000
    else:
        tunjab = 100000
    #TUNJANGAN DARI TANGGUNGAN
    if tang == 1:
        tuntang = 200000
    elif tang == 2:
        tuntang = 2 * 200000
    elif tang == 3:
        tuntang = 3 * 200000
    else:
        tuntang = 4 * 200000
    #TUNJANGAN DARI STATUS
    if status == 'Single':
        tunsta = 100000
    elif status == 'Keluarga':
        tunsta = 300000
    else:
        tunsta = 0
    tot_tun = int(tunjab+tuntang+tunsta)

#2. Bonus
def bonus():
    global Bonus
    global jam_lbur
    global tot_bonus
    global ach
    jam_lbur = int(database[int(Password[3])]['Jam Lembur'])

    #Bonus Jam Lembur
    if jab == "Direktur utama":
        if 0 <= jam_lbur < 3:
            Bonus = 100000*jam_lbur
        else:
            Bonus = 100000*3
    elif jab == "Direktur keuangan":
        if 0 <= jam_lbur < 5:
            Bonus = 75000*jam_lbur
        else:
            Bonus = 75000*5
    elif jab == "Direktur Personalia":
        if 0 <= jam_lbur < 0:
            Bonus = 75000*jam_lbur
        else:
            Bonus = 75000*0
    elif jab == "Direktur Pemasaran":
        if 0 <= jam_lbur < 3:
            Bonus = 75000*jam_lbur
        else:
            Bonus = 75000*3
    elif jab == "Manager Personalia":
        if 0 <= jam_lbur < 3:
            Bonus = 50000*jam_lbur
        else:
            Bonus = 50000*3
    elif jab == "Admin":
        if 0 <= jam_lbur < 4:
            Bonus = 50000*jam_lbur
        else:
            Bonus = 50000*4
    elif jab == "Manager Pemasaran":
        if 0 <= jam_lbur < 5:
            Bonus = 50000*jam_lbur
        else:
            Bonus = 50000*5
    elif jab == "Manager Pabrik":
        if 0 <= jam_lbur < 4:
            Bonus = 50000*jam_lbur
        else:
            Bonus = 50000*4
    elif jab == "Manager":
        if 0 <= jam_lbur < 5:
            Bonus = 50000*jam_lbur
        else:
            Bonus = 50000*5
    elif jab == "Akuntan":
        if 0 <= jam_lbur < 4:
            Bonus = 50000*jam_lbur
        else:
            Bonus = 50000*4
    elif jab == "Akuntan":
        if 0 <= jam_lbur < 3:
            Bonus = 50000*jam_lbur
        else:
            Bonus = 50000*3
    #Bonus Achievement
    ach = int(database[int(Password[3])]['Gaji'])
    #Total Bonus
    tot_bonus = int(Bonus+ach)