import random
higher=100
answer = random.randint(1,higher)
print(answer) #TODO: remove after testing
print("Please guess a number between 1 and {} : ".format(higher))

guess = 0 #initialise to any number that doesn't equal the answer

while guess!=answer:
    guess = int(input())
    if guess == 0:
        break
    if guess==answer:
        print("you guess correctly. You win!!")
        break
    else:
        if guess<answer:
            print("Please guess higher: ")
        else:  #guess must be greater than answer
            print("Please guess lower: ")


# #second code
# if guess!=answer:
#     if guess<answer:
#         print("Please guess higher: ")
#     else:  #guess must be greater than answer
#         print("Please guess lower: ")
#     guess=int(input())
#     if answer==guess:
#         print("You guessed correctly !!!")
#     else:
#         print("Sorry, your guess is not correct. Try next time 🤕")
# else:
#     print("You guessed correctly in first time 🥰✨")
#first code

# if guess>answer:
#     print("Please guess lower number")
#     guess = int(input())
#     if guess==answer:
#         print("You got it second time 🤭🫣")
#     else:
#         print("Sorry, you have not guessed correctly.")
# elif guess<answer:
#     print("please guess higher number")
#     guess = int(input())
#     if guess==answer:
#         print("You got it second time 🤭🫣")
#     else:
#         print("Sorry, you have not guessed correctly.")
# else: 
#     print("You got it first time. 🤭😏")