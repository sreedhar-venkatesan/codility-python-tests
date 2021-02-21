def solution(X,Y,D):
    if (Y-X)%D ==0:
        ans = (Y-X)//D
        return ans
    else:
        return ((Y-X)//D)+1
if __name__ =="__main__":
    X=10
    Y=85
    D=30
    ans = solution(X,Y, D)
    print (ans)