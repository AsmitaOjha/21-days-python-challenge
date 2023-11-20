odd = [1,3,5,7,9]
even = [2,4,6,8,10]
numbers= odd + even
sorted_number= sorted(numbers)
print(sorted_number)
print(numbers)
digits = sorted("456123987")
print(digits)
alphabets = sorted("AZEVTBSQ")
print(alphabets)
more_numbers = numbers[:]
print(more_numbers)
print(numbers is more_numbers)
print(numbers == more_numbers)