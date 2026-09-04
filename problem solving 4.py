# def carcal(persons):
#     if persons%5==0:
#         print (f'the number of cars requiredn are:{persons//5}')
#     else:
#         print(f' the number of cars required are:{(persons//5)+1}')

# carcal(10)            

# write a program to check whether a year is leap year are not
# def leapyear(year):
#     if year%4==0 and year%100!=0 or year%400==0:
#         print (f'the {year} is a leap')
#     else:
#         print(f'the {year} is not a leap ')    
# leapyear(2019)  
# 
# def daysinmonth(month,year):
#     if month==2:
#         if year%4==0 and year%100!=0 or year%400==0:
#             noofdays=29
#         else:
#             noofdays=28
#     elif month==4 or month==6 or month==11:
#         noofdays=30
#     else:
#         noofdays=31
#     return f'the number of days in month {month} and year {year} are:{noofdays}'
# print(daysinmonth(2,1996))        
# 
#write a function to check whether a given date is valid or not
# def daysinmonth(month,year):
#     if month==2:
#         if year%4==0 and year%100!=0 or year%400==0:
#             noofdays=29
#         else:
#             noofdays=28
#     elif month==4 or month==6 or month==11:
#         noofdays=30
#     else:
#         noofdays=31
#     if day>=1 and day<=noofdays    
#     return f'the number of days in month {month} and year {year} are:{noofdays}'
# print(daysinmonth(2,1996))      
# 
# 
# write a function to print all prime numbers from m to n
# def allprimes(m,n):
#     primecount=0
#     for num in range(m,n+1):
#         count=0
#         for i in range(1,num+1):
#             if num%i==0:
#                 count+=1
#         if count==2:
#             print(num)
#             primecount+=1
#     print(f'the number of prime numbers are:{primecount}')        
# allprimes(10,22)            

# write a function to print first prime number from m to n
def allprimes(m,n):
    lastprime=0
    primecount=0
    for num in range(m,n+1):
        count=0
        for i in range(1,num+1):
            if num%i==0:
                count+=1
        if count==2:
            print(num)
            primecount+=1

    print(f'the number of prime numbers are:{primecount}')        
allprimes(10,22)    

# frist prime last prime nth prime closest prime number to a num




            