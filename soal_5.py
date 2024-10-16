#meminta pengguna untuk memasukkan nilai integer n:
n = int(input("Enter the value of n: "))

#mencetak angka dari 1 hingga n, di mana setiap angka i dicetak sebanyak i kali, dan pindah ke baris baru setelah setiap angka.
for i in range(1, n + 1):
    for j in range(i):
        print(i, end=' ')
    print()  # To move to the next line
