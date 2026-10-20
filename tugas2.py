import turtle
import math
import colorsys

# Bagian inisialisasi awal NIM Anda
nim = 26241042
nim_str = str(nim)

# Menyimpan digit NIM ke dalam variabel sesuai instruksi sebelumnya
digit_1 = int(nim_str[0])  # 2
digit_2 = int(nim_str[1])  # 6
digit_3 = int(nim_str[2])  # 2
digit_4 = int(nim_str[3])  # 4
digit_5 = int(nim_str[4])  # 1

# Setup Layar dan Turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
t.hideturtle()

# Loop pembentukan pola geometri berbasis NIM
for i in range(360):
    # Pewarnaan gradasi menggunakan konsep HSV
    h = (0.85 + i / 720) % 1.0
    c = colorsys.hsv_to_rgb(h, 0.9, 1.0)
    t.pencolor(c)
    
    # MODIFIKASI MENGGUNAKAN NIM:
    # 262 didapat dari gabungan digit_1, digit_2, dan digit_3
    # digit_1 (nilai: 2) digunakan sebagai pengali sudut gelombang (membuat pola 2 atau 4 kelopak besar)
    r = (digit_1 * 100 + digit_2 * 10 + digit_3) * math.sin(math.radians(digit_1 * i))
    
    # Menghitung koordinat x dan y
    x = r * math.cos(math.radians(i))
    y = r * math.sin(math.radians(i))
    
    # Menggerakkan turtle ke koordinat tujuan
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(digit_5 + 2) # Ukuran lingkaran kecil disesuaikan digit_5 (1 + 2 = 3)

turtle.done()

import turtle
import math
import colorsys

# Bagian inisialisasi awal NIM Anda
nim = 26241042
nim_str = str(nim)

# Menyimpan digit NIM ke dalam variabel sesuai instruksi sebelumnya
digit_1 = int(nim_str[0])  # 2
digit_2 = int(nim_str[1])  # 6
digit_3 = int(nim_str[2])  # 2
digit_4 = int(nim_str[3])  # 4
digit_5 = int(nim_str[4])  # 1

# Setup Layar dan Turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
t.hideturtle()

# Loop pembentukan pola geometri berbasis NIM
for i in range(360):
    # Pewarnaan gradasi menggunakan konsep HSV
    h = (0.85 + i / 720) % 1.0
    c = colorsys.hsv_to_rgb(h, 0.9, 1.0)
    t.pencolor(c)
    
    # MODIFIKASI MENGGUNAKAN NIM:
    # 262 didapat dari gabungan digit_1, digit_2, dan digit_3
    # digit_1 (nilai: 2) digunakan sebagai pengali sudut gelombang (membuat pola 2 atau 4 kelopak besar)
    r = (digit_1 * 100 + digit_2 * 10 + digit_3) * math.sin(math.radians(digit_1 * i))
    
    # Menghitung koordinat x dan y
    x = r * math.cos(math.radians(i))
    y = r * math.sin(math.radians(i))
    
    # Menggerakkan turtle ke koordinat tujuan
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(digit_5 + 2) # Ukuran lingkaran kecil disesuaikan digit_5 (1 + 2 = 3)

turtle.done()
import turtle
import math
import colorsys

# Bagian inisialisasi awal NIM Anda
nim = 26241042
nim_str = str(nim)

# Menyimpan digit NIM ke dalam variabel sesuai instruksi sebelumnya
digit_1 = int(nim_str[0])  # 2
digit_2 = int(nim_str[1])  # 6
digit_3 = int(nim_str[2])  # 2
digit_4 = int(nim_str[3])  # 4
digit_5 = int(nim_str[4])  # 1

# Setup Layar dan Turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
t.hideturtle()

# Loop pembentukan pola geometri berbasis NIM
for i in range(360):
    # Pewarnaan gradasi menggunakan konsep HSV
    h = (0.85 + i / 720) % 1.0
    c = colorsys.hsv_to_rgb(h, 0.9, 1.0)
    t.pencolor(c)
    
    # MODIFIKASI MENGGUNAKAN NIM:
    # 262 didapat dari gabungan digit_1, digit_2, dan digit_3
    # digit_1 (nilai: 2) digunakan sebagai pengali sudut gelombang (membuat pola 2 atau 4 kelopak besar)
    r = (digit_1 * 100 + digit_2 * 10 + digit_3) * math.sin(math.radians(digit_1 * i))
    
    # Menghitung koordinat x dan y
    x = r * math.cos(math.radians(i))
    y = r * math.sin(math.radians(i))
    
    # Menggerakkan turtle ke koordinat tujuan
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(digit_5 + 2) # Ukuran lingkaran kecil disesuaikan digit_5 (1 + 2 = 3)

turtle.done()
