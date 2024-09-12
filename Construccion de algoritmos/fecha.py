__author__ = "Karol Isabella Cabrera"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "karol.cabrerap@campusucc.edu.co"


class Fecha:
    # Aqui inicia la declaracion de la clase
    
    """#_______________________________________________________________
    # atributos
    _________________________________________________________________#"""
    
    dia = 0
    mes = 0
    anio = 0

    """#_______________________________________________________________
    # metodos
    _________________________________________________________________#"""

    
    __method__ = "DarDia"
    __parameter__ = "ninguno"
    __return__ = "Dia"
    __description__ = "metodo que regresa el dia"

    def DarDia(self):
        return self.dia

    
    __method__ = "DarMes"
    __parameter__ = "ninguno"
    __return__ = "Mes"
    __description__ = "metodo que regresa el Mes"

    def DarMes(self):
        return self.mes

     
    __method__ = "DarAnio"
    __parameter__ = "ninguno"
    __return__ = "Anio"
    __description__ = "metodo que regresa el Anio"

    def DarAnio(self):
        return self.anio


    __method__ = "DarFecha"
    __parameter__ = "ninguno"
    __return__ = "Fecha"
    __description__ = "metodo que regresa la fecha digitada por el usuario"

    def DarFecha(self):
        return self.dia+'/'+self.mes+'/'+self.anio








    

