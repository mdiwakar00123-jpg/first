# def printnum():
#     n=int(input('enter number:'))
#     for i in range(1,n+1):
#         print(i)
# printnum()        

# write a program to print all odd numbers from 1 to n using while loop
# def oddnum():
#     n=int(input('enter a number:'))
#     i=1
#     while i<=n:
#         if i%2==1:
#             print(i)
#         i+=1
# oddnum()                


#write a program to print sum of all 1 to n numbers
# def printsum():
#     n=int(input("enter a number:"))
#     total=0
#     i=1
#     while i<=n:

#         total+=i
#         i+=1
#     print(total)
# printsum()         


#write a function to calculate electricity bill

def electricity():
    units=int(input('enter a number of units:'))
    price=float(input('enter unit price:'))
    bill=units*price
    charges=bill*0.08
    totalbill=bill+charges
    print('totalbill',totalbill)
electricity()    
