n=int(input("Please enter your number:"))
def jieCheng(n):
    if n == 1:
        return 1
    else:
        return n*jieCheng(n-1)
