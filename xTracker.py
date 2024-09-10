# xTracker v0.2
# expense tracker

# Update Log
# v0.1 : 01-11-2022 # Analisis dari data satu hari
# v0.2 : 04-11-2022 # data 14 hari dan fitur nama
# v0.3 : 06-11-2022 # Analisis harian, input hari dapat ditambah
# v0.4 : 07-11-2022 # Analisis mingguan
# v0.5 : 08-11-2022 # bug fixes
# v1.1 : 08-11-2022 # tampilan reworked
# v1.2 : 08-11-2022 # penambahan kamus pada program
# v1.5 : 08-11-2022 # bug fixes
# v2.0 : 08-11-2022 # navigation reworked


# Kamus
# b3, menu4, menu5, nama, s3, s6, s7, sampCat, t3, t6, t7 : string
# d, g, h, i, j, m4, menu1, menu2, menu3, menu6, menu7, n, n4, n6, n7, totCategory, totUser, totWeek, w, wk, x : integer
# loop1, loop2, loop3, loop4, loop5, loop6, loop7, menu2Ana, wBack : boolean
# username : array [0..totUser - 1] of string
# category : array [0..totCategory - 1] of string
# hari, llharill : array [0..6] of string
# sampi : array of integer
# data, AnaWeek : matrix of float/integer


# Algoritma
username = ['achmad', 'habibie', 'krasochnyy', 'ahmad', 'hashigawa','marjan','axmad', 'hiroshima', 'charles', 'kama', 'romanee-konti']
category = ['makan', 'minum', 'parkir', 'bensin']
totUser = 11
totCategory = 4
totWeek = 1

data = [[[[0 for i in range(totCategory)], 0] for i in range(totUser)] for i in range(7*totWeek)]

#data[hari][nama][]
data[1][0][0] = [16, 0, 4, 0]
data[1][0][1] = 20
data[0][0][0] = [18, 3, 2, 0]
data[0][0][1] = 23

AnaWeek = [[[[0 for i in range(totCategory)], 0] for i in range(totUser)] for i in range(totWeek)]

