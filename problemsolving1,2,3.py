# area of a square
#area = side*side
# side=int(input('enter size of a square side'))
# area=side*side
# print(f'area of a squarem with side {side}is:{area}')

#perimeter of a square
# side=float(input('enter size of a perimeter of side')) 
# perimeter = 4*side
# print(f'perimeter of the square with side {side}is: {perimeter}')

# base=float(input('enter the base of a triangle'))
# height=float(input('enter the height of a triangle'))

# side1=float(input('enter side1 measure'))
# side2=float(input('enter side2 measure'))
# side3=float(input('enter side3 measure'))
# area=(1/2)* base* height

# perimeter=side1+side2+side3

# print(f'area and perimeter of a triangle are:{area} and {perimeter}is:')

# check whether a even or odd
# num=int(input("enter a number"))
# if num%2==0:
#  print(f'{num}is even')
# else:
#  print(f'{num}is odd')

# check whether a num is divisible by 5 and not divisible by 10
# num=int(input('enter a number'))
# if num%5==0 and num%10!=0:
#     print(f'{num}satisfy condition')
# else:
#     print(f'{num}doesnt satisfy ')

# greatest among two numbers

# num1=int(input('enter number1:'))
# num2=int(input('enter number2:'))
# if num1>num2:
#     print(f'{num1}is greater')
# elif num2>num1:
#     print(f'{num2}is greater')

# else:
#     print(f'both are equal')

#smallest among two numbers

# num1=int(input('enter number1:'))
# num2=float(input('enter number2:'))
# if num1<num2:
#     print(f'{num1}is smaller')
# elif num2<num1:
#     print(f'{num2}is smaller')
# else:
#     print(f'both are equal')

#leap year or not

# year=int(input('enter a year:'))
# if year%4==0 and year%100!=0 or year%400==0:
#     print(f'{year}is a leap year')
# else:
#     print(f'{year}is not a leap year')

# check whether a number is perfect square or not
# num=int(input('enter a number:'))
# perfsq=num**0.5
# if perfsq==int(perfsq):
#     print(f'{num}is a perfect square')
# else:
#     print(f'{num}is not a perfect square')
    

# count the required number of cars for given passengers where each car can carry maximum 5 members

# passengers=int(input('enter a number of passengers:'))
# if passengers%5==0:
#     cars=passengers//5
#     print('number of cars required for pasengers is,:',cars)
# else:
#     cars=passengers//5+1
#     print('number of cars required for pasengers is:',cars)
    

# write a program to print sum and product of numbers from m to n using while loop

# def sumprod(m,n):
#     sum=0
#     product=1
#     while m<=n:
#         sum+=m
#         product*=m
#         m+=1
#     return f'the sum and product is:{sum},{product}'
# print(sumprod(1,5))      
# 
# write a program to print return factorial of a number using function and while loop
# def factorial(number):
#     fact=1
#     temp=number
#     while temp>0:
#         fact*=temp
#         temp-=1
#         return f'the factorial of number is:{}'
# print(factorial(5))


# write a program to print n fibonacci number using while loop

# def fibinocci(num):

#    a = 0
#    b = 1


#    while num >=1:
#     print(a)
#     a, b = b, a + b
#     num -= 1
# fibinocci(10)    


#write a function to return count of no of divisibles of a number using while loop
# def  divisiblecount(n):
#     count=0
#     i=1
#     while i<=n:
#         if n%i==0:
#             count+=1
#         i+=1
#     return f'thenumber of divisibles of{n}are:{count}'
# print(divisiblecount(6))

# write a function o return count of prime numbers of a number using while loop
# def  primenumcount(n):
#     count=0
#     i=1
#     while i<=n:
#         if n%i==0:
#             count+=1
#         i+=1
#     if count==2:
#         return f'{n} is prime:'
#     else: 
#         return f'{n} is not prime:'

# print(primenumcount(51))

#perfect square
# def perfectsquare(num):
#     result=num**0.5
#     if result==int(result):
#      return f'{num}is a perfect square'
#     else:
#        return f'{num}is not a perfect square'
# print(perfectsquare(25))
# 
# perfect number


#def perfect number
# def perfectnumber(num):
#     sum=0
#     i=1
#     while i<num:
#         if num%i==0:
#             sum+=i
#         i+=1
#     if sum==num:
#           return f'the {num} is perfect number: '  
#     else:
#            return f'the {num} is not perfect number:' 
# print(perfectnumber(6))     
            























    