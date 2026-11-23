# ==============================================
# TUGAS PERTEMUAN 6 - OPERATOR LOGIKA
# Nama : INTAN
# NIM  : 26241042
# ==============================================

# Langkah 1: Memasukkan digit A dan B dari NIM
a = int(input("Digit A: "))
b = int(input("Digit B: "))

# Langkah 2: Membuat dua kondisi
kondisi1 = a >= 5
kondisi2 = b >= 5

# Langkah 3: Menampilkan nilai kondisi
print("\nKondisi 1:", kondisi1)
print("Kondisi 2:", kondisi2)

# Langkah 4: Operasi Logika
print("\nNOT:", not kondisi1)          # Logika BUKA / NEGASI
print("AND:", kondisi1 and kondisi2)   # Logika DAN
print("OR :", kondisi1 or kondisi2)    # Logika ATAU
print("XOR:", kondisi1 ^ kondisi2)     # Logika EKSKLUSIF ATAU

# Langkah 5: Komentar Penjelasan
# Mengapa OR dan XOR berbeda saat kedua kondisi True?
# OR = Benar jika salah satu atau keduanya Benar
# XOR = Benar HANYA jika keduanya BERBEDA, jika sama (sama-sama True/False) hasilnya SALAH
()