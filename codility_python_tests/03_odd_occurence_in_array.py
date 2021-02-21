def solution(A):
    odd = 0
    for i in A:
        odd^=i 
        return odd



if __name__ == "__main__":
    A = [1,2,1,2,1,2,1,2]
    X=solution(A)
    print (X)