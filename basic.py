# Write a program to add two integer numbers
# m=int(input('enter number1:'))
# n=int(input('enter number2:'))
# k=m+n
# print(k)

# #Write a program to add three integer numbers
# m=int(input('enter number1:'))
# n=int(input('enter number2:'))
# k=int(input('enter number3:'))
# sum=m+n+k
# print(sum)

# #Write a program to print all sum combination of three numbers by taking two numbers at a time
# a=int(input('enter a number:'))
# b=int(input('enter a number:'))
# c=int(input('enter a number:'))
# sum1=a+b
# sum2=a+c
# sum3=b+c
# print('a+b',sum1)
# print('a+c',sum2)
# print('b+c',sum3)

# #Write a program to convert celsius to fahrenheit
# celsius=int(input('enter temparature:'))
# fahrenheit = ((celsius*9)/5)+32
# print(fahrenheit)



# #Write a program to convert fahrenheit to celsius
# fahrenheit=int(input('enter temparature:'))
# Celsius = ((fahrenheit-32)*5)/9;
# print(Celsius)

# #Write a program to find the perimeter of the square
# side=float(input('enter size of a perimeter of side:')) 
# perimeter = 4*side
# print('perimeter',perimeter)

# #Write a program to find the area of the circle
# r=int(input('enter radius: '))
# pi=3.142
# area = pi*r*r
# print('the area of the circle',area)

# #Write a program to calculate total surface area of a cylinder
# radius=int(input('enter number:'))
# height=int(input('enter number:'))
# pi=3.142
# surface=2*pi*radius*(radius+height)
# print(f'{surface:.4f}')

# #Write a program to find the perimeter of the rectangle

# length=int(input('enter length of a rectangle:'))
# width=int(input('enter width of a rectangle:'))
# perimeter=2*(length+width)
# print('perimeter of a rectangle',perimeter)

# #Write a program to convert Dollars to rupees
# dollor=int(input('enter amount:'))
# rupees=dollor*61.06
# print('the conversion of dollor into rupees:',rupees)




# ASSIGNMENT 2
#Check if a given number is even number or odd number.
# num=int(input('enter a number:'))
# if num%2==0:
#     print('the number is even:')
# else:
#     print("the number is odd:")

# # Determine whether the given number is multiple of 5 or not.
# num=int(input('enter a number:'))
# if num%5==0:
#     print('yes it is divisible by 5')
# else:
#     print('no it is no divisible by 5')
# # 
# # Determine whether the given number is multiple of 10 or not.
# num=int(input('enter the number:')) 
# if num%10==0:
#     print('it is divisible by 10')
# else:
#     print('it is not divisible by 10')    


# #Write a program to check whether the number is multiple of both 5 and 3.
# num=int(input('enter a number:'))
# if num%5==0 and num%3==0:
#     print('it is divisible by 5 and 3')
# else:
#     print('it is not divisible by 5 and 3')

# #Write a program to check whether the number is multiple of 5, 3 and 7.
# num=int(input('enter a number:'))
# if num%5==0 and num%3==0 and num%7==0:
#     print('it is divisible by 5,3 and 7')
# else:
#     print('it is not divisible by 5,3 and 7')

# #Write a program to check whether the given number is two digit number or not.
# num=int(input('enter a number:'))
# if 10 <=num <=99:
#     print('it is a two digit number')
# else:
#     print('it is not a two digit number')

# #Write a program to check whether the given number is three digit number or not.
# num=int(input('enter a number:'))
# if 111 <=num <=999:
#     print('the given number is in three digit')
# else:
#     print('the given number is not in three digit')  

# #Check if a given number is three digit number and also it is a multiple for 10.
# num=int(input('enter a number:'))
# if 111 <=num <=999 and num%10==0:
#     print('the given number is in three digit and divisible by 10')
# else:
#     print('the given number is not in three digit and not divisible by 10')    

