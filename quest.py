from data import *
from wifi import *
import os

# question
k1 = 'Apakah kamu membutuhkan internet?'
k2 = 'Apakah kamu berlokasi di perkotaan?'
k3 = 'Apakah kamu berada di pulau jawa?'
k4 = 'Apakah kamu berada di jabodetabek?'
k5 = 'Apakah dilokasi kamu tersedia jaringan 4G?'
k6 = 'Apakah kamu menggunakan internet hanya di satu lokasi?'
k7 = 'Apakah kamu menggunakan internet untuk suatu instansi?'
k8 = 'Apakah kamu menggunakan untuk menonton tayangan Drama / Olahraga / Film?'
k9 = 'Apakah kamu akan menggunakan untuk bermain game?'
k10 = 'Apakah kamu bersedia untuk mengeluarkan dana lebih untuk ini?'
k11 = 'Apakah pengguna sekitar ada yang memakai wifi?'
k12 = 'Apakah kamu membutuhkan internet yang skala besar?'
k13 = 'Apakah kamu menggunakan dalam jangka waktu lama?'
k14 = 'Apakah kamu menggunakan untuk menonton tayangan Televisi?'




def question():
  os.system('cls' if os.name == 'nt' else 'clear')
  print("Selamat datang di Pertanyaan Tree")
  print("Silahkan jawab pertanyaan berikut dengan jawaban 'y' atau 'n' \n y = ya \n n = tidak")
