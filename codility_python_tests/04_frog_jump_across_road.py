import math
def solution(X,Y,D):
    distance = Y-X
    return math.ceil(distance/D)

if __name__ =="__main__":
    X=10
    Y=85
    D=30
    ans = solution(X,Y, D)
    print (ans)