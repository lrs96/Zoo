from Animal import *
class Pessoa:
    def __init__(self):
        self.__Nome = None
        self.__Sexo = None
        self.__Idade = None

    @property
    def Nome(self):
        return self.__Nome
    @Nome.setter
    def Nome(self,nome):
        self.__Nome = nome
    @property
    def Sexo(self):
        return self.__Sexo
    @Sexo.setter
    def Sexo(self,sexo):
        self.__Sexo = sexo
    @property
    def Idade(self):
        return self.__Idade 
    @Idade.setter
    def Idade(self,idade):
        self.__Idade = idade

class Visitante(Pessoa):
    def __init__(self):
        Pessoa.__init__(self)
        self.__Passe_Visitante = None
    
    @property
    def Passe_Visitante(self):
        return self.__Passe_Visitante
    @Passe_Visitante.setter
    def Passe_Visitante(self,nomero):
        self.__Passe_Visitante = nomero
    def Faz_Carrinho(self,pessoa,animal):
        return 'O visitante {} esta Acariciando o Animal {}'.format(self.__Nome,self.__Nome)
class Funcionario(Pessoa):
    def __init__(self):
        Pessoa.__init__(self):
        self.__Numero_Funcionario = None

    @property
    def Numero_Funcionario(self):
        return self.__Numero_Funcionario
    @Numero_Funcionario.setter
    def Numero_Funcionario(slef,numero):
        self.__Numero_Funcionario = numero

    def Alimenta_Animal(self,Numero_Funcionario,animal):
        return 'O Funcionario {} Com o Numero {} Ta Alimentado o Animal {}'.format(self.__Nome,self.__Numero_Funcionario,self.__Nome)






pessoa = Pessoa()
pessoa.Nome = 'rENATO'
pessoa.Idade = 22
pessoa.Sexo = 'Mascolino'

print(pessoa.Nome)
print(pessoa.Idade)
print(pessoa.Sexo)
