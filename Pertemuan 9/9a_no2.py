class Genshin:
    damage_boss = 19000
    def __init__(self, nama, HP, shield, ):
        self.nama = nama
        self.shield = shield
        self.HP = HP


    @classmethod
    def ketahanan_shield(cls, shield, ):
        return shield - cls.damage_boss
    
    @staticmethod
    def HP_sisa(HP,shield):
        return (Genshin.damage_boss - shield) + HP

    @property
    def kehidupan(self):
        damage_boss = 19000
        karakter = self.shield + self.HP - damage_boss
        if karakter < 0:
            return "Mati"
        else:
            return "Hidup"

zhongli = Genshin.ketahanan_shield(20000)
print(f"Shield Zhongli mampu menahan {zhongli} damage lagi")

zhongli = Genshin.HP_sisa(30000, 20000)
print(f"Total damage yang masih bisa ditahan Zhongli {zhongli}")  

zhongli = Genshin("Zhongli", 30000, 20000)
print(f"Karakter {zhongli.nama} dalam posisi {zhongli.kehidupan}")