def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a,b):
    return int(a * b / gcd(a,b))

a = 56
b = 24
print(gcd(a,b))
print(lcm(a,b))