class Elemen:
    anemo = "Angin"
    def __init__(self, anemo):
        self.anemo = anemo

    def tampilkan_data(self):
        print("Karakter anemo:", self.anemo)

karakter1 = Elemen("Xiao")
karakter1.tampilkan_data()

del karakter1.anemo
del Elemen.anemo
print('efek keyword del')
karakter1.tampilkan_data()