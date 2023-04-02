import os
import pwinput as pw
from quest import *
# import getpass as gp

def login():
    username = input("Masukan username: ")
    password = pw.pwinput("Masukan password: ", mask="*")
    with open("user_details.txt", "r") as cek:
        for line in cek:
            data = line.strip().split(",")
            if username == data[0] and password == data[1]:
                print("Login Berhasil!")
                return
    print("Username / Password Salah!")

def register():
    while True:
        username = input("Masukan username: ")
        if not os.path.exists("user_details.txt"):
            break
        with open("user_details.txt", "r") as cek:
            for line in cek:
                data = line.strip().split(",")
                if username == data[0]:
                    print("Username sudah ada!")
                    break
            else:
                break

    while True:
        password = pw.pwinput("Masukan password: ", mask="*")
        confirm_password = pw.pwinput("Konfirmasi Password: ", mask="*")
        if password == confirm_password:
            break
        else:
            print("Password salah! Coba lagi")

    with open("user_details.txt", "a") as cek:
        cek.write(f"{username},{password}\n")
    print("User berhasil dibuat!")

def main():
    while True:
        print(" --- MENU --- ")
        print("1. Sign up\n2. Login\n0. Exit")
        pilihan = int(input("Masukan pilihan: "))
        if pilihan == 1:
            register()
            break
        elif pilihan == 2:
            login()
            question()
            break
        elif pilihan == 0:
            exit()
        else:
            print("Pilihan / Menu tidak ada!")

if __name__ == "__main__":
    while(True):
        main()
        print("\n\nLanjut?\n1. Ya\n2. Tidak")
        pilihan = int(input("Masukan pilihan : "))
        if pilihan == 2:
            break
    print("Terima Kasih!")