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

    def get_services(self):
        services = self.model.services.keys()
        return(self.view.list_services(services))
    
    def get_pricing(self):
        services = self.model.services.keys()
        return(self.view.list_pricing(services))
    
    def bid_price(self):
        tawar = str(input("What services do you want to bid? email, sms, or voice: ").lower())
        harga = int(input("Enter the price you want (in $):"))
        self.model.services[tawar]['price'] = harga

    
#Instansiasi objek
controller = Controller()
print("Service Provided:")
controller.get_services()
controller.get_pricing()
controller.bid_price()
print("Price accroding to your bid:")
controller.get_pricing()
