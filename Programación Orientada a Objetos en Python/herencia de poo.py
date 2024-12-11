class Car:
    def __init__(self, brand, model, price):  # Constructor para inicializar las propiedades del coche
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True
# Método para vender el coche
    def sell(self):
        if self.is_available:
            self.is_available = False  # Cambia el estado a no disponible
            print(f"El coche {self.brand} {self.model} ha sido vendido.")
        else:
            print(f"El coche {self.brand} {self.model} no está disponible.")

    def check_availability(self):
        return self.is_available
     # Método para obtener el precio del coche
    def get_price(self):
        return self.price
    # Clase que representa un cliente
class Costumer:
    def __init__(self, name):  
        self.name = name
        self.cars_purchased = []
# Método para que el cliente compre un coche
    def buy_car(self, car):
        if car.check_availability():
            car.sell()
            self.cars_purchased.append(car)  # Añade el coche a la lista de coches comprados
        else:
            print(f"Lo siento, {car.brand} {car.model} no está disponible.")

    def inquire_car(self, car):
        availability = "disponible" if car.check_availability() else "no está disponible"  
        print(f"El coche {car.brand} {car.model} está {availability} y cuesta {car.price}")    
# Clase que representa una concesionaria
class Dealership:
    def __init__(self): 
        self.inventory = []
        self.customers = []  
# Método para agregar un coche al inventario de la concesionaria
    def add_car(self, car):
        self.inventory.append(car)
        print(f"El coche {car.brand} {car.model} ha sido agregado al inventario")
 # Método para mostrar los coches disponibles en la concesionari
    def register_customer(self, customer):  
        self.customers.append(customer)
        print(f"El cliente {customer.name} ha sido registrado")

    def show_available_cars(self):
        print("Coches disponibles en la concesionaria:")
        for car in self.inventory:
            if car.check_availability():
                print(f"{car.brand} {car.model} por {car.price}")

# Crear instancias de coches
car1 = Car("Toyota", "Corolla", 20000)
car2 = Car("Honda", "Civic", 22000)
car3 = Car("Ford", "Mustang", 35000)

# Crear instancia de cliente
customer1 = Costumer("Sebastian")  

# Crear instancia de concesionaria y registrar coches y clientes
dealer = Dealership()
dealer.add_car(car1)
dealer.add_car(car2)
dealer.add_car(car3)
dealer.register_customer(customer1)

# Mostrar coches disponibles
dealer.show_available_cars()

# Cliente consulta un coche
customer1.inquire_car(car1)

# Cliente compra coche
customer1.buy_car(car1)

# Mostrar coches disponibles nuevamente
dealer.show_available_cars()

# Cliente intenta comprar un coche ya vendido    
customer1.buy_car(car1)

