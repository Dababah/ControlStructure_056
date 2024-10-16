#meminta pengguna memasukkan batas n dan mencetak pesan untuk menampilkan bilangan ganjil hingga n.
n = int(input("Enter the limit: "))

print(f"Odd numbers up to {n}:")

#mencetak bilangan ganjil dari 1 hingga n, dengan spasi di antara setiap angka, lalu pindah ke baris baru.
for i in range(1, n+1, 2):
    print(i, end=' ')
print()  # To move to the next line
