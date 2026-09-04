#nested loops : in insted lopps we can define a loop inside another loop.
# in python cross nested loops are possible i.e we can write while loop inside a for loop and for loop inside while loop

#basic program
# for i in range(5):
#     for j in range(5):
#         print(f'{i},{j}')

#printing all tables from 1 to 12
# for i in range(1,13):
#     print(f'table of {i}')
#     for j in range(1,11):
#         print(f'{i}*{j}={i*j}')

# print each element in a matrix individually
# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(matrix[i][j])  
# for row in matrix:
#     for value in row:
#         # print(value)
# sum=0
# for row in matrix:
#     for value in row:
#                 sum+=value
# print(sum)

# wap  to print seating arrangement in theater
# rows=['A','B','C','D','E']
# seats=[1,2,3,4,5,2,3,4,5,6,7,8,9,10]
# for row in rows:
#     for seat in seats:
#         print(f'{row}{seat}',end=' ')
#     print()

#write a program to make schedule for all weekdays for all classes
# days=['mon','tue','wed','thu','fri']
# classes=['py','sql','communication','apptitude']
# for day in days:
#     for cla in classes:
#      print(f'{day}:{cla}',end=' ')
# print()
