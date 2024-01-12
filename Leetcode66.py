def plusOne(digits: list[int]) -> list[int]:
        s = ""
        for i in digits:
            s += str(i)
        s = int(s)
        s += 1
        s = str(s)
        lst = []
        for i in s:
            lst.append(int(i))
        return lst


n = int(input("Input Lenth: "))
lst = [int(input("Element: ")) for i in range(n)]

result = plusOne(lst)
print(result)