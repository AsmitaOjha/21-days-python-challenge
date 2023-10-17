# for i in range(1,20):
#     print("i is now {}".format(i))
# for i in range(5):
#     print(i)
# for i in range(10,0,-2):
#     print("i is now {}".format(i))
#     print("_" * 8)
# for i in range(90,100,3):
#     print("i is now {}".format(i))
# age= int(input("How old are u: "))
# if age  in range(16,66):
#     print("Have a good day at work")
# else:
#     print("Go to bed")

#write a program to print out all the numbers from
# 0 to 100 that are divisible by 7
for i in range(0,101,7):
    print(i)
# This solution uses a slice
for i in range(101)[::7]:
    print(i)