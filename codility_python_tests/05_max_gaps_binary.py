def solution(N):
    bin = "{0:b}".format(N)
    max_gap = 0
    accum = 0
    for i in bin:
        if i=='0':
            accum += 1
        elif i =='1':
            if accum> max_gap:
                max_gap =accum
            accum = 0
    return (max_gap)

if __name__ =="__main__":
    X= solution(20)
    print (X)
