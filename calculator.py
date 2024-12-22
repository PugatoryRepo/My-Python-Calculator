#Come back to this program!
#import math 
import string

class Arithmetic_Cal:
    def __init__(self, num_1,num_2):
        self._num1=num_1
        self._num2=num_2

    def multiple(self):
        return self._num1*self._num2
    
    def addition(self):
        return self._num1+self._num2
    
    def subtraction(self):
        return self._num1-self._num2
    
    def division(self):
        if ZeroDivisionError:
            return "Divsion by zero"
        return self._num1/self._num2
    
    def modulo(self):
       if ZeroDivisionError:
            return "Divsion by zero"
       return self._num1%self._num2
    
    def double_slash_division(self):
        if ZeroDivisionError:
            return "Divsion by zero"
        return self._num1//self._num2

    def __init__(self,num):
        self._num=num
        
    def exponental(self):
        return self._num*self._num
    
    def is_square_root(self):
        expon=self.exponental()
        if expon//self._num==self._num and expon%self._num==0:
            return True
        return False
    
    def is_square_root(self):
        expon=self.exponental()
        return expon/self._num
    
    def abs_value(self):
        if self._num<0:
            return -self._num
        return self._num
    def ceiling(self,num):
        
        return round(num,1)
    

class User:
   def __init__(self,user):
       self._user=user
       self._str=""

   def error_handling(self):
       
        weird_sym='''"'?,.:;|&$!~\`'''
        if self._user=="":
            return ""
       
        else:
            self._str+=self._user[0]
            return self._str+self.error_handling(self._user[1:])


        
   def pemdas(self, user):
       return self.pemdas_helper(self,user,[])
   
   def pemdas_helper(self,user, lol):
       trigger=False
       i=1
       if self._user=="":
           return []
       else:
           if self._user[0].isnumeric() and  self._user[2].isnumeric() and trigger==False:
               lol.append([self._user[0:3]])
               return lol+self.pemdas_helper(self._user[3:],lol)
           
           if self._user[0] in "([{" or trigger==True:
               trigger=True

               if self._user[i] in ")]}" and i==1:
                   return "Error: Invalid Operation"
               
               if self._user [i] not in ")]}":
                   i+=1

               if self._user [i] in ")]}" and i!=1:
                   lol.append([self._user[0:i+1]])
                   trigger=False
                   return lol+self.pemdas_helper(self._user[i+1:],lol)
                     
              
               
               


def main():
    print("Welcome to my calculator")
    text=input("What you will do?")
    user=User(text)
    print(user.error_handling())

    
    
    pass

    
    



    
   
main()





    
