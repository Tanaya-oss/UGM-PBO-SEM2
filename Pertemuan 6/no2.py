from abc import ABC, abstractmethod

class BalapKarung(ABC):
    def __init__(self, nama, jarak_lompat):
        self.nama = nama
        self.jarak_lompat = jarak_lompat
        
    @abstractmethod
    def juara(self):
        pass

class KarungGoni(BalapKarung):
    def __init__(self, nama, jarak_lompat):
        super().__init__(nama, jarak_lompat) 
        
    def juara(self):
        efisiensi = (2000//self.jarak_lompat ) 
        self.waktu_finish = efisiensi * 5 #karung goni dapat melompat tiap 5 detik
        print(f"{self.nama} sampai finish dalam waktu {self.waktu_finish/60} menit")

class KarungBeras(BalapKarung):
    def __init__(self, nama, jarak_lompat):
        super().__init__(nama, jarak_lompat) 

    def juara(self):
        efisiensi = (2000//self.jarak_lompat ) 
        self.waktu_finish = efisiensi * 6 #karung beras dapat melompat tiap 6 detik
        print(f"{self.nama} sampai finish dalam waktu {self.waktu_finish/60} menit")
    
asep = KarungGoni("Asep", 30)
bagas = KarungBeras("Bagas", 35)

print("==Lomba Balap Karung 20 Meter==")
asep.juara()
bagas.juara()
