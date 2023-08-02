#Maria Luiza Sousa Martins Americo
#Classe em Python é uma forma de organizar dados e "metodos" juntos.

class Ponto2D: #Define a classe (Ponto2D)
    def __init__ (self, x1, x2, y1, y2):
        self.x1 = x1 #Abcissa do ponto 1
        self.x2 = x2 #Abcissa do ponto 2
        self.y1 = y1 #Ordenada do ponto 1
        self.y2 = y2 #Ordenada do ponto 2
        
    def informações (self): #Metodo usado para definir as abcissas e ordenadas dos pontos
        print ("Ponto 1 = ({},{})".format(self.x1,self.y1))
        print ("Ponto 2 = ({}, {})".format(self.x2, self.y2))
    
    def distância (self): #Metodo usado para calcular a distancia dos dois pontos
        d = ((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)**(1/2)
        print ("A distância de um ponto ao outro é de {}.".format(d))
        
#Teste 1  
if __name__ == "__main__": 
    pontos = Ponto2D (1,4,5,6)
    pontos.informações()
    pontos.distância()
    