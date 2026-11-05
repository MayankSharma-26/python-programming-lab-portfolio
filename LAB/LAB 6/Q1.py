# print("\tMultiplication Table")
# print("\t", end="")
# for j in range(1, 10):
#     print(f"{j:4}", end="")
# print("\n\t" + "-" * 36)
# for i in range(1, 10):
#     print(i, end="\t")
#     for j in range(1, 10):
#         print(f"{i * j:4}", end="")
#     print()


for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=" ")
    print()