def solution(N):
    return len(max(format(N,'b').strip('0').split('1')))

if __name__ =="__main__":
    X= solution(20)
    print (X)
