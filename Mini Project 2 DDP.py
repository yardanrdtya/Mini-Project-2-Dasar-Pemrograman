from prettytable import PrettyTable
import os
import sys
os.system ("cls")

# Tabel profil diri
table = PrettyTable()
table.field_names = ["NAMA", "NIM", "PROGRAM"]
table.add_row(["Yardan Raditya Rafi' Widyadhana", "2409116037", "Sistem Pendaftaran Webinar Online"])
print(table)

table = PrettyTable()
table.field_names = ["No Webinar", "Daftar Webinar", "Tanggal Webinar", "Waktu Webinar"]

# Fungsi menambahkan webinar ke daftar
def tambah_webinar(no_webinar, daftar_webinar, tanggal_webinar, waktu_webinar):
    table.add_row([no_webinar, daftar_webinar, tanggal_webinar, waktu_webinar])

# Database webinar
tambah_webinar("1", "Artificial Intelligence (AI) dan Machine Learning", "Kamis, 17 Oktober 2024", "14.00 - 16.00 WITA")
tambah_webinar("2", "Keamanan Jaringan: Membangun Infrastruktur yang Aman", "Kamis, 24 Oktober 2024", "14.00 - 16.00 WITA")
tambah_webinar("3", "Cloud Computing: Infrastruktur IT di Era Digital", "Kamis, 31 Oktober 2024", "14.00 - 16.00 WITA")
tambah_webinar("4", "Full Stack Development: Keterampilan Utama Pengembang Web Modern", "Kamis, 7 November 2024", "14.00 - 16.00 WITA")
tambah_webinar("5", "Mobile Application Development: Membangun Aplikasi Android dan iOS", "Kamis, 14 November 2024", "14.00 - 16.00 WITA")
tambah_webinar("6", "User Experience (UX) dan User Interface (UI) Design", "Kamis, 21 November 2024", "14.00 - 16.00 WITA")
tambah_webinar("7", "Data Science dan Big Data: Menemukan Nilai dari Data", "Kamis, 28 November 2024", "14.00 - 16.00 WITA")

# Menerapkan program login admin atau user
def login():
    while True:
        print("--------------------------------------------")
        print("Silahkan pilih mode login")
        print("--------------------------------------------")
        print("[1]. Admin")
        print("[2]. Peserta")
        pilihan = input("Masukkan pilihan (1 atau 2) : ")
        if pilihan == "1":
            admin()
        elif pilihan == "2":
            peserta()
            break
        else:
            print("Mode login tidak ada, silahkan coba lagi")
            return login()

# Login mode admin
def admin():
    while True:
        print("--------------------------------------------")
        print("Anda login sebagai Admin")
        print("--------------------------------------------")
        print("[1]. Tambah Webinar")
        print("[2]. Lihat Daftar Webinar")
        print("[3]. Update Webinar")
        print("[4]. Delete Webinar")
        print("[5]. Keluar/Kembali ke Mode Login")
        operasi = input("Silahkan pilih operasi yang diinginkan : ")
        if operasi == "1":
            tambah_webinar_admin()
        elif operasi == "2":
            lihat_webinar()
        elif operasi == "3":
            update_webinar()
        elif operasi == "4":
            delete_webinar()
        elif operasi == "5":
            mode_login = input("Apakah anda ingin keluar atau kembali ke mode login? (Keluar/Kembali) : ")
            if mode_login == "Keluar":
                print("---------------------------------------------------------------------------------")
                print("Baiklah, terimakasih sudah menggunakan program ini")
                print("---------------------------------------------------------------------------------")
                sys.exit()
            elif mode_login == "Kembali":
                login()
        else:
            print("Input tidak valid, silahkan coba lagi")

# Role admin menambah jadwal webinar
def tambah_webinar_admin():
    while True:
        no_webinar = input("Masukkan nomor webinar : ")
        daftar_webinar = input("Masukkan daftar webinar : ")
        tanggal_webinar = input("Masukkan tanggal webinar : ")
        waktu_webinar = input("Masukkan waktu webinar : ")
        tambah_webinar(no_webinar, daftar_webinar, tanggal_webinar, waktu_webinar)
        print("---------------------------------------------")
        print("Konfirmasi Penambahan Jadwal Webinar")
        print("---------------------------------------------")
        print(f"Nomor Webinar : {no_webinar}")
        print(f"Webinar       : {daftar_webinar}")
        print(f"Hari/Tanggal  : {tanggal_webinar}")
        print(f"Pukul         : {waktu_webinar}")
        print("-----------------------------------------------------")
        print("Jadwal webinar telah berhasil ditambahkan!")
        print("-----------------------------------------------------")
        pilihan = input("Apakah anda ingin menambahkan jadwal webinar lagi? (ya/tidak) : ")
        if pilihan == "ya":
            tambah_webinar_admin()
        elif pilihan == "tidak":
            break