hari = ['Ahad', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu']
llharill = ['==Ahad', '=Senin', 'Selasa', '==Rabu', '=Kamis', '=Jumat', '=Sabtu']

def inputChiffre(x, str): # fungsi mengintegerkan angka apabila inputnya bilangan bulat
    # Kamus lokal
    # x : float/integer
    # str : string 
    x = float(input(str))
    if x == int(x):
        x = int(x)
    return x

def pourcentage(x, tot): # fungsi mencari persentase dari suatu data
    # Kamus lokal
    # x, tot : integer/float
    if tot != 0: # pembilang /= 0
        x = (10000 * x//tot + 5) //10 /10
        if x == int(x): # x = bilangan bulat
            x = int(x)
        return x
    else: # tot == 0: mereturn 0 apabila pembilangnya 0
        return 0

def indicateur(a, b, i): # fungsi mengecek apakah suatu data nilainya naik/turun dari data sebelumnya
    # Kamus lokal
    # a, b : integer/float
    # i : integer
    if i > 0 and a > b and a != 0 and b != 0:
        return " ^"
    elif i > 0 and a < b and a != 0 and b != 0:
        return " ˅"
    else:
        return ""

loop1 = True
while loop1 == True:
    print("=========Expense Tracker xTracker v1.0========")
    print("Menu: ")
    print("1. Mulai")
    print("0. Matikan program")
    menu1 = int(input())
    print()

    if menu1 == 1: # mulai
        wBack = True
        nama = str(input("Masukkan nama: "))
        if nama not in username: # mengecek apakah nama ada di list
            wBack = False
            username.append(nama)
            totUser += 1
            for i in range(7*totWeek):
                data[i].append(0)
                data[i][totUser-1] = [[0 for j in range(totCategory)], 0]
            for i in range(totWeek):
                AnaWeek[i].append(0)
                AnaWeek[i][totUser-1] = [[0 for j in range(totCategory)], 0]

        for i in range(totUser):
            if username[i] == nama:
                n = i
        print()
        loop2 = True
        while loop2 == True:
            menu2Ana = False
            for i in range(7*totWeek):
                if data[i][n][1] != 0:
                    menu2Ana = True
            if wBack == True:
                print("============Selamat datang kembali============")
            else:
                print("================Selamat datang================")
            print(f"Halo, {nama}! Silahkan pilih menu:")
            print("1. Input pengeluaran")
            if menu2Ana == True: # analisis
                print("2. Analisis harian")
                print("3. Analisis mingguan")
            print("0. <- (Keluar akun)")
            menu2 = int(input())
            print()

            if menu2 == 1: # input pengeluaran
                wk = 0
                loop3 = True
                while loop3 == True:
                    b3 = ""
                    if wk < 4:
                        print("==============Input Pengeluaran===============")
                        print(f"Pilih hari pada minggu ke-{wk%4+1} yang akan diinput:")
                    else:
                        print("====================================Input Pengeluaran=====================================")
                        print(f"Pilih hari pada minggu ke-{wk%4+1} bulan ke-{wk//4+1} (Asumsikan 1 bulan = 4 minggu) yang akan diinput:")
                    print(f"1. Ahad,   expense tot: {data[0+7*wk][n][1]}")
                    print(f"2. Senin,  expense tot: {data[1+7*wk][n][1]}")
                    print(f"3. Selasa, expense tot: {data[2+7*wk][n][1]}")
                    print(f"4. Rabu,   expense tot: {data[3+7*wk][n][1]}")
                    print(f"5. Kamis,  expense tot: {data[4+7*wk][n][1]}")
                    print(f"6. Jumat,  expense tot: {data[5+7*wk][n][1]}")
                    print(f"7. Sabtu,  expense tot: {data[6+7*wk][n][1]}")
                    print(f"8. > (Minggu selanjutnya)")
                    print(f"9. -> (Loncat ke minggu yang ke- )")
                    s3, t3 = "<", ""
                    if wk > 0: # minggu sebelumnya
                        print("10. < (Minggu sebelumnya)")
                        s3, t3 = "#", " ke menu awal"
                    if wk > 1: # minggu pertama
                        print("11. << (Minggu pertama)")
                    print(f"0. {s3} (Kembali{t3})")
                    menu3 = int(input())
                    print()

                    if menu3 > 0 and menu3 < 8: # hari Ahad-Sabtu
                        loop4 = True
                        while loop4 == True:
                            print("==============Input Pengeluaran===============")
                            if wk < 4:
                                print(f"Pengeluaran pada {hari[(menu3-1)%7]}, minggu ke-{wk+1}: {data[menu3-1+7*wk][n][1]}")
                            else:
                                print(f"Pengeluaran pada {hari[(menu3-1)%7]}, minggu ke-{wk+1} : {data[menu3-1+7*wk][n][1]}")
                            print("Input per kategori:")

                            n4 = 1
                            sampi = []
                            if data[menu3-1+7*wk][n][0] != [0 for i in range(totCategory)]: # list kategori yg sudah diinput
                                for i in range(totCategory):
                                    if data[menu3-1+7*wk][n][0][i] != 0:
                                        print(f"{n4}. {category[i]}: {data[menu3-1+7*wk][n][0][i]}")
                                        n4 += 1
                                        sampi.append(i)

                            print(f"{n4}. Tambahkan kategori: ")
                            m4 = n4

                            print("Rekomendasi kategori:")
                            i, j = 0, 0
                            while j < 3 and i < totCategory: # list 0-3 rekomendasi kategori
                                if data[menu3-1+7*wk][n][0][i] == 0:
                                    n4 += 1
                                    print(f"{n4}. {category[i]}")
                                    sampi.append(i)
                                    j += 1
                                i += 1
                            
                            print("0. < (Kembali)")
                            print("00. # (Kembali ke menu awal)")
                            menu4 = str(input())
                            print()
                                
                            if int(menu4) > 0 and int(menu4) < n4+1: # pilihan kategori
                                menu4 = int(menu4)
                                if menu4 == m4: # tambahkan kategori
                                    sampCat = str(input("Tambahkan kategori: "))
                                    if sampCat not in category:
                                        category.append(sampCat)
                                        totCategory += 1
                                        for j in range(totUser):
                                            for i in range(7*totWeek):
                                                data[i][j][0].append(0)
                                            for i in range(totWeek):
                                                AnaWeek[i][j][0].append(0)
                                    for i in range(totCategory):
                                        if sampCat == category[i]:
                                            x = i
                                
                                elif int(menu4) < m4: # list kategori yg sudah diinput
                                    x = sampi[menu4-1]

                                else: # menu4 > m4: list 0-3 kategori yg direkomendasikan
                                    x = sampi[menu4-2]
                                
                                if data[menu3-1+7*wk][n][0][x] != 0: # kategori sudah ada nilai
                                    loop5 = True
                                    while loop5 == True:
                                        print("==============Input Pengeluaran===============")
                                        print(f"Kategori {category[x]}: {data[menu3-1+7*wk][n][0][x]}")
                                        print("1. Tambahkan")
                                        print("2. Ubah nilai")
                                        print("3. Hapus kategori")
                                        print("0. < (Kembali)")
                                        print("00. # (Kembali ke menu awal)")
                                        menu5 = str(input())
                                        print()

                                        if menu5 == "1": # tambahkan
                                            data[menu3-1+7*wk][n][1] -= data[menu3-1+7*wk][n][0][x]
                                            data[menu3-1+7*wk][n][0][x] += inputChiffre(data[menu3-1+7*wk][n][0][x], f"nilai {data[menu3-1+7*wk][n][0][x]} ditambahkan dengan: ")
                                            data[menu3-1+7*wk][n][1] += data[menu3-1+7*wk][n][0][x]
                                            print()
                                            loop5 = False
                                        
                                        elif menu5 == "2": # ubah nilai
                                            data[menu3-1+7*wk][n][1] -= data[menu3-1+7*wk][n][0][x]
                                            data[menu3-1+7*wk][n][0][x] = inputChiffre(data[menu3-1][n][0][x], f"nilai {data[menu3-1+7*wk][n][0][x]} diubah menjadi: ")
                                            data[menu3-1+7*wk][n][1] += data[menu3-1+7*wk][n][0][x]
                                            print()
                                            loop5 = False
                                        
                                        elif menu5 == "3": # hapus kategori
                                            data[menu3-1+7*wk][n][1] -= data[menu3-1+7*wk][n][0][x]
                                            data[menu3-1+7*wk][n][0][x] = 0
                                            loop5 = False

                                        elif menu5 == "0": # kembali
                                            loop5 = False

                                        elif menu5 == "00": # kembali ke menu awal
                                            loop3, loop4, loop5 = False, False, False
                                
                                else: # kategori belum ada nilai
                                    data[menu3-1+7*wk][n][0][x] = inputChiffre(data[menu3-1+7*wk][n][0][x], f"Total pengeluaran pada kategori {category[x]}: ")
                                    data[menu3-1+7*wk][n][1] += data[menu3-1+7*wk][n][0][x]
                                    print()
                            
                            elif menu4 == "0": # kembali
                                loop4 = False

                            elif menu4 == "00": # kembali ke menu awal
                                loop3, loop4 = False, False

                    elif menu3 == 10 and wk > 0: # minggu sebelumnya
                        wk -= 1
                    
                    elif menu3 == 11 and wk > 1: # minggu pertama
                        wk = 0

                    elif menu3 == 8: # minggu selanjutnya
                        wk += 1
                        if totWeek < wk+1:
                            data.extend([0 for i in range(7)])
                            for i in range(7):
                                data[i+7*totWeek] = [[[0 for i in range(totCategory)], 0] for i in range(totUser)]
                            AnaWeek.extend([0])
                            AnaWeek[totWeek] = [[[0 for i in range(totCategory)], 0] for i in range(totUser)]
                            totWeek += 1

                    elif menu3 == 9: # loncat ke minggu yang ke-
                        wk = int(input("Loncat ke minggu yang ke-"))-1
                        while totWeek < wk+1:
                            data.extend([0 for i in range(7)])
                            for i in range(7):
                                data[i+7*totWeek] = [[[0 for i in range(totCategory)], 0] for i in range(totUser)]
                            AnaWeek.extend([0])
                            AnaWeek[totWeek] = [[[0 for i in range(totCategory)], 0] for i in range(totUser)]
                            totWeek += 1
                        print()

                    elif menu3 == 0: # kembali
                        loop3 = False

            elif menu2 == 2 and menu2Ana == True: # analisis harian
                h = 0
                loop6 = True
                while loop6 == True:
                    print("===============Analisis Harian================")
                    n6 = 1
                    for i in range(totCategory):
                        if data[h][n][0][i] != 0:
                            print(f"  {n6}. {category[i]}: {data[h][n][0][i]}{indicateur(data[h][n][0][i], data[h-1][n][0][i], h)} ({pourcentage(data[h][n][0][i], data[h][n][1])}%{indicateur(pourcentage(data[h][n][0][i], data[h][n][1]), pourcentage(data[h-1][n][0][i], data[h-1][n][1]), h)})")
                            n6 += 1
                    print(f"  Total pengeluaran: {data[h][n][1]}{indicateur(data[h][n][1], data[h-1][n][1], h)}")
                    if h < 28:
                        print(f"============={llharill[h%7]}, Minggu ke-{h//7+1}==============")
                    else:
                        print(f"========{llharill[h%7]}, Minggu ke-{h//7+1}, Bulan ke-{h//28+1}========")

                    print("Menu:")
                    n6, s6, t6 = 1, "<", ""
                    if h+1 < 7*totWeek: # hari selanjutnya
                        print(f"{n6}. > (Hari selanjutnya)")
                        n6 += 1
                    print(f"{n6}. -> (Loncat ke hari yang ke- )")
                    n6 += 1
                    if h > 0: # hari sebelumnya
                        print(f"{n6}. < (Hari sebelumnya)")
                        s6, t6 = "#", " ke menu awal"
                    if h > 1: # hari pertama
                        print(f"{n6+1}. << (Hari pertama)")
                    print(f"0. {s6} (Kembali{t6})")
                    menu6 = int(input())
                    print()

                    if menu6 == n6 and h > 0: # hari sebelumnya
                        h -= 1

                    elif menu6 == n6+1 and h > 1: # hari pertama
                        h = 0

                    elif menu6 == 1 and h+1 < 7*totWeek: # hari selanjutnya
                        h += 1

                    elif menu6 == n6-1: # loncat ke hari yang ke-
                        g = int(input("Loncat ke hari yang ke-")) - 1
                        if g >= 0 and g < 7*totWeek:
                            h = g
                        elif g >= 7*totWeek:
                            print("Data tidak ditemukan")
                            print(f"Silahkan input data pada minggu ke-{g//7+1} terlebih dahulu atau loncat ke hari <= {7*totWeek}")
                        else:
                            print(f"Tidak dapat menganalisis data pada hari ke negatif{g*-1}")
                        print()

                    elif menu6 == 0: # kembali
                        loop6 = False

            elif menu2 == 3 and menu2Ana == True: # analisis mingguan
                w = 0
                loop7 = True
                while loop7 == True:
                    AnaWeek[w][n][1] = 0
                    for i in range(totCategory):
                        AnaWeek[w][n][0][i] = 0
                        for d in range(7):
                            AnaWeek[w][n][0][i] +=  data[7*w+d][n][0][i]
                        AnaWeek[w][n][1] += AnaWeek[w][n][0][i]
                    print("==============Analisis Mingguan===============")
                    n7 = 1
                    for i in range(totCategory):
                        if AnaWeek[w][n][0][i] != 0:
                            print(f"  {n7}. {category[i]}: {AnaWeek[w][n][0][i]}{indicateur(AnaWeek[w][n][0][i], AnaWeek[w-1][n][0][i], w)} ({pourcentage(AnaWeek[w][n][0][i], AnaWeek[w][n][1])}%{indicateur(pourcentage(AnaWeek[w][n][0][i], AnaWeek[w][n][1]), pourcentage(AnaWeek[w-1][n][0][i], AnaWeek[w-1][n][1]), w)})")
                            n7 += 1
                    print(f"  Total pengeluaran: {AnaWeek[w][n][1]}{indicateur(AnaWeek[w][n][1], AnaWeek[w-1][n][1], w)}")
                    if w < 4:
                        print(f"=================Minggu ke-{w+1}==================")
                    else:   
                        print(f"============Minggu ke-{w%4+1}, Bulan ke-{w//4+1}===========")

                    print("Menu:")
                    n7, s7, t7 = 1, "<", ""
                    if w+1 < totWeek: # minggu selanjutnya
                        print(f"{n7}. > (Minggu selanjutnya)")
                        n7 += 1
                    if totWeek > 2: # loncat ke minggu yang ke-
                        print(f"{n7}. -> (Loncat ke minggu yang ke- )")
                        n7 += 1
                    if w > 0: # minggu sebelumnya
                        print(f"{n7}. < (Minggu sebelumnya)")
                        s7, t7 = "#", " ke menu awal"
                    if w > 1: # minggu pertama
                        print(f"{n7+1}. << (Minggu pertama")
                    print(f"0. {s7} (Kembali{t7})")
                    menu7 = int(input())
                    print()

                    if menu7 == n7 and w > 0: # minggu sebelumnya
                        w -= 1

                    elif menu7 == n7+1 and w > 1: # minggu pertama
                        w = 0

                    elif menu7 == 1 and w+1 < totWeek: # minggu selanjutnya
                        w += 1

                    elif menu7 == n7-1 and totWeek > 2: # loncat ke minggu yang ke:
                        g = int(input("Loncat ke minggu yang ke-")) - 1
                        if g > 0 and g < totWeek:
                            w = g
                        elif g >= totWeek:
                            print("Data tidak ditemukan")
                            print(f"Silahkan input data pada minggu ke-{g+1} terlebih dahulu atau loncat ke minggu < {totWeek}")
                        else:
                            print(f"Tidak dapat menganalisis data pada minggu ke negatif{g*-1}")
                        print()

                    elif menu7 == 0: # kembali
                        loop7 = False

            elif menu2 == 0: # keluar akun
                loop2 = False
    
    elif menu1 == 0: # matikan program
        loop1 = False
        print("=================Terima kasih=================")
        print("Terima kasih sudah menggunakan program kami :)")
        print("==============================================")