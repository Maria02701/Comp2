#Maria Luiza Sousa Martins Americo
#Classe em Python é uma forma de organizar dados e "metodos" juntos.

class Funcionário: #Define a classe (Funcionário)
    def __init__(self, nome, cpf, departamento, salario, entrada, ativo):
        self.nome = nome 
        self.cpf = cpf
        self.departamento = departamento 
        self.salario = salario 
        self.entrada = entrada 
        self.ativo = ativo 
        
    def informações (self):
        print ("Nome: ",self.nome)
        print ("CPF: ", self.cpf)
        print("Departamento:", self.departamento)
        print ("Salário: ", self.salario)
        print ("Data de entrada:", self.entrada)
        
    def atividade (self): #Metodo usada para validar a situação cadastral do funcionário
        if self.ativo: #Se o valor for verdadeiro (True), o usuario está ativo.
            True
            print ("Usuario ativo")
            
        else: # Se o valor for falso (False), o usuário está inativo.
            print ("Usuario inativo / demitido")
    
    def aumento (self): #Metodo usado para aumentar o salário do usuário ativo.
        if self.ativo: #Se usuário estiver ativo, ele receberá um aumento de 15%.
            True
            novo = self.salario + (self.salario * 15 / 100)
            print ("seu novo salário é {}".format(novo))
        
        else: #Se o usuário estiver inativo, ele não recebrá ajuste salarial.
            print ("O usuário esta inativo, por isso não pode receber reajuste salarial.")
            
        
    def get_ativo (self): #Método usado para buscar a informação da atividade.
        return self.ativo
        
        
    def set_ativo (self, ativo):#Método usado para alterar a Situação Cadastral do Funcionário.
        self.ativo = ativo
        print ("Situação cadastral alterada!")
        
      
     #Método usado para resgatar as informações do funcionário
    def get_nome (self): 
        return self.nome 
        
    def get_cpf (self): 
        return self.cpf
    
    def get_departamento (self):
        return self.departamento
        
    def get_salario (self):
        return self.salario 
        
    def get_entrada (self):
        return self.cpf
    
    
    # Método usado para alterar informações do Funcionário    
      
    def set_nome (self, nome): 
        self.nome = nome 
        print ("Nome alterado com sucesso!")
    
    def set_cpf (self, cpf): 
        self.cpf = cpf
        print ("CPF alterado com sucesso")
    
    def set_departamento (self, departamento):
        self.departamento = departamento
        print ("Departamento alterado com sucesso")
    
    def set_salario (self, salario):
        self.salario = salario
        print ("Salário alterado com sucesso")
        
    def set_entrada (self, entrada):
        self.entrada = entrada
        print ("Data de entrada alterado com sucesso")
        
        
            

#Teste 
if __name__ == "__main__":
    pessoa1 = Funcionário ("João", "135.865.975-45", "Departamento Estrategico",1000, "02/02/2007", False)
    pessoa1.informações()
    pessoa1.atividade()
    print ("------------ // ------------")
    
    #Para aumento salarial
    pessoa1.aumento()
    print ("------------ // --------------")
   
    #Para alterar situação cadastral
    pessoa1.set_ativo(True)
    
    
    # Para alterar dados
    #nome
    pessoa1.set_nome("Jose")
    print(pessoa1.get_nome())
    
    #cpf
    pessoa1.set_cpf("123.579.974-45")
    print(pessoa1.get_cpf())
    
    #departamento
    pessoa1.set_departamento("Departamento de obras")
    print(pessoa1.get_departamento())
    
    #salario 
    pessoa1.set_salario(500)
    print(pessoa1.get_salario())
    
    #Data de entrada 
    pessoa1.set_entrada("05/09/2001")
    print(pessoa1.get_entrada())
    
    #Teste novo aumento
    pessoa1.aumento()
    
    
    
        
    
    
