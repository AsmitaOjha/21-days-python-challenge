# i=0
# while i<10:
#     print("i is now {}".format(i))
#     i+=1

available_exits = ['north','south', 'east','west']
chosen_exit = ''
while chosen_exit not in available_exits:
    chosen_exit= input('please choose a direction:').casefold()
    if chosen_exit.casefold()=="quit":
        print("Game over")
        break
else: print("Aren't you glad you got out of there")