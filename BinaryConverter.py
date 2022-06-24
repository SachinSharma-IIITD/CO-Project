def converter(num1, A, B):
    tot=0
    digit = [i for i in num1]
    digit.reverse()
    for val in range(len(digit)):
        if digit[val].isalpha():
            pos = ord(digit[val]) - 55
            tot += (A**val)*pos
        else:
            tot += int(digit[val])*(A**val)
    l=[]
    a2=tot
    while a2>0:
        a1 = tot%B
        a2 = tot//B
        tot = a2
        l.append(a1)
    l2=[]
    for converter in l:
        if converter>9:
            l2.append(chr(converter-10 + 65))
        else:
            l2.append(converter)
    l2=[str(num1) for num1 in l2]
    l2.reverse()
    finalnum = "".join(l2)
    return finalnum