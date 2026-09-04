#write a function to calculate salary of a person after tax deduction
# def salcal(basicsal,taxper):
#     taxamt=basicsal*(taxper/100)
#     totalsal=basicsal-taxamt
#     return totalsal
# print(salcal(78000,7))
# write a function sum of all even numbers from 1 to 50
# def sumeven():
#     sum1=0
#     for i in range(1,51):
#         if i%2==0:
#             sum1+=i
#     return sum1
# print(sumeven())        
# write a functionn to simulate banking with nestedfunction where take balance as enclosingvariable and with draw as localvariable
# def banking():
#     bal=5000
#     def banking1():
#         nonlocal bal
#         withdraw=2000
#         bal=bal-withdraw
#         print(f'the withdraw amount is :{withdraw}')
#     banking1()
#     print(f'the balance amount is:{bal}')
# banking()     

#TASK
# write a nested function we perform limited number of api calls to a server take limit  as parameter to the outer function and apicalls as enclosing variable
def apicalls(limit):
    calls=0
    def apicalls1():
        
# write a program to calculate 
