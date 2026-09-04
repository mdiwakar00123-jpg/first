# def sumofnum(a,b):
#     return a+b
#     return a,b
# print(sumofnum(35,45))

# # if we give two return statement in a function it takes only one return statement in the function

# # write a program
# def sumchecker(a,b):
#     if a+b==10:
#         return a,b
#     return'their sum is not ==10'
# print(sumchecker(8,2))

# # TYPES OF ARGUMENTS
# def student(name,course):
#     print(f'student {name}has taken the course{course}')
# student('diwakar','cyber secirity')
# student('artificial intelligence','shankar')  

# # write a function to calculate sum of numbers in the given range
# def sumofnums(first,last):
#     sum=0
#     for i in range(first,last+1):
#         sum+=i
#     return sum
# # firstnum=int(input('enter a number:'))
# # lastnum=int(input('enter a number:')) 
# result=sumofnums(1,5)   
# print('sumofnums',result)    

#calculate simple intrest
# define simpleintrest (amount,intrest ,time)

def simpleintrest(amt,intrest,amount):
    sim=amt*intrest*amount/100
    return sim
result=simpleintrest(100000,2,4) 
print('simpleintrest=',result)  


#write a function calculate area of a circle

# def areacircle(radius):
#     area=(22/7)*radius*radius
#     return area
# print(areacircle(5))

# #perimeter of a circle
# def pericircle(radius):
#     area=(22/7)*radius*radius
#     area=(2*22/7*radius)
#     return area
# print(f'{pericircle(10):}'.f)





