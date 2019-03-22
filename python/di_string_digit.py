
#// 123, “012X456789” -> “12X” 
#// 255, “0123456789ABCDEF” -> “FF” 
#// 7, “01” -> “111” 
#// 7, “AB” -> “BBB”


def convert(num, string):
    k = len(string)
    if k < 2: return ''
    else:
        sout = ''
        sign = num/abs(num)
        tmp = num
        while tmp > 0:
            sout += string[tmp % k]
            tmp = tmp//k
    return sout[::-1]

print(convert(123, '012x456789'))
print(convert(255, '0123456789ABCDEF'))
print(convert(7, '01'))
print(convert(6, 'AB'))

