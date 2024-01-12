def isUgly(n: int) -> bool:
        if n <= 0:
            return False
        while n % 2 == 0:
            n /= 2
        while n % 3 == 0:
            n /= 3
        while n % 5 == 0:
            n /= 5
        if n == 1:
            return True
        else:
            return False
        
n = int(input("Enter number: "))
result = isUgly(n)

print(result)