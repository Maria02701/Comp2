#Maria Luiza Sousa Martins Americo
#Classe em Python é uma forma de organizar dados e "metodos" juntos.

class veiculo: #Define a classe (veiculo)
    
    def __init__(self, consumo, capacidade, distancia):
        self.consumo = consumo #Consumo do tanque
        self.combustivel = 10 #Quantidade atual de combustível
        self.capacidade_max = capacidade #Capacidade máxima do tanque 
        self.distancia = distancia #Possível distância que o veiculo percorrerá
    
    
    def pode_se_mover(self, distancia): # Verifica se existe a possibilidade de andar com a quantidade de combustivel no tanque
        consumo = distancia / self.consumo #Quanto devera ser gasto de gasolina na distancia
        return (self.combustivel>=consumo) 
    
    
    def mover (self, km): #Metodo usado para mover o carro, ele diminuino nivel de combustivel baseado no consumo do veiculo e diz se é possivel ou não andar.
        if (self.pode_se_mover(km)):
            self.distancia += km
            self.combustivel -= (km/self.consumo)
            print ("Seu carro está andando.")
        
        else:
            print ("Não há combustível suficiente para andar {}km".format(km))

    def getCombustivel (self): #Diz o nível atual de combustível no carro.
        print ("O nível atual de combustível é de {} litros.").format(self.combustivel)
    
    def tanque (self,litros): 
        if (self.combustivel + litros <= self.capacidade_max): #verifica se a quantidade de litros que se pretende abastecer cabe no tanque
           return litros

        else: #se não couber, completa o tanque
           return (self.capacidade_max - self.combustivel)
        
    def abastecer (self, quantidade): #Metodo usado para abastecer o carro, basicamente adiciona a quantidade de combustivel ao nivel atual de combustível
        abastecer = self.tanque(quantidade)
        self.combustivel += abastecer
        print("Você abasteceu com {} litros de combustível. Nível atual de {} litros".format(abastecer, self.combustivel))
        
        
    def imprimir (self): # Informa alguns dados do veículo 
       print ('-------Informacões do veículo-------')
       print ('Seu veículo estava com {} litros de gasolina.'.format(self.combustivel))
       print ('O consumo do seu veiculo é de {} km/litro.'.format(self.consumo))
       print ('A distância que o veículo pretende percorrer é de {} km.'.format(self.distancia))
        
    
#Testes     
if __name__=='__main__':
    print ("Teste 1")
    meuCarro = veiculo (1,15,18) #(Consumo do tanque, capacidade do tanque e distância que pretende percorrer)
    meuCarro.imprimir()
    meuCarro.abastecer(7) #(Valor a ser adicionado no tanque)
    meuCarro.mover(18) #Define se o veiculo pode ou não percorrer a distancia pretendida (Distancia a ser percorrida)
    print ("  ")
    
    
if __name__=='__main__':
    print ("Teste 2")
    meuCarro2 = veiculo (2,10,16)
    meuCarro2.imprimir()
    meuCarro2.abastecer(8)
    meuCarro2.mover(16)
            
    
    
    