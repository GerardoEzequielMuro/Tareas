class Vehiculo():
    
    def __init__(self,nombre,color,ruedas):
        self.nombre = nombre
        self.color = color
        self.ruedas = ruedas
    
    
    
    def descripcion(self):
        print(f"El Nombre del vehiculo es: {self.nombre}, el color es: {self.color}, la cantidad de ruedas es {self.ruedas}")    
        
#######################################
#######################################

class Coche(Vehiculo):
    
    def __init__(self,nombre,color,ruedas,velocidad,cilindrada):
        super().__init__(nombre,color,ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        
    def descripcion(self):
        super().descripcion()
        print(f"La velocidad es: {self.velocidad}KM/H, La cilindrada es {self.cilindrada}cc ")
        


#######################################
#######################################

class Camioneta(Vehiculo):
    
    def __init__(self,nombre,color,ruedas, carga):
        super().__init__(nombre,color,ruedas) 
        self.carga = carga
        
    def descripcion(self):
        super().descripcion()
        print(f"La carga soportada es {self.carga}kg")
        
        
        
#######################################
#######################################

class Bicicleta(Vehiculo):
    
    def __init__(self,nombre,color,ruedas,tipo):
        super().__init__(nombre,color,ruedas)
        self.tipo = tipo
        
    def descripcion(self):
        super().descripcion()
        print(f"El tipo de bicicleta es {self.tipo}") 
    
    
    
#######################################
#######################################

class Motocicleta(Vehiculo):
    
    def __init__(self,nombre,color,ruedas,velocidad,cilindrada):
        super().__init__(nombre,color,ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    
    def descripcion(self):
        super().descripcion()
        print(f"La velocidad es {self.velocidad}km/h, la cilindrada es {self.cilindrada}cc") 
        
#######################################
#######################################


coche1 = Coche("Fiat 100","Rojo",4,50,4)
camioneta1 = Camioneta("Wolsbagen 200","Naranja",4,250)
bicicleta1 = Bicicleta("BMX 500","Azul",2,"Deportiva")
motocicleta1 = Motocicleta("Susuki 500","Verde",2,100,4)

lista_vehiculos = [coche1,camioneta1,bicicleta1,motocicleta1]

def catalogar():
    for x in lista_vehiculos:
        print("Este es un:",type(x).__name__,end="")
        print("")
        x.descripcion()
        
      
def catalogar_x_ruedas(nro):
    for x in lista_vehiculos:
        if nro == x.ruedas:
            print("Es un",type(x).__name__)


catalogar_x_ruedas(4)   
           
    
