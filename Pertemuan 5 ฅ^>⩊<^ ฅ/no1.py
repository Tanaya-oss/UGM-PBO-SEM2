class Xiao:
    def name(self):
        print("Xiao")

    def vision(self):
        print("Anemo")
    
    def weapon(self):
        print("Polearm")

class Wriothesley:
    def name(self):
        print("Wriothesley")

    def vision(self):
        print("Cryo")

    def weapon(self):
        print("Catalyst")

xiao = Xiao()
wriothesley = Wriothesley()

for character in (xiao,wriothesley):
    character.name()
    character.vision()
    character.weapon()
    print()
