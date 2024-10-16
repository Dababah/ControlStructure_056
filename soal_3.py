#untuk meminta pengguna memasukkan jumlah suku Fibonacci yang ingin ditampilkan:
n = int(input("Enter the number of Fibonacci terms: "))

a, b = 0, 1
print("Fibonacci series:")

#mencetak deret Fibonacci berdasarkan jumlah suku yang diminta:
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b
print()  # To move to the next line
