class Persegi:
    def luas(s):
        hasil_luas = s*s
        print("Luas Persegi: ",hasil_luas)
    def keliling(s):
        hasil_keliling = 4*s
        print("Keliling Persegi: ",hasil_keliling)
    
s = int(input("Masukan Sisi Persegi: "))
Persegi.luas(s)
Persegi.keliling(s)