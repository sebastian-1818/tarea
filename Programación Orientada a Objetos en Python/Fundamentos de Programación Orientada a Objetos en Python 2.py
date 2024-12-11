class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True

    def deposit(self, amount): # Método para depositar dinero en la cuenta
        if self.is_active:
            self.balance += amount # Aumenta el saldo con la cantidad depositada
            print(f"Se ha depositado {amount}. Saldo actual: {self.balance}")
        else:
            print("No se puede depositar, cuenta inactiva")

    def withdraw(self, amount): # Método para retirar dinero de la cuenta
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Se ha retirado {amount}. Saldo actual: {self.balance}")
            else:
                print("No se puede retirar, saldo insuficiente.")
        else:
            print("No se puede retirar, cuenta inactiva.")

    def deactivate_account(self): # Método para desactivar la cuenta
        self.is_active = False
        print("La cuenta ha sido desactivada.")

    def activate_account(self):  # Método para activar la cuenta
        self.is_active = True
        print("La cuenta ha sido activada.")

# Crear instancias de cuentas
account1 = BankAccount("Ana", 500)  
account2 = BankAccount("Luis", 1000)

# Llamada a los métodos
account1.deposit(200)  # Depositar en cuenta de Ana
account2.deposit(100)   # Depositar en cuenta de Luis
account1.deactivate_account()  # Desactivar cuenta de Ana
account1.deposit(50)   # Intentar depositar en cuenta inactiva
account1.activate_account()  # Activar cuenta de Ana
account1.deposit(50)   # Depositar en cuenta de Ana
account1.withdraw(100) # Retirar de la cuenta de Ana
account1.withdraw(700)  # Intentar retirar más de lo que tiene

               