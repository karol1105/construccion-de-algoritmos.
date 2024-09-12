__author__ = "Karol Isabella Cabrera"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "karol.cabrerap@campusucc.edu.co"

class CuentaCorriente:
    #aqui inicia la declaracion de clase
    
    """#_______________________________________________________________
    
    # Atributos
    _________________________________________________________________#"""
  
    __saldo = 0

    """#_______________________________________________________________
    
    # Metodos
    _________________________________________________________________#"""

    __method__ = "DarSaldo"
    __parameter__ = "ninguno"
    __return__ = "saldo de la cuenta"
    __description__ = "metodo quue retorna el saldo de la cuenta"

    def DarSaldo(self):
        return self.__saldo



    __method__ = "ConsignarSaldo"
    __parameter__ = "monto"
    __return__ = "ninguno"
    __description__ = "metodo que permite consignar un monto a la cuenta"

    def ConsignarSaldo(self, monto):
        # aqui va mi codigo
        self.__saldo  =  self.__saldo+monto



    __method__ = "RetirararSaldo"
    __parameter__ = "monto"
    __return__ = "ninguno"
    __description__ = "metodo que permite retirar un monto de la cuenta"

    def RetirarSaldo(self, monto):
        # aqui va mi codigo
        self.__saldo = self.__saldo-monto
   