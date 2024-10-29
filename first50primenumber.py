def isPrime(n):
    divisor = 2
    while divisor<=n/2:
        if n % divisor ==0:
            return False
        divisor +=1

    return True


