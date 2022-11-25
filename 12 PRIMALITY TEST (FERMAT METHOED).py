def expo(a,n):
    if n==0:
        return 1
    elif n==1:
        return a
    else:
        if n%2==0:
            r=n/2
            p=expo(a,r)
            return p*p
        else:
            r=n//2
            p=expo(a,r)
            return a*p*p
def isPrime(n):
    for a in range(2,n):
        m=n-1
        E=expo(a,m)
        if E%n!=1:
            return False
    return True 

if __name__== "__main__":
    num=int(input("enter the number:"))
    if isPrime(num):
        print(f"YESS, {num} is a prime no.")
    else:
        print(f"{num} is NOT PRIME")
    
    
