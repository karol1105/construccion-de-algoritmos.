__author__ = "Karol Isabella Cabrera"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "karol.cabrerap@campusucc.edu.co"



class CDT:
    # Aqui inicia la declaracion de la clase
    
    """#_______________________________________________________________
    
    # Atributos
    _________________________________________________________________#"""
  
    saldo = 0
    fecha_apertura = 0
    intereses = 0
    
    """#_______________________________________________________________
    
    # Asociacion
    _________________________________________________________________#"""
    
    __method__= "DarSaldo"
    __parameter__= "ninguno"
    __returns__ = "saldo"
    __descripcion__="metodo que regreswa el saldo del CDT"

    def DarSaldo(self):
        return self.saldo


    def InteresMensual(self):
        return self.InteresMensual