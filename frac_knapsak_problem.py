# Class to define an item.
class Item:
    # Constructor
    def __init__(self, Weight, Value):
        # Weight and Value of
        # an Item.

        self.weight = Weight
        self.value = Value

        # Value one can obtain by
        # taking a unit weight (1 Kg).
        self.valuePerUnitWeight = (Value)*1.00/(Weight)

    # Comparator to sort
    def __lt__(self, other):
        return self.valuePerUnitWeight > other.valuePerUnitWeight

# Function to find the maximum
# value that can be obtained.
def getMax (weight, value,  capacity):

    # Finding the size of the array.
    n = len(weight)

    # Making a new List array (say list)
    # of item type.
    list = []

    # Filling elements in the list.
    for i in range(n):
        list.append(Item(weight[i], value[i]))


    # Sorting the list in the decreasing
    # order of the value per unit weight ratio.
    list.sort()

    # Initializing answer with 0.
    ans = 0

    # Iterating over the list
    for i in range(n):
        wt = list[i].weight
        val = list[i].value

        valuePerUnitWeight = list[i].valuePerUnitWeight
        # If we can take the whole item.
        if (capacity >= wt):
            # Adding value to the current item.
            ans = ans + val
            print(f"{wt} is added and valueperunit weight is {valuePerUnitWeight}")


            # Reducing capacity by wt.
            capacity = capacity - wt

        # Otherwise we can take a fraction.
        else:
            print(f"capacity left= {capacity}")
            print(f"valueperunit weight is {valuePerUnitWeight}")
            # Adding the value of the part that we can take.
            ans = ans + valuePerUnitWeight * capacity
            print(valuePerUnitWeight * capacity)
            # Now we are left with no space so
            # we will terminate the loop.
            capacity = 0
            break

    # Returning the answer
    return ans

 # Driver code

# Defining the weights and values
# of the item.
weight = [10, 30, 20, 50]
value = [40, 30, 80, 70]
capacity = 60

print("Maximum value that can be obtained is", getMax(weight, value, capacity))
