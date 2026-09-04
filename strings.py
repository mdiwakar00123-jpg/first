#reverse a string
# s='hello'
# rev = " "
# for i in range(len(s)-1,-1,-1):
#     rev+=s[i]
# print(rev)

#remove spaces from a text
# s='hel lo wor ld'
# result = ' '
# for ch in s:
#     if ch != ' ':
#         result += ch
# print(result)

# convert snake case to camel case
# s = "my_variable_name"
# result = " "
# is_under = False
# for ch in s:
#     if is_under == True:
#         result += ch.upper()
#         is_under = False
#     elif ch!='':
#         result == ch
#     else:
#         is_under = True
#         print(result)

# upper case to lowercase
# s = "Hello World"
# result = ""
# for ch in s:
#     if 'A' <= ch <= 'Z':
#         result += ch.lower()
#     else:
#         result += ch
# print(result)


s="Hello World"
result = ""
for ch in s:
    if ord(ch) >= 65 and ord(ch) <= 90:
        result += chr(ord(ch)+32)
    else:
        result += chr(ord(ch)-32)
        print(result)