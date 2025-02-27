# -*- coding: utf-8 -*-
"""python assignment 1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TWKRCnbLY4F7irLUUwsSKGPg8Ns_dZZI
"""



"""python assignment = 01

Name:Disha N M
  
Date :11/09/2024

1.a)variables in python

variables are the location or a name,that can able to store a data interms of int,float,string etc
ex:name="disha nm"

1.b)differnce between variable and constant?can we have constants in python

variables are the location or a name,that can able to store a data interms of int,float,string etc...

constant are the fixed value we can not alter that.there is no constant in python

2. Working with Different Data Types

   a) Create variables of the following types in Python:

      1. Integer
      2. Float
      3. String
      4. Boolean
"""

x=10
type(x)

y=3.14
type(y)

name="disha"
type(name)

a=True
type(a)

"""2.b)write a python script to display the type of each variable you created"""

var_int = 10
var_float = 3.14
var_string = "Hello World!"
var_list = [1,2,3,4,5]
var_dict = {'key1':'value1','key2':'value2'}
var_bool = True
print("Type of var_int:",type(var_int))
print("Type of var_float:",type(var_float))
print("Type of var_string:",type(var_string))
print("Type of var_list:",type(var_list))
print("Type of var_dict:",type(var_dict))
print("Type of var_bool:",type(var_bool))

"""3. Arithmetic Operators

a) Explain the following arithmetic operators with examples:

1.Addition (`+`)

2Subtraction (`-`)

3.Multiplication (``)

4.Division (`/`)

5.Floor Division (`//`)

6.Modulus (`%`)
  
7.Exponentiation (``)
"""

x=5
y=3
result =(x+y)
print("Addition:",result)

x=10
y=4
result = x-y
print("Substraction:",result)

x=6
y=7
result = x*y
print("Multiplication:",result)

x=20
y=6
result = x//y
print("Division:",result)

x=15
y=4
result = x%y
print("Modulus:",result)

x=2
y=3
result = x**y
print("Exponention:",result)

"""b) Write a Python script to calculate the area of a rectangle using variables `length` and `width` with values 5 and 10, respectively. Use the multiplication operator."""

length=5
width=10
area=length*width
print("The area of the rectangle is:",area)

"""4. Comparison and Logical Operators

a) Explain the following comparison operators with examples:

1.Equal to (`==`)

2.Not equal to (`!=`)

3.Greater than (`>`)

4.Less than (`<`)

5.Greater than or equal to (`>=`)
  
6.Less than or equal to (`<=`)

"""

a=5
b=5
result=a==b
print("Equal to:",result)

a=5
b=7
result=a!=b
print("Not Equal to:",result)

a=10
b=6
result=a>b
print("Greater than:",result)

a=5
b=9
result=a<b
print("Less than:",result)

a=4
b=4
result=a>=b
print("Greater than or equal to:",result)

a=4
b=8
result=a<=b
print("Less than or equal to:",result)

"""b) Using logical operators (`and`, `or`, `not`), write a Python script that checks if a number is positive and even."""

number=int(input("Enter a number:"))
if number>0 and number % 2 == 0:
  print("The number is positive and even:")
else:
  print("The number is either not positive or not even:")

"""5. Type Casting in Python
  
a) What is type casting? Explain the difference between implicit and explicit type casting with examples.

Type Casting is the method to convert the Python variable datatype into a certain data type in order to perform the required operation by users.

Implicit type casting

  Type Casting is the method to convert the Python variable datatype into a certain data type in order to perform the required operation by users.

  example

  a = 7
    
print(type(a))

Explicit type casting

 In this method, Python needs user involvement to convert the variable data type into the required data type.

 example
 a = 5
  
n = float(a)

print(n)
print(type(n))

b) Write a Python script that:


1.
Converts a float to an integer.

2.
Converts an integer to a string.
  
3.
Converts a string to a float.
"""

float_num = 3.14
int_num = int(float_num)
print("Float to integer:",int_num)

int_num=42
str_num=str(int_num)
print("integer to string:",str_num)

str_num="7.5"
float_num=float(str_num)
print("String to float:",float_num)

"""6.Mini Calculator

Write a Python script that asks the user to input two numbers and then:

1.
Adds the two numbers and prints the result.

2.
Subtracts the second number from the first and prints the result.

3.
Multiplies the two numbers and prints the result.

4.
Divides the first number by the second and prints the result (handle division by zero).
  
5.
Converts the sum of the numbers to a string and prints the type of the result.
"""

num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
sum_result = num1 + num2
print(f"The sum of {num1}and {num2}is{sum_result}")
substraction_result = num1-num2
print(f"The result of substracting {num2}from {num1}is{substraction_result}")
multiplication_result=num1*num2
print(f"The result multiplying of {num1}and {num2}is{multiplication_result}")
division_result=num1/num2
print (f"The result of dividing {num1}by{num2} {division_result}")
print("Error:Division by zero is not allowed.")
sum_as_str=str(sum_result)
print(f"The sum converted to a string is'{sum_as_str}'and its type is{type(sum_as_str)}")