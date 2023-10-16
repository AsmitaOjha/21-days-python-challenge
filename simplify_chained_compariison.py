# age = int(input("How old are you ? : "))
# if 16<=age <=60:
#     print("Have a good dau at work")
#     print("_" * 80)
# else:
#     print("Enjoy your free time")
#     print("-" * 60)
day="Monday"
temperature = 30
raining = True
# if day=="Saturday" and temperature<=27 or not raining: # 3 otai expression True bhaye matra output sahi aaune ho, yaa raining aagar True bhaye
#     # not raining false hunxh, so ek expression false bhayo tabh output "Learn Python" dekhau xh
#     print("Go swimming")
# else:
#     print("Learn Python")
if day=="Saturday" and temperature<=27 or not raining:
        #yaaa day wala ani temperature wala expression are connected using AND so, first ma yo dui expression ko output 
        #nikaalinxh then aayeko output lai OR not raining sang compare garerah final output nikaalainxh
        #that means precedence of AND is higher than OR
        # real ma yestoh ho: if (day=="Saturday" and temperature<=27) or not raining:
        print("Go swimming")
else:
    print("Learn Python")