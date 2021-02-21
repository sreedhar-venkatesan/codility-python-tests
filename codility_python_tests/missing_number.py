def solution(A):
    # write your code in Python 3.6
    A = set(A)
    A = list(A)
    A.sort()
    if  max(A) <= 0:
        return 1
    A= [x for x in A if x > 0 ]
    for i in range(len(A)):
        if A[i] != i+1:
            return i+1            
    return max(A)+1
A = [0,1,2,4,5]
miss_num = solution (A)
print (miss_num)
