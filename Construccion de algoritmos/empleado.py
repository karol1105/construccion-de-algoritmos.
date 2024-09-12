__author__ = "Karol Isabella Cabrera"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "karol.cabrerap@campusucc.edu.co"

from Fecha import Fecha

class empleado:
    # Aqui inicia la declaracion de la clase
    
    """#_______________________________________________________________
    # atributos
    _________________________________________________________________#"""
    
    nombre  = ""
    apellido = ""
    salario = 0
    
    """#_______________________________________________________________
    # 1 = Masculino, 2 = femenino
    _________________________________________________________________#"""
    
    sexo = 0
    
    """#_______________________________________________________________
    # asociacion
    _________________________________________________________________#"""
   
    fechaIngreso = Fecha()
    fechaNacimiento = Fecha()
    
     
    """#_______________________________________________________________
     # metodos
    _________________________________________________________________#"""
    
    #este metodo retorma el nombre del empleado
    
    def DarNombre(self):
        #aqui va mi codigo
        return self.nombre
    

    
    __method__ = "cambiarSalario"
    __parameter__ = "nuevoSalario"
    __return__ = "salario"
    __description__ = "metodo que actualiza el salario del empleado"
    
    def CambiarSalario(self, nuevoSalario):
        #aqui va mi codigo
        self.salario = nuevoSalario



    __method__ = "DarSalario"
    __parameter__ = "ninguno"
    __return__ = "salario"
    __description__ = "metodo que muestra el salario del empleado"
    
    #retorma el salario del empleado
    def DarSalario(self):
        #aqui va mi codigo
        return self.salario
    
    

    __method__ = "ConsulatarFechaIngreso"
    __parameter__ = "ninguno"
    __return__ = "FechaIngreso"
    __description__ = "muestra la fecha de ingreso del empleado"

    def ConsultarFechaIngreso(self):
        return self.fechaIngreso.DarFecha()
    


    __method__ = "calcularSalarioAnual"
    __parameter__ = "ninguno"
    __return__ = "salario anual"
    __description__ = "muestra el salario anual del empleado"

    def calcularSalarioAnual (self):
        # aqui va mi codigo
        # forma 1 
        # total= self.salario*12
        # return total
        # forma 2 
        return self.salario*12

        
    
    __method__ = "CalcularImpuestoSalarioAnual"
    __parameter__ = "ninguno"
    __return__ = "impuesto de salario anual"
    __description__ = "muestra el impuesto del salario anual del empleado"

    def CalcularImpuestoSalarioAnual(self):
        # aqui inicia mi codigo
        # forma 1
        # salarioAnual=self.CalcularSalarioAnual()
        # ImpuestoAnual=salarioAnual*0,19
        # return impuestoAnual
        # Forma 2 
        return self.CalcularSalarioAnual()*0,19



    __method__ = "calcular impuesto salario mensual"
    __parameter__ = "ninguno"
    __return__ = "impuesto de salario mensual"
    __description__ = "muestra el impuesto del salario mensual del empleado"

    def CalcularImpuestoSalarioMensual(self):
         return self.DarSalario()*0,19







    

    
    


    

    


        
        
