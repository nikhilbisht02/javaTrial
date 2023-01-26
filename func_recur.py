## function and recursion

# def func1(name):
#     c ="hello ,"+name
#     return c 
# a = func1("nikhil") 
# print(a)
    
## ques : sum progran
# num1 = int(input("enter a number1\n"))
# num2= int(input("enter a number2\n"))
# def mysum(a,b):
#     c = a +b 
#     return c 
# s = mysum(num1,num2) 
# print("sum is",s)

##ques: default parameter value
   

# def mysum(a=0,b=0):# by default the values are zero
#     c = a +b 
#     return c 
# s = mysum() #here we have not assign any values to a and b in mysum() calling default function parameter value
# print("sum is",s)

#ques: factorial using recursion

# num1=int(input("enter a number to get its factorial\n"))
# def factorial(n):
#     fact =1
#     for i in range(n):
#         fact *=i+1
#     return fact
# print(factorial(num1))


# def factorial(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         return n*factorial(n-1)

# print(factorial(5))


#                              practice set

# num1 = int(input("enter num1"))
# num2 = int(input("enter num2"))
# num3 = int(input("enter num3"))

# def compare_numbers(num1,num2,num3):
#     if num1>num2:
#         if num1>num3:
#             print("num1 is greater")
#         else:
#             print("num3 is greater")
#     else:
#         if num2>num3:
#             print("num2 is greater")
#         else:
#             print("num3 is greater")
# print(compare_numbers(2,3,0))
  


# def farh(cel="non
#     farheneit= (cel*(9/5))+32
#     return farheneit
# a=farh(0)  
# b=farh(100)  
# print(" 0 celsius  to fahreneit   is "+str(a))
# print("100 celsius  to fahreneit   is "+str(b))

# n=5
# sum(n) =n+sum(n-1)


# def add(n):
#     if n==1:  
#      return 1
#     else:
#      return n +add(n-1)
# a=  add(5)  
# print(a)   


    

# n= int(input("Enter the value of n is "))
# def sum(n):
#     if n==1:
#         return 1
#     else:
#         return n+sum(n-1)  
# print(sum(n))   

# patterns
# num=6
# for i in range(num,0,-1):
#     print("*"*i)
    
# num=6
# for i in range(num):
#     print("*"*(num-i))
 


   

    


        
    
    


 




