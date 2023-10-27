shopping_list =['milk','pasta', 'eggs','rice','bread']
another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list +=['cookies']
print(shopping_list)
print(id(shopping_list)) #list are mutable 
a=b=c=d=e=f=another_list
print(id(a))
print(id(b))
print("Adding cream")
b.append('cream')
print(c)
print(d)