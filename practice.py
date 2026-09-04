# TO ADD ELEMENTS IN A LIST AND PRINT THEM

# n=int (input('enter a list size:'))

# list=[]

# for i in range (n):
#     num=int(input('enter a number:'))
#     list.append(num)

# for i in range (n):
#     print(list[i])


# #WRITE A PROGRAM TO FIND THE SUM AND COUNT OF ELEMENTS IN A LIST

# total=0
# for i in range (n):
#     total+=list[i]
# print(total)

# count=0
# for i in range (n):
#     count+=1
# print(count)



# WRITE A PROGRAM TO PRINT ODD NUMBERS IN A LIST AND FIND THE AVERAGE OF ELEMENTS IN A LIST

# n = int(input("Enter the list size: "))

# numbers = []

# for i in range(n):
#     num = int(input("Enter a number: "))
#     numbers.append(num)

# print("Odd numbers are:")
# for i in range(n):
#     if numbers[i] % 2 == 1:
#         print(numbers[i])

# total = 0
# for i in range(n):
#     total += numbers[i]

# avg = total / n      
# print("Average =", avg)


# FIND THE LARGEST ELEMENT IN A LIST

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


#WRITE A PROGRAM TO PRINT SEATING ARRANGEMENT IN A THEATER
# rows=['A','B','C','D','E']
# seats=[1,2,3,4,5,2,3,4,5,6,7,8,9,10]
# for row in rows:
#     for seat in seats:
#         print(f'{row}{seat}',end=' ')
#     print()


# WRITE A PROGRAM TO PRINT SECONDLARGEST AND LARGEST NUMBER IN A LIST
# numbers = []

# n = int(input("Enter the number of elements: "))

# for i in range(n):
#     num = int(input())
#     numbers.append(num)

# largest = numbers[0]
# second_largest = numbers[0]

# for num in numbers:
#     if num > largest:
#         second_largest = largest
#         largest = num
#     elif num > second_largest and num != largest:
#         second_largest = num

# print("Largest:", largest)
# print("Second Largest:", second_largest)


# take a number whether it is positive negative or zero

n = int(input())

salaries = list(map(int, input().split()))

average = sum(salaries) / n

count = 0

for salary in salaries:
    if salary > average:
        count += 1

print("Average Salary:", average)
print("Employees Above Average:", count)
