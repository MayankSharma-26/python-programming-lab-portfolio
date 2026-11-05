# # s=input()
# # b=input()
# # s=s.lower()
# # b=b.lower()
# # h=0
# # k=0
# # for char in s:
# #     for j in char:
# #         h=ord(char)
# #         h
# # for c in b:
# #     for k in c:
# #         k=ord(c)

# # if h==k:
# #     print("True")
# # else:
# #     print("Flase")


# # s = input()
# # b = input()
# # s = s.lower()
# # b = b.lower()
# # h = 0
# # k = 0
# # if len(s)!= len(b):
# #     print("False")
# # else:
# #     for char in s:
# #         h = 0
# #         k = 0
# #         for j in s:
# #             if ord(char) == ord(j):
# #                 h = h + 1
# #         for c in b:
# #             if ord(char) == ord(c):
# #                 k = k + 1

# #         if h != k:
# #             print("False")
# #             break
# #     else:
# #         print("True")

# s = input()
# b = input()
# s = s.lower()
# b = b.lower()
# h = 0
# k = 0
# for char in s:
#         h=0 
#         k=0
#     for j in s:
#         if ord(char)==ord(j):
#             h=h+1
#     for c in b:
#         if ord(char)==ord(c): 
#             k=k+1
#     if h!=k:
#             print("FALSE")
#             break
# else:
#             print("TRUE")


def areAnagrams(string1, string2):
    string1 = string1.lower().replace(" ", "")
    string2 = string2.lower().replace(" ", "")
    b=True
    if len(string1) != len(string2):
        return False
    else:
        for ch in string1:
            if string1.count(ch)!=string2.count(ch):
                return False 
        return b
s = input("Enter first string: ")
b = input("Enter second string: ")
print(areAnagrams(s, b))


