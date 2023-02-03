# Time complexity O(n), space O(1)
def graduation_ceremony(n):
    if n < 4:
        return str(2 ** (n - 1)) + '/' + str(2 ** n)
    A = 2
    AA = 1
    AAA = 1
    P = 4
    count = 8
    for i in range(4, n + 1):
        temp = AAA
        AAA = AA
        AA = A
        A = P
        P = count
        count = (count - temp) * 2 + temp
    return str(AAA + AA + A) + '/' + str(count)


if __name__ == '__main__':
    assert graduation_ceremony(5) == "14/29"
    assert graduation_ceremony(10) == "372/773"