# Role admin melihat daftar webinar
def lihat_webinar():
    print(table)

# Role admin memperbarui jadwal webinar
def update_webinar():
    lihat_webinar()
    no_webinar = input("Masukkan nomor webinar yang ingin diubah : ")
    update_jadwal_webinar = input("Silahkan pilih yang ingin diubah (tanggal/waktu) : ")
    jadwal_baru = input(f"Masukkan {update_jadwal_webinar} baru : ")

    for row in table._rows:
        if row[0] == no_webinar:
            index = table._rows.index(row)
            if update_jadwal_webinar == "tanggal":
                table._rows[index][2] = jadwal_baru
            elif update_jadwal_webinar == "waktu":
                table._rows[index][3] = (jadwal_baru)
            else:
                print("Data tidak valid")
                return update_webinar()
    print("---------------------------------------------")
    print("Konfirmasi Perubahan Jadwal Webinar")
    print("---------------------------------------------")
    print(f"Nomor Webinar : {no_webinar}")
    print(f"Tanggal/Waktu : {jadwal_baru}")
    print("-----------------------------------------------------")
    print("Perubahan jadwal webinar telah berhasil!")
    print("-----------------------------------------------------")

# Role admin menghapus jadwal webinar
def delete_webinar():
    while True:
        lihat_webinar()
        no_webinar = input("Masukkan nomor webinar yang ingin dihapus : ")
        
        for row in table._rows:
            if row [0] == no_webinar:
                table.del_row(table.rows.index(row))
        print("-------------------------------------------------------")
        print(f"Jadwal webinar dengan nomor {no_webinar} telah dihapus")
        print("-------------------------------------------------------")   
        pilihan = input("Apakah anda ingin menghapus jadwal webinar lagi? (ya/tidak) : ")
        if pilihan == "ya":
            delete_webinar()
        elif pilihan == "tidak":
            break

# Login mode peserta
def peserta():
    while True:
        print("--------------------------------------------")
        print("Anda login sebagai Peserta")
        print("--------------------------------------------")
        print("[1]. Lihat Daftar Webinar")
        print("[2]. Daftar Webinar")
        print("[3]. Keluar/Kembali ke Mode Login")
        pilihan = input("Masukkan pilihan : ")
        if pilihan == "1":
            lihat_webinar()
        elif pilihan == "2":
            daftar_webinar()
        elif pilihan == "3":
            mode_login = input("Apakah anda ingin keluar atau kembali ke mode login? (Keluar/Kembali) : ")
            if mode_login == "Keluar":
                print("---------------------------------------------------------------------------------")
                print("Baiklah, terimakasih sudah menggunakan program ini")
                print("---------------------------------------------------------------------------------")
                sys.exit()
            elif mode_login == "Kembali":
                login()
            else:
                print("Input tidak valid, silahkan coba lagi")

# Role peserta mendaftar webinar
def daftar_webinar():
    while True:
        lihat_webinar()
        while True:
            nama_peserta = input("Masukkan nama peserta : ")
            email_peserta = input("Masukkan email peserta : ")
            nomor_telepon = input("Masukkan nomor telepon peserta : ")
            no_webinar = input("Masukkan nomor webinar yang ingin diikuti : ")

            found = False
            for row in table._rows:
                if row[0] == no_webinar:
                    found = True
                    print("--------------------------------------------")
                    print("Konfirmasi Pendaftaran")
                    print("--------------------------------------------")
                    print(f"Nama          : {nama_peserta}")
                    print(f"Email         : {email_peserta}")
                    print(f"Nomor Telepon : {nomor_telepon}")
                    print(f"Webinar       : {row[1]}")
                    print("----------------------------------------------------------------------------------")
                    print("Pendaftaran webinar anda telah berhasil!")
                    print("----------------------------------------------------------------------------------")
                    sys.exit()
            if not found:
                print("Input tidak valid, jadwal webinar dengan nomor tersebut tidak ada. Silahkan coba lagi")

# Memulai program dengan login
login()