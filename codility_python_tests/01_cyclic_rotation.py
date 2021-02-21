def solution(A,K):
    return (A[len(A)-K:len(A)]+A[0:len(A)-K])

if __name__ =="__main__":
    K=3
    A=[3,8,9,7,6]
    A=solution(A,K)
    print (A)
