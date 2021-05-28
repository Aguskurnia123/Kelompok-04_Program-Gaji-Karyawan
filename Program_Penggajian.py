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
                      "1. Makmur(02345678)\n"
                      "2. Abdi(025678001)")
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