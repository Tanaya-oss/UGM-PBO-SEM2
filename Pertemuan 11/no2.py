class Model(object):
    services = {
        'email' : {'number': 1000, 'price': 2,},
        'sms' : {'number': 1000, 'price': 10,},
        'voice': {'number': 1000, 'price':15,},   
    }

class View(object):
    def list_services(self, services):
        for svc in services:
            print(svc,'')

    def list_pricing(self,services):
        for svc in services:
            print("For", Model.services[svc]['number'],
                  svc, "message you pay $",
                  Model.services[svc]['price']),

class Controller(object):
    def __init__(self):
        self.model = Model()
        self.view = View()
        self.view2 = View2()

    def get_services(self):
        services = self.model.services.keys()
        if language == 1:
            return(self.view.list_services(services))
        else:
            return(self.view2.list_services(services))
    
    def get_pricing(self):
        services = self.model.services.keys()
        if language == 1:
            return(self.view.list_pricing(services))
        else:
            return(self.view2.list_pricing(services))

class View2(object):
    def list_services(self, services):
        for svc in services:
            print(svc,'')

    def list_pricing(self,services):
        for svc in services:
            print("Untuk setiap", Model.services[svc]['number'],
                  svc, "anda membayar $",
                  Model.services[svc]['price']),    

#Instansiasi objek
controller = Controller()
language = int(input("What language do you choose? [1]English [2]Indonesia:"))
if language == 1:
    print("Service Provided:")
    controller.get_services()
    print("Pricing for Services:")
    controller.get_pricing()
elif language == 2:
    print("Layanan yang disediakan:")
    controller.get_services()
    print("Tarif tiap layanan:")
    controller.get_pricing()
else:
    print("Error, choose the language number!")
