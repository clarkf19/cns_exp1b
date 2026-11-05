import math
import random
bases=[57,23,44,14,11]
def valid_base(a,n):
    while a<2 or a>=n or math.gcd(a,n)!=1:
        a=random.randint(2,n-2)
    return a

def euler_test(n):
    if n<=1:
        return "Composite"
    if n<=3:
        return "Prime"
    if n%2==0:
        return "Composite"
    for a in bases:
        a=valid_base(a,n)
        x=pow(a,(n-1)//2,n)
        if x!=1 and x!=n-1:
            return "Composite"
    return "Prime"
n=int(input("Enter a number:"))
print(n,"is",euler_test(n))