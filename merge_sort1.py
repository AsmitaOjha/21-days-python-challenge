A = [12, 9, 5, 8, 99, 16,33,45,1,2,67,90,23,45,67]
temp = [0] * len(A)  # Create a temp array of the same size as A

def simplemerge(A, first, second, last):
    i = first
    j = second
    l = 0

    while i < second and j <= last:
        if A[i] < A[j]:
            temp[l] = A[i]
            i += 1
        else:
            temp[l] = A[j]
            j += 1
        l += 1

    while i < second:
        temp[l] = A[i]
        i += 1
        l += 1

    while j <= last:
        temp[l] = A[j]
        j += 1
        l += 1

    # Copy the temp array back into the original array A
    for k in range(first, last + 1):
        A[k] = temp[k - first]

def mergesort(A, first, last):
    if first < last:
        mid = (first + last) // 2
        mergesort(A, first, mid)
        mergesort(A, mid + 1, last)
        simplemerge(A, first, mid + 1, last)

# Call the merge sort function to sort the array A
mergesort(A, 0, len(A) - 1)
print(A)
