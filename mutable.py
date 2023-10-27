shopping_list =['milk','pasta', 'eggs','rice','bread']
another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list +=['cookies']
print(shopping_list)
print(id(shopping_list)) #list are mutable 