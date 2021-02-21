def solution(A):
    return 1 if set(A)==set(range(1,len(A))) else 0

if __name__ == "__main__":
    A = [1,2,3,4,2]
    X=solution(A)
    print (X)