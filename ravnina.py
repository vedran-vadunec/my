
from math import sqrt

class Tocka:
    """
    Opis ove klase
    2-dim tocke u ravnini
    """
    def __init__(self,x,y): # konstruktor
        self.x=x
        self.y=y
        
    def norm(self):
        return sqrt(self.x**2+self.y**2)
    
    def __repr__(self):
        return "Tocka ({0}, {1})".format(self.x,self.y)
    
class Vector(Tocka):
    """
    Opis ove klase
    """
    
    def __add__(self,b):
        x=self.x+b.x
        y=self.y+b.y
        return Vector(x,y)
    
    def __repr__(self):
        return "Vector ({0}, {1})".format(self.x,self.y)

    def norm(self):
        return sqrt( self.x**2 + self.y**2  )
    
    
    
    def __mul__(self,b):
        L1=[self.x,self.y]
        L2=[b.x,b.y]
        return 1
        

        #result=sum([i*j for (i, j) in zip(list1, list2)])
        
        