""" Para esta tarea, agregaremos algunas funciones a la clase Usuario:

hacer_retiro(self, amount): haz que este método reduzca el balance del usuario en la cantidad especificada 
mostrar_balance_usuario(self): haz que este método imprima el nombre del usuario y el balance de cuenta en la terminal 
Ej.: “Usuario: Guido van Rossum, Balance: $150
BONUS: transfer_dinero(self, other_user, amount): haz que este método reduzca el balance del usuario por el monto y agrega esa cantidad al balance de otro_usuario 
"""

class Usuario:
    def __init__(self, name):
        self.name = name
        self.balance_cuenta = 1000

    def hacer_deposito(self, amount):
        self.balance_cuenta += amount 

    def hacer_retiro(self, amount):
        self.balance_cuenta -= amount 
        
    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.name}, Balance: ${self.balance_cuenta}")

    def transfer_dinero(self, other_user, amount):
        self.balance_cuenta -= amount
        other_user.balance_cuenta += amount

#no se usa print ya que esta dentro del metodo mostrar_balance
guido = Usuario ("Guido van Rossum")
guido.hacer_deposito(100)
guido.hacer_deposito(100)
guido.hacer_deposito(100)
guido.hacer_retiro(100)
guido.mostrar_balance_usuario()  #imprime el Usuario: y Balance:


emi = Usuario ("Emilia")
emi.hacer_deposito(500)
emi.hacer_deposito(500)
emi.hacer_retiro(200)
emi.hacer_retiro(200)
emi.mostrar_balance_usuario()


eve = Usuario("Eve")
eve.hacer_deposito(1000)
eve.hacer_retiro(300)
eve.hacer_retiro(300)
eve.hacer_retiro(300)
eve.mostrar_balance_usuario()

guido.transfer_dinero(eve, 200)  # Transferir $200 de Guido a Eve
guido.mostrar_balance_usuario()   
eve.mostrar_balance_usuario()



