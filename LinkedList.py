# -*- conding:utf-8 -*-
from Node import Node
class LinkedList:
    def __init__(self):
        self.first=None
        self.lenght=0

    def add(self, value):
        
        #Se agrega al principio si no existe elemento en el primer nodo.
        if (not self.first):
            self.first= Node(value)
            return True
            
        #Se agrega al final    
        current= self.first
        while(current.next):
            current=current.next
        current.next= Node(value)
        self.lenght+= 1
        return True

    def remove(self, position):
        #Se comprueba que position sea un entero.
        if not isinstance(position, int):
            print("Capablanca")
            return False
        #Se comprueba que position sea mayor que cero.
        if (position<0):
            print("Capablanca 2")
            return False
        #Si el nodo que se desea eleminar es el primero.
        current = self.first
        if (position == 0):
            self.first= current.next
            current=None
            self.lenght+=-1
            return True
        #Se inicia un contador para buscar el nodo que se desea eliminar.
        count=1
        
        while(current.next):
            
            if(count==position):
                
                before=current
                current = current.next
                before.next=current.next
                current= None
                self.lenght+=-1
                return True
            count=count + 1
            current=current.next
        
        #Se imprime un error si el Nodo no existe.
        if (current.next==None):
            print("Error, no existe Nodo")
            return False


    def printLL(self):
        current= self.first
        while(current):
            print(current.value)
            current=current.next
