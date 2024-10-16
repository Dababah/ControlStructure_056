#Baris ini meminta pengguna memasukkan nilai persentase
percentage = float(input("Enter the percentage: "))

#memeriksa apakah nilai percentage lebih besar dari atau sama dengan 90:
if percentage >= 90:
    print("Excellent performance")
elif percentage >= 80:
    print("Very Good performance")
# memeriksa apakah nilai lebih besar dari atau sama dengan 70,jika sesuai akan menampilkan sesuai print
elif percentage >= 70:
    print("Good performance")
 #memeriksa apakah nilai lebih besar dari atau sama dengan 60,dan jika benar akan mencetak sesuai print   
elif percentage >= 60:
    print("Average performance")
#semua kondisi di atas tidak terpenuhi,kondisi default,membutukan perbaikan
else:
    print("Needs improvement")
