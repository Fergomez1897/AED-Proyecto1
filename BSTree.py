# -*- conding:utf-8 -*-
from BstNode import BstNode
class Btree:
    def __init__(self):
        self.root=None
       


    def add(self,value):
        return self.addInner(value,self.root)

    def addInner(self,value,current):
        if not isinstance(current,BstNode):
            return False
        if(self.root == None):
            self.root = BstNode(value) 
            return True
        if(value<current):
                if (not current.left):
                    current.left= BstNode(value)
                    return True
                return self.addInner(value, current.left)
        
        if (value>current.value):
            if(not current.right):
                current.right= BstNode(value)
                return True
            return self.addInner(value, current.left)
        
        return False 
