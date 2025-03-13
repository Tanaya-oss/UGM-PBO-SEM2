class Jamur:
    def intro(self):
        print("Ada banyak sekali jenis jamur.")
    
    def edible(self):
        print("Ada jamur yang dapat dimakan, tetapi ada juga yang tidak.")

class Tiram(Jamur):
    def edible(self):
        print("Jamur Tiram dapat dimakan.")

class Death_Cap(Jamur):
    def edible(self):
        print("Jamur Death Cap tidak dapat dimakan.")

obj_jamur = Jamur()
obj_tiram = Tiram()
obj_death_cap = Death_Cap()

obj_jamur.intro()
obj_jamur.edible()


obj_tiram.edible()
obj_death_cap.edible()