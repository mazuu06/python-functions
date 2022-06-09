# ***************************************** Fnctions  *****************************************
# def myFun(a, b=50):             # here b=50is an default argument
#     print("x: ", a)
#     print("y: ", b)
 

# a = 25
# myFun(a)

# ***************************************** Keyword arguments  *****************************************
# Variable length keyword arguments

# def myFun(**kwargs):
#     for key, value in kwargs.items():
#         print("%s == %s" % (key, value))
 
# myFun(first="I'm", mid='learning', last='Python')

# # Variable length non-keywords argument
# def myFun(*argv):
#     for arg in argv:
#         print(arg)
 
# myFun('Hello', 'Welcome', 'to', 'Python')

# ***************************************** Docstring *****************************************

# def evenOdd(x):
#     """The first Comment in triple qouts after the function is called known as Document string."""
     
#     if (x % 2 == 0):
#         print("even")
#     else:
#         print("odd")
 
# print(evenOdd.__doc__)

# ***************************************** Docstring *****************************************

# def square_value(num):
#     return num**2
  
# output = square_value(2)
# ***************************************** Pass by Reference *****************************************
# def myFun(x):
#     x[-2] = 20

# lst = [10, 11, 12, 13, 14, 15]
# myFun(lst)
# print(lst)

# ***************************************** Anonymous functions *****************************************
# def cube(x): return x*x*x
 
# cube_v2 = lambda x : x*x*x
 
# print(cube(7))
# print(cube_v2(7))

# ***************************************** Yield statement, Generator-Function *****************************************
# def nextSquare():
#     i = 1

#     while True:
#         yield i*i                
#         i += 1  

# for num in nextSquare():
#     if num > 100:
#          break    
#     print(num)

# *****************************************Global, Local variables  *****************************************
# def f():
#     print("outer Function", str)
#     def n():
#         print("Inner Function", str)
#     x = 10
#     print("Inner Fun: ", x)
#     n()
    
# str = "I am learning python"
# f()
# # print(x)            Return an error because x is an local variable
# print("Outside Function", str)

# ***************************************** initialized *****************************************
# def sum():
#     x = 45
#     y = 85
#     global z        # z is a global variable.

#     z = x+y
#     return x+y

# print(sum())
# print(z)

# ***************************************** First Class functions *****************************************
# def create_adder(x):
#     def adder(y):
#         return x+y
  
#     return adder
  
# add_15 = create_adder(15)
  
# print (add_15(10))
# ***************************************** Nested functions *****************************************
# def outerFunction(text):
#     print("I am in outer function")
#     def innerFunction():
#         print("I am in inner function")
#         print(text)
 
#     innerFunction()
 
# outerFunction('Hey!')

# ***************************************** Closures *****************************************  
# def outerFunction(text):
#     print("I'm in outer function")
 
#     def innerFunction():
#         print("I'm in inner function")
#         print(text)

#     return innerFunction 

# myFunction = outerFunction('Hey!')
# myFunction()

# ***************************************** Decorators *****************************************  
# def decor1(func):
#     def inner():
#         x = func()
#         return x * x
#     return inner
 
# def decor(func):
#     def inner():
#         x = func()
#         return 2 * x
#     return inner
 
# @decor1
# @decor
# def num():
#     return 10
 
# print(num())

# ***************************************** Decorators with parameters *****************************************  
# def decorator(*args, **kwargs):
#     print("Inside decorator")
     
#     def inner(func):

#         print("Inside inner function")
#         print("I like", args[0], "and", kwargs['language'])
         
#         func()
  
#     return inner
 
# @decorator("python", language="php")
# def my_func():
#     print("Inside actual function")

# ***************************************** recursive program ***************************************** 

# def facto(num):
#     if num == 1:
#         return 1
#     else:
#         return num * facto(num-1)
         
 
# print(facto(12))
# print(facto(9))



