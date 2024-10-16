# meminta pengguna untuk memasukkan tiga angka menggunakan fungsi input(), lalu mengonversi input tersebut menjadi bilangan desimal (float) dan menyimpannya dalam variabel a, b, dan c.
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

#ini mengecek apakah a adalah angka terbesar di antara a,
if a >= b and a >= c:
    print(f"The largest number is {a}")

#mengecek apakah b adalah angka terbesar di antara b, a, dan c. Jika ya, program akan mencetak: "The largest number is b".
elif b >= a and b >= c:
    print(f"The largest number is {b}")

# mencetak "The largest number is c" jika a dan b tidak lebih besar atau sama dengan c.
else:
    print(f"The largest number is {c}")
