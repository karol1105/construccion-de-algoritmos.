__author__ = "Karol Isabella Cabrera"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "karol.cabrerap@campusucc.edu.co"

   
from cuentaCorriente import CuentaCorriente
from cuentaAhorros import CuentaAhorros
from CDT import CDT

class simuladorBancario:
    # Aqui inicia la declaracion de la clase
    
    """#_______________________________________________________________
    
    # Atributos
    _________________________________________________________________#"""


    __nombre  = ""
    __cedula = ""
    __MesActual = 0
    
    """#_______________________________________________________________
    
    # Asociaciones
    _________________________________________________________________#"""
    

    __CuentaCorriente = CuentaCorriente()
    __CuentaAhorros = CuentaAhorros()
    __CDT = CDT()

 
    """#_______________________________________________________________
    
    # Metodos
    _________________________________________________________________#"""


    __method__ = "DepositarCuentaCorriente"
    __parameter__ = "monto"
    __return__ = "ninguno"
    __description__ = "metodo que permite depositar en la cuenta corriente"

    def DepositarCuentaCorriente(self, monto):
       self.__CuentaCorriente.consignarSaldo(monto)


    
    __method__ = "CalcularSaldoTotal"
    __parameter__ = "ninguno"
    __return__ = "saldo total de todas las cuentas"
    __description__ = "metodo que permite calcular el saldo total de todas las cuentas"

    def CalcularSaldoTotal(self):
        # Aqui inicia mi codigo
        # Metodo 1
        #total = self.__cuenta_corriente.DarSaldo()+self.__CuentaAhorros.DarSaldo()
        # return total
        # Metodo 2 
        return self.__CuentaCorriente.DarSaldo()+self.__CuentaAhorros.DarSaldo()
    

    
    __method__ = "PasarAhorroACorriente"
    __parameter__ = "ninguno"
    __return__ = "ninguno"
    __description__ = "metodo que permite pasar saldo de la cuenta de ahorros a la cuenta corriente"

    def PasarAhorrosACorriente(self):
        #aqui va mi codigo
        saldoAhorros = self.__CuentaAhorros.DarSaldo()
        self.__CuentaAhorros.retirarSaldo(saldoAhorros)
        self.__CuentaCorriente.ConsignarSaldo(saldoAhorros)



    __method__ = "Ahorrar"
    __parameter__ = "monto"
    __return__ = "ninguno"
    __description__ = "metodo que permite pasar saldo de la cuenta corriente a la cuenta de ahorros"

    def ahorrar(self, monto):
        #aqui va mi codigo
        self.__CuentaCorriente.RetirarSaldo(monto)
        self.__CuentaAhorros.ConsignarSaldo(monto)



    __method__ = "RetirararAhorro"
    __parameter__ = "monto"
    __return__ = "saldo"
    __description__ = "metodo que permite retirar un valor de la cuenta ahorros"

    def RetirarAhorro(self, monto):
        # aqui va mi codigo
        self.__CuentaAhorros.DarSaldo()-monto

    
    
    __method__ = "DarSaldoCorriente"
    __parameter__ = "ninguno"
    __return__ = "saldo de la cuenta corriente"
    __description__ = "metodo que  retorna el saldo que hay en la cuenta corriente"

    def DarSaldoCorriente(self):
        # aqui va mi codigo
        return self.__CuentaCorriente.DarSaldo()
    


    __method__ = "retirarTodo"
    __parameter__ = "ninguno"
    __return__ = "ninguno"
    __description__ = "metodo que permite retirar todo el dinero que hay en la cuenta corriente y en la de ahorros"

    def retirarTodo(self, monto):
        #aqui va mi codigo
        saldoAhorros= self.__CuentaAhorros.DarSaldo()
        saldoCorriente= self.__CuentaCorriente.DarSaldo()
        self.__CuentaCorriente.RetirarSaldo(saldoCorriente)
        self.__CuentaAhorros.RetirarSaldo(saldoAhorros)
    

    __method__ = "duplicarAhorro"
    __parameter__ = "ninguno"
    __return__ = "saldo duplicado"
    __description__ = "metodo que permite duplicar la cantidad de dinero que hay en la cuanta de ahorros."

    def duplicarAhorro(self):
        #aqui va mi codigo
        return self.__CuentaAhorros.DarSaldo()*2


    


  











        

       
    


    saldoCuentaCorriente = cuenta_corriente()
    saldoCuentaAhorros = cuenta_ahorros()
    saldoCDT = CDT()
    
    
    

    
    