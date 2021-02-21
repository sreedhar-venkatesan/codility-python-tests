def solution(A):
    chop_1 =A[0]
    chop_2 = sum(A[1:])
    min_diff = abs(chop_1 - chop_2)
    for i in range(1, len(A)-1):
        chop_1 += A[i]
        chop_2 -= A[i]
        if abs(chop_1-chop_2)< min_diff:
            min_diff = abs(chop_1-chop_2)
    return min_diff
if __name__ == "__main__":
    A = [3,1,2,4,3]
    X= solution(A)
    print (X)