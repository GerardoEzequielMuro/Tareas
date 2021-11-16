class Triangulo:
    
    def __init__(self,lado1=None,lado2=None,lado3=None):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    
    def lado_mayor(self):
        print(max(self.lado1,self.lado2,self.lado3))
        
    
    
    def tipo(self):
        if self.lado1 == self.lado2 and self.lado2 == self.lado3:
            print("Es un triangulo equilátero")
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3:
            print("Es un triangulo isoceles")    
        else:
            print("Es un triangulo escaleno")    
      
    
        

#########################
triangulo1 = Triangulo(122,11,12)
triangulo1.lado_mayor()
triangulo1.tipo()
       
        
        
            
        
