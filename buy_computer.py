available_parts = ["computer","monitor","keyboard","mouse","speaker"]
current_choice = "-" #nulll
computer_parts= [] #empty list
while current_choice!='0':
    if current_choice in "12345":
        print("Adding {}".format(current_choice))
        if current_choice == '1':
            computer_parts.append("computer")
        elif current_choice=='2':
            computer_parts.append("monitor")
        elif current_choice=='3':
            computer_parts.append("keyboard")
        elif current_choice=='4':
            computer_parts.append("mouse")
        elif current_choice=='5':
            computer_parts.append("speaker")
    else:
        print("Please add options from the list below:")
        # print("1. computer")
        # print("2: monitor")
        # print("3: keyboard")
        # print("4: mouse")
        # print("5. speaker")
        # print("0: to finish")
        #using for loop instead of 6 print statements 
        # for part in available_parts:
        #     print("{0}:{1}".format(available_parts.index(part)+1, part))
        #using enumerate function
        for number,part in enumerate(available_parts):
            print("{0}: {1}".format(number+1, part))
    current_choice= input()
print(computer_parts)