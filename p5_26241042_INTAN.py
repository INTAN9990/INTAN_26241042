# Memasukkan data dari pengguna
nama = input("Nama mahasiswa : ")
nim_lengkap = input("NIM lengkap    : ")
digit_a = input("Digit A        : ")
digit_b = input("Digit B        : ")

# Ubah ke bilangan bulat
A = int(digit_a)
B = int(digit_b)

# Menampilkan hasil perbandingan
print("\n===== HASIL PERBANDINGAN =====")
print(f"A > B  : {A > B}")
print(f"A < B  : {A < B}")
print(f"A == B : {A == B}")
print(f"A != B : {A != B}")
print(f"A >= B : {A >= B}")
print(f"A <= B : {A <= B}")