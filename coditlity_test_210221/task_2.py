## Task 2


def solution(A):
    "get the max sum of 2 numbers"
    A.sort()
    B = A[-1]+A[-2]
    max_A = [int(digit) for digit in str(A[-1])]
    sec_max_A = [int(digit) for digit in str(A[-2])]
    digit_sum =[]
    for i in range(len(max_A)):
        digit_temp= str(max_A[i] + sec_max_A[i])
        digit_sum.append(digit_temp)
    digit_sum_final =""
    for i in digit_sum:
        digit_sum_final += i
    if int(digit_sum_final) == B:
        return B
    else:
        return -1


if __name__ == "__main__":
    "main function"
    A = [10,21,33]
    X = solution(A)
    print (X)