from collections import namedtuple

Orang = namedtuple("Orang", "nama anak")

class class_Orang(Orang):
    def tampilkan_info(self):
        print("Nama : ", self.nama)
        print("Nama anak: ")
        for i in range(len(self.anak)):
            print(f"{i+1}. {self.anak[i]}")
            
john = class_Orang("John Doe", ["Timmy", "Jimmy"])
john.anak.append("Tina")

john.tampilkan_info()