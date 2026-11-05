# s = input()
# s=s.lower()
# if "a" in s:
#     if "b" in s:
#         if "c" in s:
#             if "d" in s:
#                 if "e" in s:
#                     if "f" in s:
#                         if "g" in s:  
#                             if "h" in s:
#                                 if "i" in s:
#                                     if "j" in s:
#                                         if "k" in s:
#                                             if "l" in s:
#                                                 if "m" in s:
#                                                     if "n" in s:
#                                                         if "o" in s:
#                                                             if "p" in s:
#                                                                 if "q" in s:
#                                                                     if "r" in s:
#                                                                         if "s" in s:
#                                                                             if "t" in s:
#                                                                                 if "u" in s:
#                                                                                     if "v" in s:
#                                                                                         if "w" in s:
#                                                                                             if "x" in s:
#                                                                                                 if "y" in s:
#                                                                                                     if "z" in s:
#                                                                                                         print("Pangram")
#                                                                                                     else:
#                                                                                                         print("Not a Pangram")
#                                                                                                 else:
#                                                                                                     print("Not a Pangram")
#                                                                                             else:
#                                                                                                 print("Not a Pangram")
#                                                                                         else:
#                                                                                             print("Not a Pangram")
#                                                                                     else:
#                                                                                         print("Not a Pangram")
#                                                                                 else:
#                                                                                     print("Not a Pangram")
#                                                                             else:
#                                                                                 print("Not a Pangram")
#                                                                         else:
#                                                                             print("Not a Pangram")
#                                                                     else:
#                                                                         print("Not a Pangram")
#                                                                 else:
#                                                                     print("Not a Pangram")
#                                                             else:
#                                                                 print("Not a Pangram")
#                                                         else:
#                                                             print("Not a Pangram")
#                                                     else:
#                                                         print("Not a Pangram")
#                                                 else:
#                                                     print("Not a Pangram")
#                                             else:
#                                                 print("Not a Pangram")
#                                         else:
#                                             print("Not a Pangram")
#                                     else:
#                                         print("Not a Pangram")
#                                 else:
#                                     print("Not a Pangram")
#                             else:
#                                 print("Not a Pangram")
#                         else:
#                             print("Not a Pangram")
#                     else:
#                         print("Not a Pangram")
#                 else:
#                     print("Not a Pangram")
#             else:
#                 print("Not a Pangram")
#         else:
#             print("Not a Pangram")
#     else:
#         print("Not a Pangram")
# else:
#     print("Not a Pangram")



x=input("Enter a sentence: ")
x=x.lower()
a="abcdefghijklmnopqrstuvwxyz"
count=0
for i in a:
    if i in x:
        count=count+1
if count==26:
    print("It is a Pangram")
else:
    print("It is not a Pangram")
