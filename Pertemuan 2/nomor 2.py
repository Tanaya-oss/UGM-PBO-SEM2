class Character:
    def __init__ (self,Nama,Vision,Senjata):
        self.Nama = Nama
        self.Vision = Vision
        self.Senjata = Senjata

    def tampilkan_data(self):
        print("Nama :"+ self.Nama)
        print("Vision: "+self.Vision)
        print("senjata: "+self.Senjata)
        print()

Character1 = Character("Xiao","Anemo","Polearm")
Character2 = Character("Wriothesley","Cryo","Catalyst")
Character3 = Character("Alhaitham","Dendro","Sword")

Character1.tampilkan_data()
Character2.tampilkan_data()
Character3.tampilkan_data()