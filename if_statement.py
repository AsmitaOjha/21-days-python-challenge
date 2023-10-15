name = input("What is your name ? \t")
age= int(input("How old are u, {0} ?".format(name)))
print(age)
# if age>=18:
#     print("You are old enough to vote.")
#     print("Please put X in the box.")
# else:
#     print("Please come back in {0} years".format(18-age))   #replacement fileds
#     print(f"Please come back in {18-age} years")        #f string
#if, elif and else
if age<18:
    print(f"Please come back in {age} years.")
elif age>=100:
    print(f"{name}, you're age to vote is gone 🤭. You are expired.")
else:
    print("You are old enough to vote");