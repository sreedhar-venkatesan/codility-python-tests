def solution(A):
    bool = [False]*len(A)

    for i in A:
        if 0<=i> len(A):
            return 0
        if bool[i-1] == True:
            return 0
        bool[i-1] = True
    return 1

if __name__ == "__main__":
    A = [1,2,3,4]
    X=solution(A)
    print (X)