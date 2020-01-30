
def bingap(x):
	num1 = '0'

	y = bin(x)
	y1 = y[2:len(y)]
	d = '-1'
	k = 0
	rez = 0
	for i in y1:
		d = i
		if i == d and i == num1:
			k +=1
		else:
			if k > rez:
				rez = k
			k = 0
	return rez

def solution(A):
    # write your code in Python 3.6
    size = len(A)
    if size == 1:
        return A[0]
    A.sort()
    print(A)
    d = A[0]
    k = 0
    for i in range(1,size):
        if A[i] == d:
            k+=1
        else:
            if k == 0 or k%2 == 1:
                return A[i-1]
            d = A[i]
            k = 0

    return A[size-1]



# o = 32
# print(bin(o))

# o1 = bingap(o)
# print(o1)
# print(s%2)
s = [1,2,3]


print(sum(s))

