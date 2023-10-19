# Modify the code inside this loop to stop when i is greater than zero and exactly divisible by 11
for i in range(0, 100, 7):
    print(i)
    if i > 0 and i % 11 == 0:
        break
#continue exercise
for i in range (0,20):
    if i%3==0 or i%5==0:
        continue
    print(i)
        