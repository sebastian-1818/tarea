class Car:
    def _init_(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self. is_available = True
        
        def sell(self):
            if self.is_available:
                self.is_available = False
                print(f"El coche {self.brand}{self.model} ha sido vendido.")
            else:
                print(f"El coche {self.brand} {self.model} no esta disponible.")
                
        def check_availability(self):
            return self.is_available
        
        def get_price(self):
            return self.price
        
        
class customer:
    def _init_(self, name):
        self.name = name
        self.cars_purchased = []
        
    def buy_car(self, car):
        if car.check_availability():
            car.sell()
            self.cars_purchased.append(car)
        else:
            print(f"Lo siento {car.brand} {car. model} no esta disponible.")
            
        def inquire_car(self, car):
            availability = "disponible" if car.check_availability() else "no disponible"
            print(f"El coche {car.brand} {car.model} esta {availability} y cuesta")
            
        
class Dealership:
    def _init_(self):
        self.inventory = []
        self.customers = []
        
    def add_car(self, car):
        self.inventory.append(car)
        print(f"El coche {car.brand} {car.model} ha sido añadido al inventario.")
    
    def register_customer(self, customer):
        self.customers.append(customer)
        print(f"El cliente {customer.name} ha sido registrado en la concensionaria.")
        
    def show_available_cars(self):
        print("Coches disponibles en la concesionaria:")
        for car in self.inventory:
            if car.check_availability():
                print(f"- {car.brand} {car.model} por {car.get_prince()}")
                
# Crear instancias de coshes
car1 = Car("Toyota", "Corolla", 20000)
car2 = Car("Honda", "Civic", 22000)
car3 = Car("Ford", "Mustang", 35000)

# Crear instancia de cliente
cutomer1 = Customer("Carlos")

# Crear instancia de concesionaria y registrar coches y clientes
dealership = Dealership()
dealership.add_car(car1)
dealership.add_car(car2)
dealership.add_car(car3)
dealership.add_register_customer(customer1)

# Mostrar coches disponibles
dealership.show_available_cars()

# Cliente consulta un coche
customer1:inquire_car(car1)

#Mostrar coches disponibles nuevamente
dealership.show_available_cars()

# Cliente intenta comprar un coche ya vendido
customer1.buy_car(car1)
                