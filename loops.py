# prod=[10,20,30,40,50,60]
# total=1
# for prod in prod:
#     total*=prod
# print(total) 
# prices=[1299,1599,2399,2699,3299,4599]
# newprices=[]
# for price in prices:
#     newprices+=[price*1.1]
#     print(newprices)

# salaries=[67000,96543,11246,123342,234000,12000]
# newsalaries=[]
# for salary in salaries:
#     if salary>100000:
#         newsalaries+=[salary-salary*0.12]
#     else:

    
#         newsalaries+=[salary-salary*0.05]
# print(newsalaries)        
     
# #break
# for i in range(1,11):
#     print(i)
#     if i==5:
#         break
# find a student name in a list of characters
# charecters=['jaffa','killbill','delhi soori','halwaraj','padmanabhasimha']
# for charecter in charecters:
#     if charecter=='gajala':
#         print(f'{charecter}:CEO of sonic solutions found')
#         break
# else:
#     print(f'gajala is gone')    


#write a program to look for a file name named virus filebin a list of files
# filename=input('enter file name:')
# files=['file1.py','file2.py','progfile.py','virus.py','kgfchapter.py']
# index=0

# while index<len(files):
    
#     if files[index]=='virus.py':
#       print('virus file found')
#       break
#     index+=1

# else:
#    print('virus file not found')


# n = int(input("Enter the list size: "))

# numbers = []

# for i in range(n):
#     num = int(input("Enter a number: "))
#     numbers.append(num)

# print("The list is:")
# for i in range(n):
#     print(numbers[i])

# n=int (input('enter a list size:'))
# list=[]
# for i in range (n):
#     num=int(input('enter a number:'))
#     list.append(num)
# for i in range (n):
#     print(list[i])
# total=0
# for i in range (n):
#     total+=list[i]
# print(total)
# count=0
# for i in range (n):
#     count+=1
# print(count)

# for i in range(n):
#     if list[i]%2==1:
#      print(list[i])
# sum=0
# for i in range(n):
#     sum+=list[i]
#     avg=sum//n
# print(avg)

# print largest elements in a list


# n=int (input('enter a list size:'))
# list=[]
# for i in range (n):
#     num=int(input('enter a number:'))
#     list.append(num)
# largest= 0
# for i in range(1,n):
#     if list[i]>largest:
#         largest=list[i]
# print(largest)

# print largest elements in a list
# n=int (input('enter a list size:'))
# list=[]
# for i in range (n):
#     num=int(input('enter a number:'))
#     list.append(num)
#     smallest=list[0]
# for i in range(1,n):
#     if list[i]<smallest:
#         smallest=list[i]
#     print(smallest)

# n=int (input('enter a list size:'))
# list=[]
# for i in range (n):
#     num=int(input('enter a number:'))
#     list.append(num)

# largest= 0
# secondlargest=0
# for i in range(1,n):
#     if list[i]>largest:  
#         secondlargest = largest      
#         largest=list[i]
# print(largest)

# n=int (input('enter a list size:'))
# list=[]
# for i in range (n):
#      num=int(input('enter a number:'))
#      list.append(num)

# smallest= list[0]
# secondsmallest= list[0]
# for i in range(1,n):
#     if list[i]<smallest:
#         secondsmallest=smallest
#         smallest=list[i]
#     elif list[i]<secondsmallest and list[i]!=smallest:
#             secondsmallest=list[i]
# print(secondsmallest*smallest)



 

