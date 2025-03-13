class Pembagian:
    def __init__(self, banyak_permen):
        self.banyak_permen = banyak_permen

    def __floordiv__(self, kunjungan):
        print('Permen yang tersedia bulan ini:',self.banyak_permen)
        print('Anak-anak yang datang ke Taman Edukasi bulan ini:', kunjungan.qty_bagi, 'anak')
        return self.banyak_permen//kunjungan.qty_bagi

class Anak:
    def __init__(self, qty_bagi):
        self.qty_bagi = qty_bagi

permen = Pembagian(300)
qty_juli = Anak(10)
print(f"Tiap anak akan mendapatkan {permen//qty_juli} permen")