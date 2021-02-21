def solution(A):
    A.sort()
    N = len(A)
    i=0
    while i<N:
        try:
            if A[i] ==A[i+1]:
                i+=2
            else:
                return A[i]
        except:
            return A[N-1]



if __name__ == "__main__":
    A = [1,2,1,2,1,4,2,1,2,5]
    X=solution(A)
    print (X)