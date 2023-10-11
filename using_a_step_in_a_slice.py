parrot = 'Norwegian Blue'
print(parrot[0:6:2])
number = "9,223,372,974,315,006,127"
print(number[0::4])
# slicing backward
letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[25:0:-1]
print(backwards)
back_two_steps = letters[25:0:-2]
print(back_two_steps)
#for printing qpo
print(letters[16:13:-1])
#for printing edcba
print(letters[4::-1])
#for printing last 8 characters in reverse order
print(letters[ :-9:-1])

# print(letters[-4::])
# print(letters[-5:26:])
print(letters[-1::])
print(letters[1::])
print(letters[:1]) # O index bhanke ko a, ani start index xain so 0 to 1 but not including 1