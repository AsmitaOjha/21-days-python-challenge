low =1
high=1000
print("please think of a number between {} and {}".format(low,high))
input("Press ENTER to start")
guesses = 1
while low!=high:
    guess = low +(high -low)//2
    high_low = input("My guess is {}.Sholud I guess higher or lower ?"
    "Enter h or l, or c if my guess was correct".format(guess)).casefold()
    if high_low == "h":
        #guess higher. The low end of the range because 1 greater than the guess.
        low = guess+1
    elif high_low=="l":
        #guess lower. the hgigh end of the range because one less than the guess.
        high = guess-1
    elif high_low == "c":
        print("I got it in {} guesses !".format(guesses)) 
        break
    else:
        print("Please enter h,l or c")
        
    #guesses = guesses +1
    guesses +=1
else:
    print("you thought of the number {}".format(low))
    print("I got it in {} guesses !".format(guesses))