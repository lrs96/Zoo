'''Nessa Classes sera implemantado o conceito de Classes alinhadas
como o objetivo de cadastar varios animais '''
class Animal:
    def __init__(self):
        self.__Especie = None
        self.__Tipo = None
        self.__Tamanho = None
        self.__Alimento = None
        self.__SubEspecie = None
        self.__Ordem = None

    @property
    def Especie(self):
        return self.__Especie
    @Especie.setter
    def Especie(self,nome):
        self.__Especie = nome
    @property
    def Tipo(self):
        return self.__Tipo
    @Tipo.setter
    def Tipo(self,tipo):
        self.__Tipo = tipo
    @property
    def Tamanho(self):
        return self.__Tamanho
    @Tamanho.setter
    def Tamanho(self,tamanho):
        self.__Tamanho = tamanho
    @property
    def Alimento(self):
        return self.__Alimento
    @Alimento.setter
    def Alimento(self,alimento):
        self.__Alimento = alimento
    @property
    def SubEspecie(self):
        return self.__SubEspecie
    @SubEspecie.setter
    def SubEspecie(self,subespecie):
        self.__SubEspecie = subespecie
    @property
    def Ordem(self):
        return self.__Ordem
    @Ordem.setter
    def Ordem(self,ordem):
        self.__Ordem = ordem
        
class Terrestre(Animal):
    def __init__(self):
        Animal.__init__(self)
        self.__Terreno = None
    
    @property
    def Terreno(self):
        return self.__Terreno
    @Terreno.setter
    def Terreno(self,terreno):
        self.__Terreno = terreno
        
    
class Marinho(Animal):
    def __init__(self):
        Animal.__init__(self)
        self.__Nivel_Dagua = None
    

    @property
    def Nivel_Dagua(self):
        return self.__Nivel_Dagua
    @Nivel_Dagua.setter
    def Nivel_Dagua(self,nivel):
        self.__Nivel_Dagua = nivel

    
class Aereo(Animal):
    def __init__(self):
        Animal.__init__(self)
        self.__Altitude = None
    

    @property
    def Altitude(self):
        return self.__Altitude
    @Altitude.setter
    def Altitude(self,altitude):
        self.__Altitude = altitude
    

class Anfibio(Marinho,Terrestre):
    def __init__(self):
        Marinho.__init__(self)
        Terrestre.__init__(self)
    

'''
lala = Anfibio()
lala.Especie = 'Salamandra'
lala.Terreno = 'Florestra Tropical'
lala.Nivel_Dagua = '100 Leguas'

print(lala.Especie)
print(lala.Terreno)
print(lala.Nivel_Dagua)


montro = Marinho()
montro.Especie = "Dragao Dagua"
montro.Nivel_Dagua = '2000 Leguas'
meu_animal = Animal()
meu_animal.Especie = 'Cachorro'
meu_animal.Tipo = 'Terrestre'
meu_animal.Tamanho = '120cm'

print(meu_animal.Especie)
print(meu_animal.Tipo)
print(meu_animal.Tamanho)
print(montro.Especie)
print(montro.Nivel_Dagua)
print('A Especie é {} do Tipo {} de Tamanho {}'.format(meu_animal.Especie,meu_animal.Tipo,meu_animal.Tamanho))'''