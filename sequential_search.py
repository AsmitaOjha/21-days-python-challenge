def seq_search(A,K):
    for i in range(len(A)):
        if K==A[i]:
            print(f"Element {K} found at index {i}.")
            return #exit the function after finding the element
    print(f"Element {K} not found in the list.")
A= [12,5,8,9,3,11,15]
K = int(input("Enter the number you want to search for: "))
seq_search(A,K)

    

