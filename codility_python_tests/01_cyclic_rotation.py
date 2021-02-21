def solution(A,K):
    if len(A) == 0:
        return A
    K=K%len(A)
    return A[-K:] + A[:-K]
if __name__ =="__main__":
    K=3
    A=[3,8,9,7,6,8]
    A=solution(A,K)
    print (A)
 