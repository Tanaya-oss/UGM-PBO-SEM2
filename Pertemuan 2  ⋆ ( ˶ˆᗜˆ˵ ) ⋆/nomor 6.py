class Manusia:
    def __init__ (self, nama,umur):
        self.nama = nama
        self.umur = umur
    def tampilkan(self):
        print("Nama : "+self.nama)
        print("Umur : "+ str(self.umur))

def main():
    nama = input("Masukan Nama: ")
    umur = int(input("Masukan Umur: "))
    Manusia1 = Manusia(nama,umur)
    Manusia1.tampilkan()

if __name__ == "__main__":
    main()