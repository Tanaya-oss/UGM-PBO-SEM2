class Honkai:
    def __init__(self, name, path, elemen):
        self.name = name
        self.path = path
        self.elemen = elemen

    def info(self):
        print(f"name: {self.name}")
        print(f"path: {self.path}")
        print(f"elemen: {self.elemen}")
        print()
    
karakter1 = Honkai("Kafka","Nihility", "Lighting")
karakter2 = Honkai("Blade", "Destruction", "Wind" )
karakter3 = Honkai("Firefly", "Destruction", "Fire")
karakter4 = Honkai("Silverwolf", "Nihility", "Quantum")

karakter1.info()
karakter2.info()
karakter3.info()
karakter4.info()