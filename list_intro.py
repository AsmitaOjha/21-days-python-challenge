human_parts = ["head","hand","toe","finger","ear","eye","nose"]
print(human_parts)
print(human_parts[3:]) #index[3] lai laggayerah teshpaxi ko print garxh

human_parts[3:]=["tongue","stomach"] #index[3] ra teshpaxi ko indexes haru lai replace garerah tongue rakhxh
print(human_parts)
#deleting slice fo items from list
data =[4,5,8,10,12,17,18,600,123,560,654,150,344,564,1233,555,232,666,430,560,125,156,189,134,167,198]
del data[0:2]
print(data)

min_valid = 100
max_valid = 200
#process the low values in the list
stop=0
for index, value in enumerate(data):
    if value >= min_valid:
        stop=index
        break
print(stop)
del data[:stop]
print(data)
#process the high values in the list
start =0
for index in range(len(data)-1,-1,-1):
    print(index)
    if data[index]<=max_valid:
        #we have the index of the last item to keep.
        #set 'start' to the position of the first
        #item to delete, which is 1 after 'index'
        start=index + 1
        break

print(start)
del data[start:]
print(data)