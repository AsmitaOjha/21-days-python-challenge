age=19
print("My age is " + str(age) + "year")
print("My age is {0} year".format(age))
print("There are {0} days in {1},{2},{3},{4},{5},{6},{7}".format(31,"Jan","Mar","May","Jul","Aug","Oct","Dec"))
print("Jan: {2}, Feb:{0},Mar:{2}, Apr:{1}".format(28,30,31))
#string formatting
for i in range(1,15):
    print(" {0:2}'s square is {1:6} and cube is {2:6}".format(i,i**2,i**3))

print()
for i in range(1,15):
    print(" {0:2}'s square is {1:<6} and cube is {2:^6}".format(i,i**2,i**3))

