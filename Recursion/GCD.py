#take input of a, b and then find the greatest common divisior!

def gcd(a,b):
    if b== 0:
        return a
    if a%b == 0:
        return b

    return gcd(b, a%b)

#a =  input("Take input of a")
#b = input("Take input of b")

print("the gcd is : ",gcd(48,18))