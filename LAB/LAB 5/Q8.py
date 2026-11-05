# sen=input("ENter your sentence  ")
# c1cap=0
# c2small=0
# c3no=0
# c4special=0
# i=0
# while i < len(sen):  #while sen[i:i+1] != "":
#     if sen[i] >= 'A' and sen[i] <= 'Z':
#         c1cap += 1
#     elif sen[i] >= 'a' and sen[i] <= 'z':
#         c2small += 1
#     elif sen[i] >= '0' and sen[i] <= '9':
#         c3no += 1
#     elif sen[i] == ' ':
#         pass
#     else:
#         c4special += 1
#     i += 1
# print("Capital letters =", c1cap)
# print("Small letters =", c2small)
# print("Digits =", c3no)
# print("Special characters =", c4special)  


sen=input("ENter your sentence  ")
c1cap=0
c2small=0
c3no=0
c4special=0
i=0
while sen[i:i+1] != "":
    if sen[i] >= 'A' and sen[i] <= 'Z':
        c1cap += 1
    elif sen[i] >= 'a' and sen[i] <= 'z':
        c2small += 1
    elif sen[i] >= '0' and sen[i] <= '9':
        c3no += 1
    elif sen[i] == ' ':
        pass
    else:
        c4special += 1
    i += 1
print("Capital letters =", c1cap)
print("Small letters =", c2small)
print("Digits =", c3no)
print("Special characters =", c4special) 