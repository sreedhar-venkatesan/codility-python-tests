def solution(A,K):
    N=len(A)
    B=[0]*N
    for i in range(N):
        B[i]=A[(i-K)%N]
    return B
if __name__ =="__main__":
    K=3
    A=[3,8,9,7,6,8]
    A=solution(A,K)
    print (A)
