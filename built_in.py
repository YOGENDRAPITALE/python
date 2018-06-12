								#Built in Functions
								
import math

print("lets do some Maths")
print("2+2=",2+2)
print("2+2*2=",2+2*2)
print("2+2/2=",2+2/2)
print("2-2=",2-2)
print("2/2*2=",2/2*2)
print("-2+2=",-2+2)
print (3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

print ("Is it true that 3 + 2 < 5 - 7?")

print (3 + 2 < 5 - 7)
print ("What is 3 + 2?", 3 + 2)

print ("How about some more.")
print ("Is it greater?", 5 > - 2)
print( "Is it greater or equal?", 5 >= - 2)
print ("Is it less or equal?", 5 <= -2)
s=((float)(2+1.5))
print(s)

#Raise Too
a=2**5;
print(a)

#Power 
b=pow(2,5)
print(b)

#inbuilt python functions

print(dir(__builtins__))
print('Absolute value :',abs(15.2222))
print("Length :",len("Hello"))
print("Square root :",math.sqrt(9))


#Numbers
age=[50,24,38,65,59]
print(age)
print("Minimum :",min(age))
print("Maximum :",max(age))
print(tuple(age))
print(sorted(age))

#String
name=["Sam","Tan","Yogi"]
print(name)
print(name[2])
new=name.append("Lee")
print(name)

name.extend(age)
print(name)

name.remove("Lee")
print(name)


#Slicing
print(age[2:])
print(name[0:1:1])