# -------------------------------------------------------------------
  #q1
  print(k1)
  q1 = input("Jawab: ").lower()
  if q1 == "y":
      #q2
    print(k2)
    q2 = input("Jawab: ").lower()
    if q2 == "y":
      #q3
      print(k3)
      q3 = input("Jawab: ").lower()
      if q3 == "y":
        #q4
        print(k4)
        q4 = input("Jawab: ").lower()
        if q4 == "y":
          #q5
          print(k5)
          q5 = input("Jawab: ").lower()
          if q5 == "y":
            #q6
            print(k6)
            q6 = input("Jawab: ").lower()
            if q6 == "y":
              #q7
              print(k7)
              q7 = input("Jawab: ").lower()
              if q7 == "y":
                print(biznet())
                print(cbn())
                print("\nRekomendasi WiFi: ")
                print("CBN\t\t: 100Mbps : Rp.799.000")
                print("Biznet\t\t: 200Mbps : Rp.575.000")
              elif q7 == "n":
                #q8
                print(k8)
                q8 = input("Jawab: ").lower()
                if q8 == "y":
                  print(firstMedia())
                  print(indihome())
                  print(biznet())
                  print(xl())
                  print(smartfren())
                  print("\nRekomendasi WiFi / Paket data: ")
                  print("First media / Indihome / Biznet / XL / Smartfren")
                elif q8 == "n":
                  #q9
                  print(k9)
                  q9 = input("jawab: ").lower()
                  if q9 == "y":
                    print(biznet())
                    print(myRepublic())
                    print(telkomsel())
                    print(xl())
                    print("\nRekomendasi Biznet / My Republic / Telkomsel / XL")
                    print("\nRekomendasi WiFi: ")
                    print("Biznet\t\t: 250Mbps : Rp.700.000 (Gamers)")
                  elif q9 == "n":
                    print(indihome())
                    print(oxygen())
                    print(indosat())
                    print(tri())
                    print("\nRekomendasi Indihome / Oxygen / Indosat / Tri")
            elif q6 == "n":
              print("k8")
              q8 = input("Jawab: ").lower()
              if q8 == "y":
                print(xl())
                print(axis())
                print(tri())
                print("\nRekomendasi XL / Axis / Tri")
              elif q8 == "n":
                print (k9)
                q9 = input("Jawab: ").lower()
                if q9 == "y":
                  print(xl())
                  print(axis())
                  print(smartfren())
                  print("\nRekomendasi XL / Axis / Smartfren")
                elif q9 == "n":
                  print(telkomsel())
                  print(indosat())
                  print(xl())
                  print("\nRekomendasi Telkomsel / Indosat / XL")
          elif q5 == "n":
            print(k10)
            q10 = input("Jawab: ").lower()
            if q10 == "y":
              print(k11)
              q11 = input("Jawab: ").lower()
              if q11 == "y":
                print(k12)
                q12 = input("Jawab: ").lower()
                if q12 == "y":
                  print(k13)
                  q13 = input("Jawab: ").lower()
                  if q13 == "y":
                    print(k14)
                    q14 = input("Jawab: ").lower()
                    if q14 == "y":
                      print(indihome())
                      print("\nRekomendasi Indihome")
                    elif q14 == "n":
                      print(vsat())
                      print("\nRekomendasi Vsat atau Data yang tersedia pada daerah anda")
                  elif q13 == "n":
                    print(k14)
                    q14 = input("Jawab: ").lower()
                    if q14 == "y":
                      print(indihome())
                      print("\nRekomendasi Indihome")
                    elif q14 == "n":
                      print(vsat())
                      print("Rekomendasi Vsat atau Data yang tersedia pada daerah anda")
                elif q12 == "n":
                  print(k13)
                  q13 = input("Jawab: ").lower()
                  if q13 == "y":
                    print(k14)
                    q14 = input("Jawab: ").lower()
                    if q14 == "y":
                      print(indihome())
                      print("\nRekomendasi Indihome")
                    elif q14 == "n":
                      print(vsat())
                      print("\nRekomendasi Vsat atau Data yang tersedia pada daerah anda")
                  elif q13 == "n":
                    print(k14)
                    q14 = input("Jawab: ").lower()
                    if q14 == "y":
                      print(indihome())
                      print("\nRekomendasi Indihome")
                    elif q14 == "n":
                      print(vsat())
                      print("\nRekomendasi Vsat atau Data yang tersedia pada daerah anda")
              elif q11 == "n":
                print(k13)
                q13 = input("Jawab: ").lower()
                if q13 == "y":
                  print(vsat())
                  print("\nRekomendasi Vsat")
                elif q13 == "n":
                  print(telkomsel())
                  print("\nRekomendasi Telkomsel")
            elif q10 == "n":
              print(k11)
              q11 = input("Jawab: ").lower()
              if q11 == "y":
                print(k12)
                q12 = input("Jawab: ").lower()
                if q12 == "y":
                  print(k13)
                  q13 = input("Jawab: ").lower()
                  if q13 == "y":
                    print(indihome())
                    print("\nRekomendasi Indihome")
                  elif q13 == "n":
                    print("Rekomendasi Telkomsel")
                elif q12 == "n":
                  print(telkomsel())
                  print("\nRekomendasi Telkomsel")
              elif q11 == "n":
                print(telkomsel())
                print("\nRekomendasi Telkomsel")
        elif q4 == "n":
          print(k5)
          q5 = input("Jawab: ").lower()
          if q5 == "y":
            print(k6)
            q6 = input("Jawab: ").lower()
            if q6 == "y":
              print(k7)
              q7 = input("Jawab: ").lower()
              if q7 == "y":
                print(cbn())
                print(biznet())
                print(indihome())
                print("\nRekomendasi CBN / Biznet / Indihome")
              elif q7 == "n":
                print(k8)
                q8 = input("Jawab: ").lower()
                if q8 == "y":
                  print(indihome())
                  print(firstMedia())
                  print("\nRekomendasi Indihome / First Media")
                elif q8 == "n":
                  print(k9)
                  q9 = input("Jawab: ").lower()
                  if q9 == "y":
                    print(biznet())
                    print(myRepublic())
                    print(indihome())
                    print("\nRekomendasi Biznet / My Republic / Indihome")
                  elif q9 == "n":
                    print(indihome())
                    print("\nRekomendasi Indihome")
            elif q6 == "n":
              print(k8)
              q8 = input("Jawab: ").lower()
              if q8 == "y":
                print(indihome())
                print(firstMedia())
                print(telkomsel())
                print(xl())
                print("\nRekomendasi Telkomsel / XL")
              elif q8 == "n":
                print(k9)
                q9 = input("Jawab: ").lower()
                if q9 == "y":
                  print(telkomsel())
                  print(smartfren())
                  print("\nRekomendasi Telkomsel / Smartfren")
                elif q9 == "n":
                  print(telkomsel())
                  print(tri())
                  print(axis())
                  print(indosat())
                  print("\nRekomendasi Telkomsel / Tri / Axis / Indosat")
          elif q5 == "n":
            print(k10)
            q10 = input("Jawab: ").lower()
            if q10 == "y":
              print(k11)
              q11 = input("Jawab: ").lower()
              if q11 == "y":
                print(k12)
                q12 = input("Jawab: ").lower()
                if q12 == "y":
                  print(k13)
                  q13 = input("Jawab: ").lower()
                  if q13 == "y":
                    print(k14)
                    q14 = input("Jawab: ").lower()
                    if q14 == "y":
                      print(indihome())
                      print("\nRekomendasi Indihome")
                    elif q14 == "n":
                      print(vsat())
                      print("\nRekomendasi Vsat")
                  elif q13 == "n":
                    print(k14)
                    q14 = input("Jawab: ").lower()
                    if q14 == "y":
                      print(indihome())
                      print("\nRekomendasi Indihome")
                    elif q14 == "n":
                      print(vsat())
                      print("\nRekomendasi Vsat")
                elif q12 == "n":
                  print(k13)
                  q13 = input("Jawab: ").lower()
                  if q13 == "y":
                    print(k14)
                    q14 = input("Jawab: ").lower()
                    if q14 == "y":
                      print(indihome())
                      print("\nRekomendasi Indihome")
                    elif q14 == "n":
                      print(vsat())
                      print("\nRekomendasi Vsat")
                  elif q13 == "n":
                    print(k14)
                    q14 = input("Jawab: ").lower()
                    if q14 == "y":
                      print(indihome())
                      print("\nRekomendasi Indihome")
                    elif q14 == "n":
                      print(vsat())
                      print("\nRekomendasi Vsat")
              elif q11 == "n":
                print(k13)
                q13 = input("Jawab: ").lower()
                if q13 == "y":
                  print(vsat())
                  print("\nRekomendasi Vsat")
                elif q13 == "n":
                  print(telkomsel())
                  print("\nRekomendasi Telkomsel / Data yang tersedia")
            elif q10 == "n":
              print(k11)
              q11 = input("Jawab: ").lower()
              if q11 == "y":
                print(k12)
                q12 = input("Jawab: ").lower()
                if q12 == "y":
                  print(k13)
                  q13 = input("Jawab: ").lower()
                  if q13 == "y":
                    print(indihome())
                    print("\nRekomendasi Indihome")
                  elif q13 == "n":
                    print(telkomsel())
                    print("\nRekomendasi Telkomsel")
                elif q12 == "n":
                  print(telkomsel())
                  print("\nRekomendasi Telkomsel")
              elif q11 == "n":
                print(telkomsel())
                print("\nRekomendasi Telkomsel")
      elif q3 == "n":
        print(k5)
        q5 = input("Jawab: ").lower()
        if q5 == "y":
          print(k6)
          q6 = input("Jawab: ").lower()
          if q6 == "y":
            print(k7)
            q7 = input("Jawab: ").lower()
            if q7 == "y":
              print(indihome())
              print(biznet())
              print("\nRekomendasi Indihome / Biznet")
            elif q7 == "n":
              print(k8)
              q8 = input("Jawab: ").lower()
              if q8 == "y":
                print(indihome())
                print("\nRekomendasi Indihome")
              elif q8 == "n":
                print(k9)
                q9 = input("Jawab: ").lower()
                if q9 == "y":
                  print(indihome())
                  print(biznet())
                  print("\nRekomendasi Indihome / Biznet")
                elif q9 == "n":
                  print(indihome())
                  print("\nRekomendasi Indihome")
          elif q6 == "n":
            print(k8)
            q8 = input("Jawab: ").lower()
            if q8 == "y":
              print(xl())
              print(tri())
              print(axis())
              print("\nRekomendasi XL / Tri / Axis")
            elif q8 == "n":
              print(k9)
              q9 = input("Jawab: ").lower()
              if q9 == "y":
                print(telkomsel())
                print(indosat())
                print(smartfren())
                print("\nRekomendasi Telkomsel / Indosat / Smartfren")
              elif q9 == "n":
                print(telkomsel())
                print(tri())
                print(axis())
                print("\nRekomendasi Tri / Axis / Telkomsel")
        elif q5 == "n":
          print(k10)
          q10 = input("Jawab: ").lower()
          if q10 == "y":
            print(k11)
            q11 = input("Jawab: ").lower()
            if q11 == "y":
              print(k12)
              q12 = input("Jawab: ").lower()
              if q12 == "y":
                print(k13)
                q13 = input("Jawab: ").lower()
                if q13 == "y":
                  print(k14)
                  q14 = input("Jawab: ").lower()
                  if q14 == "y":
                    print(indihome())
                    print(firstMedia())
                    print("\nRekomendasi Indihome / First Media")
                  elif q14 == "n":
                    print(vsat())
                    print("\nRekomendasi Vsat")
                elif q13 == "n":
                  print(k14)
                  q14 = input("Jawab: ").lower()
                  if q14 == "y":
                    print(indihome())
                    print("\nRekomendasi Indihome")
                  elif q14 == "n":
                    print(vsat())
                    print("\nRekomendasi Vsat")
              elif q12 == "n":
                print(k13)
                q13 = input("Jawab: ").lower()
                if q13 == "y":
                  print(k14)
                  q14 = input("Jawab: ").lower()
                  if q14 == "y":
                    print(indihome())
                    print("\nRekomendasi Indihome")
                  elif q14 == "n":
                    print(vsat())
                    print("\nRekomendasi Vsat")
                elif q13 == "n":
                  print(k14)
                  q14 = input("Jawab: ").lower()
                  if q14 == "y":
                    print(indihome())
                    print("\nRekomendasi Indihome")
                  elif q14 == "n":
                    print(vsat())
                    print("\nRekomendasi Vsat")
            elif q11 == "n":
              print(k13)
              q13 = input("Jawab: ").lower()
              if q13 == "y":
                print(vsat())
                print("\nRekomendasi Vsat")
              elif q13 == "n":
                print(telkomsel())
                print("\nRekomendasi Telkomsel")
          elif q10 == "n":
            print(k11)
            q11 = input("Jawab: ").lower()
            if q11 == "y":
              print(k12)
              q12 = input("Jawab: ").lower()
              if q12 == "y":
                print(k13)
                q13 = input("Jawab: ").lower()
                if q13 == "y":
                  print(indihome())
                  print("\nRekomendasi Indihome")
                elif q13 == "n":
                  print(telkomsel())
                  print("\nRekomendasi Telkomsel")
              elif q12 == "n":
                print(telkomsel())
                print("\nRekomendasi Telkomsel")
            elif q11 == "n":
              print(telkomsel())
              print("\nRekomendasi Telkomsel")
    elif q2 == "n":
      print(k3)
      q3 = input("Jawab: ").lower()
      if q3 == "y":
        print(k5)
        q5 = input("Jawab: ").lower()
        if q5 == "y":
          print(k6)
          q6 = input("Jawab: ").lower()
          if q6 == "y":
            print(k7)
            q7 = input("Jawab: ").lower()
            if q7 == "y":
              print("Rekomendasi WiFi")
            elif q7 == "n":
              print(k8)
              q8 = input("Jawab: ").lower()
              if q8 == "y":
                print("Rekomendasi Indihome")
              elif q8 == "n":
                print(k9)
                q9 = input("Jawab: ").lower()
                if q9 == "y":
                  print("Rekomendasi WiFi Gamers")
                elif q9 == "n":
                  print("Rekomendasi WiFi")
          elif q6 == "n":
            print(k8)
            q8 = input("Jawab: ").lower()
            if q8 == "y":
              print("Rekomendasi Data untuk Streaming")
            elif q8 == "n":
              print(k9)
              q9 = input("Jawab: ").lower()
              if q9 == "y":
                print("Rekomendasi Data sekitar < 50GB")
              elif q9 == "n":
                print("Rekomendasi Data biasa")
        elif q5 == "n":
          print(k10)
          q10 = input("Jawab: ").lower()
          if q10 == "y":
            print(k11)
            q11 = input("Jawab: ").lower()
            if q11 == "y":
              print(k12)
              q12 = input("Jawab: ").lower()
              if q12 == "y":
                print(k13)
                q13 = input("Jawab: ").lower()
                if q13 == "y":
                  print(k14)
                  q14 = input("Jawab: ").lower()
                  if q14 == "y":
                    print("Rekomendasi Indihome")
                  elif q14 == "n":
                    print("Rekomendasi Vsat")
                elif q13 == "n":
                  print(k14)
                  q14 = input("Jawab: ").lower()
                  if q14 == "y":
                    print("Rekomendasi Indihome")
                  elif q14 == "n":
                    print("Rekomendasi Vsat")
              elif q12 == "n":
                print(k13)
                q13 = input("Jawab: ").lower()
                if q13 == "y":
                  print(k14)
                  q14 = input("Jawab: ").lower()
                  if q14 == "y":
                    print("Rekomendasi Indihome")
                  elif q14 == "n":
                    print("Rekomendasi Vsat")
                elif q13 == "n":
                  print(k14)
                  q14 = input("Jawab: ").lower()
                  if q14 == "y":
                    print("Rekomendasi Indihome")
                  elif q14 == "n":
                    print("Rekomendasi Telkomsel")
            elif q11 == "n":
              print(k13)
              q13 = input("Jawab: ").lower()
              if q13 == "y":
                print("Rekomendasi Vsat")
              elif q13 == "n":
                print("Rekomendasi Telkomsel")
          elif q10 == "n":
            print(k11)
            q11 = input("Jawab: ").lower()
            if q11 == "y":
              print(k12)
              q12 = input("Jawab: ").lower()
              if q12 == "y":
                print(k13)
                q13 = input("Jawab: ").lower()
                if q13 == "y":
                  print("Rekomendasi Indihome")
                elif q13 == "n":
                  print("Rekomendasi Telkomsel")
              elif q12 == "n":
                print("Rekomendasi Telkomsel")
            elif q11 == "n":
              print("Rekomendasi Telkomsel")
      elif q3 == "n":
        print(k5)
        q5 = input("Jawab: ").lower()
        if q5 == "y":
          print(k11)
          q11 = input("Jawab: ").lower()
          if q11 == "y":
            print(k6)
            q6 = input("Jawab: ").lower()
            if q6 == "y":
              print(k7)
              q7 = input("Jawab: ").lower()
              if q7 == "y":
                print("Rekomendasi WiFi")
              elif q7 == "n":
                print(k13)
                q13 = input("Jawab: ").lower()
                if q13 == "y":
                  print(k14)
                  q14 = input("Jawab: ").lower()
                  if q14 == "y":
                    print("Rekomendasi Indihome")
                  elif q14 == "n":
                    print("Rekomendasi Telkomsel")
                elif q13 == "n":
                  print("Rekomendasi Telkomsel")
            elif q6 == "n":
              print(k13)
              q13 = input("Jawab: ").lower()
              if q13 == "y":
                print(k14)
                q14 = input("Jawab: ").lower()
                if q14 == "y":
                  print("Rekomendasi Indihome")
                elif q14 == "n":
                  print("Rekomendasi Telkomsel")
              elif q13 == "n":
                print("Rekomendasi Telkomsel")
          elif q11 == "n":
            print(k6)
            q6 = input("Jawab: ").lower()
            if q6 == "y":
              print(k7)
              q7 = input("Jawab: ").lower()
              if q7 == "y":
                print("Rekomendasi WiFi")
              elif q7 == "n":
                print(k13)
                q13 = input("Jawab: ").lower()
                if q13 == "y":
                  print(k14)
                  q14 = input("Jawab: ").lower()
                  if q14 == "y":
                    print("Rekomendasi Indihome")
                  elif q14 == "n":
                    print("Rekomendasi Telkomsel")
                elif q13 == "n":
                  print("Rekomendasi Telkomsel")
            elif q6 == "n":
              print(k13)
              q13 = input("Jawab: ").lower()
              if q13 == "y":
                print(k14)
                q14 = input("Jawab: ").lower()
                if q14 == "y":
                  print("Rekomendasi Indihome")
                elif q14 == "n":
                  print("Rekomendasi Telkomsel")
              elif q13 == "n":
                print("Rekomendasi Telkomsel")
        elif q5 == "n":
          print(k10)
          q10 = input("Jawab: ").lower()
          if q10 == "y":
            print(k11)
            q11 = input("Jawab: ").lower()
            if q11 == "y":
              print(k12)
              q12 = input("Jawab: ").lower()
              if q12 == "y":
                print(k13)
                q13 = input("Jawab: ").lower()
                if q13 == "y":
                  print(k14)
                  q14 = input("Jawab: ").lower()
                  if q14 == "y":
                    print("Rekomendasi Indihome")
                  elif q14 == "n":
                    print("Rekomendasi Telkomsel")
                elif q13 == "n":
                  print("Rekomendasi Telkomsel")
              elif q12 == "n":
                print("Rekomendasi Telkomsel")
            elif q11 == "n":
              print("Rekomendasi Telkomsel")
          elif q10 == "n":
            print("Rekomendasi Telkomsel")         
  elif q1 == "n":
    print("Maaf, Aplikasi ini hanya dapat mencari data rekomendasi Internet")
  else:
    print("Jawaban tidak valid")