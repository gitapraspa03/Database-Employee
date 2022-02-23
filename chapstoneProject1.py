myList = [{'Id': '101', 'Birth_date': '1953-09-02', 'Name': 'Georgi', 'Gender': 'M', 'Hire_date': '1986-06-26'},
          {'Id': '102', 'Birth_date': '1964-06-02', 'Name': 'Bezalel', 'Gender': 'F', 'Hire_date': '1985-11-21'}, 
          {'Id': '103', 'Birth_date': '1957-04-20', 'Name': 'Anneke', 'Gender': 'F', 'Hire_date': '1989-06-02'},
          {'Id': '104', 'Birth_date': '1954-04-19', 'Name': 'Benny', 'Gender': 'M', 'Hire_date': '1994-09-15'}]

# Read Data Function
def read_Data():
    while True:
        print('''=======Report Data Karyawan=======\n
        1. Report Seluruh Data
        2. Report Data Tertentu
        3. Kembali ke Menu Utama
        ''')
        read = input("Silahkan Pilih Sub Menu Read Data[1-3] : ")
        if read == '1':
            if len(myList) != 0:
                print('Daftar Karyawan\n')
                print('   Id\t| Birth_date| \tName\t| Gender | Hire_date')
                for j, i in enumerate(myList):
                    print(f"{j+1}. {i['Id']}\t| {i['Birth_date']}| {i['Name']}\t|   {i['Gender']}\t | {i['Hire_date']}")
           
            else :
                print('Tidak Ada Data Karyawan')
            continue

        elif read == '2':
            if len(myList) != 0:
                addId = input("Masukkan Id: ")
                print(f"Data Karyawan dengan ID: {addId}")
                for j, i in enumerate(myList):
                    if i ['Id'] == addId:
                        print('   Id\t| Birth_date| \tName\t| Gender | Hire_date')
                        print(f"{j+1}. {i['Id']}\t| {i['Birth_date']}| {i['Name']}\t|   {i['Gender']}\t | {i['Hire_date']}")
                        break
                else:
                    print('Tidak ada Data Karyawan')
                continue

        elif read == '3':
            break

# Create Data
def create_Data():
    while True:
        print('''=======Menambah Data Karyawan=======\n
        1. Tambah Data Karyawan
        2. Kembali ke Menu Utama
        ''')
        create = input("Silahkan Pilih Sub Menu Create Data [1-2]: ")
        if create == '1':
            if len(myList) != 0:
                addId = input("Masukkan Id Karyawan: ")
                for j, i in enumerate(myList):
                    if  addId == i ['Id']:
                        print('Data karyawan sudah ada')
                        break
                else:
                    birthDate = input('Masukkan birth date (dd-mm-yyyy) : ')
                    namaKaryawan = input('Masukkan Nama : ').capitalize()
                    genderKaryawan = input('Masukkan Gender (M/F) : ').upper()
                    hireDate = input('Masukkan hire date (dd-mm-yyy) : ')
                    
                    while True:
                        checker  = input('Apakah Data akan disimpan? (Y/N) : ').upper()
                        if (checker == 'Y') or (checker == 'N'):
                            break

                    if checker == 'Y':
                        myList.append({
                            'Id'            : addId,
                            'Birth_date'    : birthDate,
                            'Name'          : namaKaryawan, 
                            'Gender'        : genderKaryawan, 
                            'Hire_date'     : hireDate
                            })
                        print('Data Sudah Tersimpan')
                        continue
                    elif checker == 'N':
                        print('Data Tidak Tersimpan')
                        continue

        elif create == '2':
            break

# Update Data
def update_Data():
    while True:
        print('''=======Mengubah Data Karyawan=======\n
        1. Ubah Data Karyawan
        2. Kembali ke Menu Utama
        ''')
        update = input("Silahkan Pilih Sub Menu Create Data [1-2]: ")
        if update == '1':
            addId = input("Masukkan Id: ")
            for j, i in enumerate(myList):
                if i ['Id'] == addId:
                    print('   Id\t| Birth_date| \tName\t| Gender | Hire_date')
                    print(f"{j+1}. {i['Id']}\t| {i['Birth_date']}| {i['Name']}\t|   {i['Gender']}\t | {i['Hire_date']}")

                    while True:
                        checker = input('Tekan Y jika ingin lanjut update data atau N jika ingin cancel update (Y/N): ').upper()
                        if checker == 'Y' or checker == 'N':
                            break
                    
                    if checker == 'Y':
                        addValue = input('Masukkan kolom/keterangan yg ingin di edit: ').capitalize()
                        newValue = input(f'Masukkan {addValue} baru: ')

                        while True :
                            checker1 = input('Apakah data akan diupdate? (Y/N): ').upper()
                            if checker1 == 'Y' or checker1 == 'N':
                                if checker1 == 'Y':
                                    myList[j][addValue] = newValue
                                    print('Data Updated')
                                    break
                                elif checker1 == 'N':
                                    print('Data Tidak Terupdate')
                                    break
                                break
                    elif checker == 'N':
                        print('Data Tidak Terupdate')
                        break

                    break
            else:
                print('Data Tidak Ada')
                continue

        elif update == '2':
            break

# Delete Data
def delete_Data():
    while True:
        print('''=======Menghapus Data Karyawan=======\n
        1. Hapus Data Karyawan
        2. Kembali ke Menu Utama
        ''')
        inpt = input("Silahkan Pilih Sub Menu Create Data [1-2]: ")
        if inpt == '1':
            addId = input("Masukkan Id: ")
            for j, i in enumerate(myList):
                if i ['Id'] == addId:
                    while True :
                        checker = input('Apakah data akan dihapus? (Y/N): ').upper()
                        if checker == 'Y' or checker == 'N':
                            if checker == 'Y':
                                del myList[j]
                                print('Data Deleted')
                                break
                            elif checker == 'N':
                                print('Data Tidak Terhapus')
                                break
                    break
            else:
                print('Data Tidak Ada')
                continue
        
        elif inpt == '2':
            break

while True :
    pilihanMenu = input('''
=====Selamat Datang di Database Karyawan=====\n
List Menu:\n
    1. Report Data Karayawan
    2. Menambahkan Data Karyawan
    3. Mengubah Data Karyawan
    4. Menghapus Data Karyawan
    5. Exit\n
Masukkan angka Menu yang ingin dijalankan [1-5]: ''')

    if (pilihanMenu == '1') :
        read_Data()
    elif(pilihanMenu == '2') :
        create_Data()
    elif(pilihanMenu == '3') :
        update_Data()
    elif(pilihanMenu == '4') :
        delete_Data()
    elif(pilihanMenu == '5') :
        print('See you later!')
        break
    else:
        print('Pilihan yang anda masukkan salah')


        


            

       
            
                