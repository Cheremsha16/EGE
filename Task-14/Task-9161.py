def convert(num, sys):
    res=''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
num= 7*5**123 + 6*5**111 - 5*25**50 + 4*125**30 - 3*5**10
print(convert(num, 5).count('4'))
#89