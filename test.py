# n = int(input("Enter the number of employees: "))
# salaries = list(map(int, input("Enter the salaries separated by space: ").split()))

# average = sum(salaries) / n
# count = 0

# for salary in salaries:
#     if salary > average:
#         count += 1

# print("Average Salary:", average)
# print("Employees Above Average:", count)

# find repeated values

# numbers = list(map(int, input("Enter numbers: ").split()))

# repeated = []

# for num in numbers:
#     if numbers.count(num) > 1 and num not in repeated:
#         repeated.append(num)

# print("Repeated values:", repeated)

# num = int(input("Enter a positive integer: "))
# original = num
# reverse = 0

# while num > 0:
#     result = num % 10
#     reverse = reverse * 10 + result
#     num = num // 10

# if original == reverse:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

# numbers = list(map(int, input("Enter numbers: ").split()))
# minimum = numbers[0]
# maximum = numbers[0]
# for num in numbers:
#     if num < minimum:
#         minimum = num

#     if num > maximum:
#         maximum = num

# print("Minimum:", minimum)
# print("Maximum:", maximum)

# salary = float(input("Enter  salary: "))
# per = float(input("Enter deduction per: "))

# deduction = salary * per / 100
# final_salary = salary - deduction

# print("Deduction:", deduction)
# print("Final salary:", final_salary)