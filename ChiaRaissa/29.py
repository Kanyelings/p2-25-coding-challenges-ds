def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return true
    for i in range(2, n):
        if n%i == 0:
            return False
        return True
    i = 2
    j = 3
    count = 0
    while count<100:
        if isPrime(j):
            print(j, "-",i,"=", j-1)
            count += 1
            i = j
            j += 1
