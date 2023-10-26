print("Please choose an option:")
print("1. Go for cycle ride\n 2. Go to bed.\n 3.Learn Python\n 4. Making college notes\n 5. Go to temple\n0.exit")
# your_choice = int(input("Enter here: "))
# for i in range(5):
#     if your_choice==1:
#         print("Take cycle and go for ride")
#         break
#     elif your_choice==2:
#         print("Make bed and close lights")
#         break
#     elif your_choice==3:
#         print("Open laptop and start your course")
#         break
#     elif your_choice==4:
#         print("See old past paper and take reference from notes of senior")
#         break
#     elif your_choice==5:
#         print("Take bath and get ready")
#         break
#     elif your_choice==0:
#         print("Exit")
#         break
# else:
#     print("Invalid choice")
#     your_choice = int(input("Enter here: "))
choice="-"
while choice!=0:
   
    if choice in "12345":
        print("You chose {}".format(choice))
    else:
        print("Please choose your option from the list below:")
        print("1. Go for cycle ride\n 2. Go to bed.\n 3.Learn Python\n 4. Making college notes\n 5. Go to temple\n0.exit")
    choice = input()