# to print first prime number

# def first_prime(m,n):
#     for num in range (m,n+1):
#         if num>1:
#             for i in range(2,num):
#                 if (num%i)==0:
#                     break
#             else:
#                 print(num)
#                 return
# first_prime(50,100)


# to print last prime number
# def last_prime(m,n):
#     for num in range (n,m-1,-1):
#         if num>1:
#             for i in range(2,num):
#                 if (num%i)==0:
#                     break
#             else:
#                 print(num)
#                 return

# last_prime(50,100)    
            
# to print nth prime number
# def nth_prime(n):
#     count = 0
#     num = 1
#     while count < n:
#         num += 1
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             count += 1
#     print(num)
# nth_prime(2)    

# to print closest prime number
def closest_prime(start, end, num):
    closest = None
    difference = float('inf')

    for n in range(start, end + 1):
        if n > 1:
            for i in range(2, n):
                if n % i == 0:
                    break
            else:
                diff = abs(n - num)

                if diff < difference:
                    difference = diff
                    closest = n

    print("Closest prime:", closest)


closest_prime(50,100,60)