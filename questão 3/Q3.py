#Maria Luiza Sousa Martins Americo
class Triangulo:
    def __init__ (self, A ,B ,C): #Define os lados, o perimetro e a area
        self.ladoa = A
        self.ladob = B
        self.ladoc = C
        self.perim = A + B + C
        self.area = ((self.perim/2) * ((self.perim/2) - A) * ((self.perim/2) - B) * ((self.perim/2) - C) )**(1/2)

    def eValido (self): #valida se realmente é um triangulo
        if self.ladoa + self.ladob <= self.ladoc or self.ladoa + self.ladoc <= self.ladob or self.ladob + self.ladoc <= self.ladoa:
            print("Esses valores não formam um triângulo.")
       
        else:
            print("Esses valores formam um triângulo.")
    
    def tipo (self): #Define o tipo do triângulo caso seja um triângulo
        if self.ladoa + self.ladob <= self.ladoc or self.ladoa + self.ladoc <= self.ladob or self.ladob + self.ladoc <= self.ladoa:
            print ("Não é um triângulo.")
       
        else:    
            if self.ladoa == self.ladob and self.ladoa == self.ladoc:
                print ("Triângulo Equilátero")
       
            if self.ladoa == self.ladob and self.ladoa != self.ladoc or self.ladob == self.ladoc and self.ladob != self.ladoa or self.ladoa == self.ladoc and self.ladoa != self.ladob :
                print ("Triângulo Isósceles")
            
            if self.ladoa != self.ladob and self.ladoa !=self.ladoc and self.ladob != self.ladoc:               
                print ("Triângulo Escaleno")

    def perimetro (self): #Calcula o perimetro do triângulo, caso seja um.
        if self.ladoa + self.ladob <= self.ladoc or self.ladoa + self.ladoc <= self.ladob or self.ladob + self.ladoc <= self.ladoa:
            print ("O perimetro do triângulo não pode ser calculado, pois esses valores não formam um triângulo. ")
            
        else:
            print ("O perimetro é {}.".format(self.perim))
            
    def areaA (self): #Calcula a área do triângulo caso seja um.
        if self.ladoa + self.ladob <= self.ladoc or self.ladoa + self.ladoc <= self.ladob or self.ladob + self.ladoc <= self.ladoa:
            print ("A area do triângulo não pode ser calculada, pois esses valores não formam um triângulo. ")
            
        else:
            print("A area é {}".format(self.area))
    

#testa 
if __name__ =='__main__':
    print("Teste 1")
    meutriangulo = Triangulo (3,4,5)
    meutriangulo.eValido()
    meutriangulo.tipo()
    meutriangulo.perimetro()
    meutriangulo.areaA()
    
if __name__ =='__main__':
    print("Teste 2")
    meutriangulo = Triangulo (6,8,10)
    meutriangulo.eValido()
    meutriangulo.tipo()
    meutriangulo.perimetro()
    meutriangulo.areaA()
    
if __name__ =='__main__':
    print("Teste 3")
    meutriangulo = Triangulo (2,4,25)
    meutriangulo.eValido()
    meutriangulo.tipo()
    meutriangulo.perimetro()
    meutriangulo.areaA()
    
if __name__ =='__main__':
    print("Teste 4")
    meutriangulo = Triangulo (2,2,3)
    meutriangulo.eValido()
    meutriangulo.tipo()
    meutriangulo.perimetro()
    meutriangulo.areaA()
    
if __name__ =='__main__':
    print("Teste 5")
    meutriangulo = Triangulo (4,4,4)
    meutriangulo.eValido()
    meutriangulo.tipo()
    meutriangulo.perimetro()
    meutriangulo.areaA()


    