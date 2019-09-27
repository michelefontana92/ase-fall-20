def sum(m, n):
    for i in range(n):
        m = m+1
    return m

def divide(m, n):
    count = 0
    try:
        while n > 0:
            m = m-n
            count = count+1
    except:
        print("cannot divide for 0")
    return count

def subtract(m, n):
    if n<0:
        return sum(m,abs(n))
    else:
        for i in range(n):
            m = m-1

def multiply(m, n):
    if n<0:
        return -multiply(m, abs(n))
    else:
        for i in range(n):
            m = m+m
    return m

def main():
    print(str(sum(2, 3)))
    print(str(divide(10, 3)))
    print(str(divide(4, 0)))
