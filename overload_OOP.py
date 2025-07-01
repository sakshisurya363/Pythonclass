class book:
    def __init__(self,name,page):
        self.name=name
        self.page=page
        
    def __add__(self,other):
        return self.page+other.page 
    
    def __sub__(self,other):
        return self.page-other.page   
    
    def __mul__(self,other):
        return self.page*other.page 
    
    def __mod__(self,other):
        return self.page%other.page   
    
    #def __div__(self,other):     #TypeError: unsupported operand type(s) for /: 'book' and 'book'
        #return self.page/other.page   
    
    def __floordiv__(self,other):
        return self.page//other.page  
    
    def __equal__(self,other):
        return self.page==other.page 
    
    def __notequal__(self,other):
        return self.page!=other.page  
     
    def __gt__(self,other):
        return self.page>other.page 
     
    def __lt__(self,other):
        return self.page<other.page 
    
    #def __gte__(self,other):           #TypeError: '>=' not supported between instances of 'book' and 'book'
        #return self.page>=other.page 
    
    #def __lte__(self,other):
        #return self.page<=other.page   # TypeError: '<=' not supported between instances of 'book' and 'book'
    
b1=book("The End Is Beginning",250)
b2=book("Rich Dad Poor Dad",25)

print(b1+b2)
print(b1-b2)     
print(b1*b2)   
print(b1%b2)
#print(b1/b2)
print(b1//b2)
print(b1==b2)
print(b1!=b2)
print(b1>b2)
print(b1<b2)
#print(b1>=b2)
#print(b1<=b2)

        