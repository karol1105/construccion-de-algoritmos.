__author__ = "Karol Isabella Cabrera"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "karol.cabrerap@campusucc.edu.co"

class CuentaAhorros:
    # Aqui inicia la declaracion de la clase
    
    """#_______________________________________________________________
    
    # Atributos
    _________________________________________________________________#"""
  
    __saldo = 0 
    __interesMensual = 0
    
    """#_______________________________________________________________
    
    # metodos
    _________________________________________________________________#"""
    
    
    
    __method__ = "DarSaldo"
    __parameter__ = "ninguno"
    __return__ = "saldo de la cuenta"
    __description__ = "metodo que retorna el saldo de la cuenta del cliente"
    
    def Darsaldo(self):
        #aqui va el codigo
        return self.__saldo



    __method__ = "consignarSaldo"
    __parameter__ = "monto"
    __return__ = "ninguno"
    __description__ = "metodo que permite comsignar un monto a la cuenta"
    
    def ConsignarSaldo(self, monto):
        #aqui va el codigo
       self.__saldo=self. __saldo+monto

        
        
    __method__ = "retirarsaldo"
    __parameter__ = "monto"
    __return__ = "ninguno"
    __description__ = "metodo que retorna el valor retirado"
    
    def RetirarSaldo(self, monto):
         #aqui va el codigo
         self.__saldo=self.__saldo-monto
         
         
         
    __method__ = "DarInteresMensual"
    __parameter__ = "ninguno"
    __return__ = "valor del interes mensual"
    __description__ = "metodo que retorna el valor del interes mensual"
    
    def DarInteresMensual (self):
         #aqui va el codigo
         return self.__interesMensual
         
         
      
   