angka = int(input("Masukan angka: "))
if angka == 1:
    print("Bukan Angka prima")
elif angka == 2:
    print("Angka Prima")
elif angka == 3:
    print("Angka Prima")
elif angka % 2 == 0:
    print("Bukan Angka Prima")
elif angka % 3 == 0:
    print("Bukan Angka Prima")
elif angka % 5 == 0:
    print("Bukan Angka Prima")
elif angka < 1:
    print("Bukan Angka Prima")
else:
    print("Angka Prima")