# #Check if a given number is three digit number and also it is a multiple of 2, 5 and 10.
# num=int(input('enter a number:'))
# if 111 <=num <=999 and num%2==0 and num%5==0 and num%10==0:
#       print('yes it is a three digit number and divisible by 2,5 and 10')
# else:
#        print(' not divisible by 2,5 and 10')
       
# #Write a program to Check if a given number ends with zero or not.
# num=int(input('enter a number:'))
# if num%10==0:
#     print('the given number ends with zero')
# else:
#     print('the number not ends with zero')    

# #assignment 3
# #ascii value of character
# char=input('enter a char:')
# ascii_value=ord(char)
# print(ascii_value)

# # #ASCII CHAR

# num=int(input('enter a num:'))
# ascii_char=char(num)
# print(ascii_char)  

# # #LOWER CASE

# num=int(input('enter a number:'))
# if 97<=num<=122:
#     print('yes')
# else:
#     print('no')   

# # #UPPERCASE     
# num=int(input('enter a number:'))
# if 65<=num<=90:
#     print('yes')
# else:
#     print('no')   

# #NUMBER ASCII VALUE OR NOT
# num=int(input('enter a number:')) 
# if 48<=num<=57:
#     print('yes')
# else:
#     print('no')     

# #GAME OF MULTIPLICATION AND ADDITION
# num1=int(input('enter a number:'))
# num2=int(input('enter a number:'))
# if num1%2==0 and num2%2==0:
#     print(num1*num2)
# else:
#     print(num1+num2)     

# # POSIIVE OR NEGATIVE
# num=int(input('enter a number:'))
# if num>0:
#     print('positive')
# elif num<0:
#     print('negative')
# else:
#     print('zero')

# #ABSOLUTE VALUE
# num=int(input('enter a number:')) 
# if num<0:
#     abs_val=-num   
# else:
#     print('abs_val')          

# #LARGEST NUMBER
# num1 = int(input('enter a number:'))
# num2= int(input('enter a number:'))

# if num1 > num2:
#     largest=num1
# else:
#     largest=num2
#     print('largest',num2)

# #small number

# num1 = int(input('enter a number:'))
# num2= int(input('enter a number:'))
# if num1<num2:
#     print(num1)
# else:    
#    print(num2)

# # largest among 3 numbers
# a, b, c = map(int, input("Enter three numbers: ").split())

# if a >= b and a >= c:
#     print("Largest number is:", a)
# elif b >= a and b >= c:
#     print("Largest number is:", b)
# else:
#     print("Largest number is:", c)

# #smallest

# a, b, c = map(int, input("Enter three numbers: ").split())

# if a <= b and a <= c:
#     print("Smallest number is:", a)
# elif b <= a and b <= c:
#     print("Smallest number is:", b)
# else:
#     print("Smallest number is:", c)

#assignment4
write a program to find the remainder of two given numbers

num1=int(input('enter a number:'))
num2=int(input('enyter a number:'))
if num1>num2:
    remainder=num1%num2
    print('remainder=',remainder)
else:
    print('remainder by zero is not possible' )       

write a program to find the grade of a student marks
marks=int(input('enter marks:'))
if marks<0 or marks>100:
    print('invalid marks')
elif marks>=90:
    print('grade= A+')
elif marks>=80:
    print('grade= A')
elif marks>=70:
    print('grade= B+')
elif marks>=60:
    print('grade= B')
elif marks>=50:
    print('grade= C')
else:
    print('student has been failed')


largest among 4 integers

n, m, l, k = map(int, input().split())

if n > m and n > l and n > k:
    print(n)
elif m > n and m > l and m > k:
    print(m)
elif l > n and l > m and l > k:
    print(l)
else:
    print(k)

swapping numbers
num1=int(input('enter a number:'))
num2=int(input('enter a number:'))
temp=num1
num1=num2
num2=temp

print(num1,num2)


smallest among 4 numbers
n, m, l, k = map(int, input().split())

if n < m and n < l and n < k:
    print(n)
elif m < n and m < l and m < k:
    print(m)
elif l < n and l < m and l < k:
    print(l)
else:
    print(k)