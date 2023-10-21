numbers= [1,45,31,16,60]
for number in numbers:
    if number%8 == 0:
        #regest the list
        print("The numbers are unacceptable")
        break
else:
    print("All those numbers are fine")