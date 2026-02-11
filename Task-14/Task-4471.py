def convert(num, sys):
    res=''
    while num:
        res += str(num%sys)
        num //= sys
    return res[::-1]
num = 7*729**543-6*81**765-5*9**987-20
print(convert(num, 9).count('8'))