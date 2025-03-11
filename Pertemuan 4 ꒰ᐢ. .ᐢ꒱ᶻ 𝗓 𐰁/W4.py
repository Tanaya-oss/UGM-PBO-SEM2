#Nomor 1
class Orang:
    def __init__(self,nama_dpn,nama_blk,no_id):
        self.nama_dpn = nama_dpn
        self.nama_blk = nama_blk
        self.no_id = no_id

#Nomor 2        
class Mahasiswa(Orang):
    SARJANA, MASTER,  DOKTOR = range(3)
    def __init__(self,nama_dpn,nama_blk,no_id,jenjang):
        super().__init__(nama_dpn, nama_blk, no_id)
        self.jenjang = jenjang
        self.matkul = []
    
    def enrol(self, input_matkul):
        self.matkul.append(input_matkul)

    def tampilkan_data(self):
        print(f"Nama : {self.nama_dpn} {self.nama_blk}")
        print(f"No ID : {self.no_id}")
        print(f"Matkul yang Diambil: {self.matkul}")

        
#Nomor 3      
class Karyawan(Orang):
    TETAP, TDK_TETAP = range(2)
    def __init__(self, nama_dpn, nama_blk, no_id, status_karyawan):
        super().__init__(nama_dpn, nama_blk, no_id)
        self.status_karyawan = status_karyawan
    
#Nomor 4    
class Dosen(Karyawan):
    def __init__(self, nama_dpn, nama_blk, no_id, status_karyawan):
        super().__init__(nama_dpn, nama_blk, no_id, status_karyawan)
        self.matkul_diajar = []
    
    def mengajar(self, input_matkul_diajar):
        self.matkul_diajar.append(input_matkul_diajar)
    
    def tampilkan_data(self):
        print(f"Nama : {self.nama_dpn} {self.nama_blk}")
        print(f"No ID : {self.no_id}")
        print(f"Mengajar Matkul: {self.matkul_diajar}")

#Nomor 5
bowo = Mahasiswa("Bowo", "Nugroho", "987654", Mahasiswa.SARJANA)
bowo.enrol("Basis Data")  
bowo.tampilkan_data()

#Nomor 6
rizki = Dosen("Rizki", "Setiabudi", "456789", Dosen.TETAP)
rizki.mengajar("Statistik")
rizki.tampilkan_data()

#Nomor 7
class Pelajar:
    def __init__(self):
        self.matkul = []

    def enrol(self, mata_kuliah):
        self.matkul.append(mata_kuliah)
    
#Nomor 8
class Pengajar:
    def __init__(self):
        self.matkul_diajar = []

    def mengajar(self, input_matkul_diajar):
        self.matkul_diajar.append(input_matkul_diajar)
        
#Nomor 9
class Asdos(Orang, Pelajar, Pengajar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Pelajar.__init__(self)
        Pengajar.__init__(self)
    
    def tampilkan_data(self):
        print(f"Nama : {self.nama_dpn} {self.nama_blk}")
        print(f"No ID : {self.no_id}")
        print(f"Matkul yang Diambil : {self.matkul}")    
        print(f"Matkul yang Diajar : {self.matkul_diajar}") 

#Nomor 10
uswatun = Asdos("Uswatun", "Hasanah", "45656")
uswatun.enrol("Big Data")
uswatun.mengajar("Kecerdasan Artifisial")
uswatun.tampilkan_data()
