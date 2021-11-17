class Tiempo:
    
    
    def __init__(self,hora=0,minuto=0,segundo=0):
        self.hora = hora
        self.minuto = minuto
        self. segundo = segundo
     
     
    def mostrar_tiempo(self):
        print(self.hora,":",self.minuto,":",self.segundo)
        
    
    def cambiar_tiempo(self):
        print(
        """
        Esta a punto de cambiar su Reloj
        """
        )   
        
        
        
        self.hora = input("Ingrese la Hora deseada: ")
        self.minuto = input("Ingrese los Minutos deseados: ") 
        self.segundos= input("Ingrese los Segundos deseados: ")           


hora = Tiempo()        
hora.cambiar_tiempo()
hora.mostrar_tiempo()
