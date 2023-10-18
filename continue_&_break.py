# #continue
# shopping_list = ["banana", "egg", "glue", "spinach", "pants"]
# for items in shopping_list:
#     if items=="spinach":
#         continue
#     print("buy " + items)

#break
shopping_list = ["banana", "egg", "glue", "spinach", "pants","braclet","orange"]
# for items in shopping_list:
#     if items=="spinach":
#         break
#     print("buy " + items)
item_to_find= "pants"
found_at = None
# for items in range(len(shopping_list)):
#     if shopping_list[items]=="pants":
#         found_at=items
#         break;
# if found_at is not None:
#     print(f"{item_to_find} is found at index {found_at}")
# else:
#     print(f"{item_to_find} is not found in the list ")
if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)
if found_at is not None:
    print(f"{item_to_find} is found at index {found_at}")
else:
    print(f"{item_to_find} is not found in the list")
