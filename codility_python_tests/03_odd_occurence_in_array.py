def solution(A):
    for num in A:
        if A.count(num)%2:
            return num



if __name__ == "__main__":
    A = [1,2,1,2,1,2,1,2,5]
    X=solution(A)
    print (X)