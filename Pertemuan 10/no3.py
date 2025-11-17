from abc import ABC
class Vision(ABC):
    def elemen(self):
        pass

class Anemo(Vision):
    def elemen(self):
        return "Anemo memiliki atribut Angin"
    
class Pyro(Vision):
    def elemen(self):
        return "Pyro memiliki atribut Api"
    
class Cryo(Vision):
    def elemen(self):
        return "Cryo memiliki atribut Es"
    
class Factory:
    @staticmethod
    def input_karakter(jenis_vision):
        if jenis_vision == "Anemo":
            return Anemo()
        elif jenis_vision == "Pyro":
            return Pyro()
        elif jenis_vision == "Cryo":
            return Cryo()
        else:
            raise ValueError("Vision ini belum terdaftar")
        
xiao = Factory.input_karakter("Anemo")
print(xiao.elemen())

wriothesley = Factory.input_karakter("Cryo")
print(wriothesley.elemen())
