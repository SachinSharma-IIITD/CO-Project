# 'mov' instruction stored for type 'mov reg1 reg2'
opcode={'add':'10000','sub':'10001','mov':'10011','ld':'10100','st':'10101','mul':'10110','div':'10111','rs':'11000','ls':'11001','xor':'11010','or':'11011','and':'11100','not':'11101','cmp':'11110','jmp':'11111','jlt':'01100','jgt':'01101','je':'01111','hlt':'01010'}
reg_add={'R0':'000','R1':'001','R2':'010','R3':'011','R4':'100','R5':'101','R6':'110','FLAGS':'111'}

def converter(num1, A=10, B=2):
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

flag_arr=[]
for i in range(0,16):
    flag_arr.append(0)
print(flag_arr)

def Unconditional_Jump(para):
    return para #parameter is memory address

def Jump_if_less_than(para):
    if(flag_arr[-3]==1):
        return para

def Jump_if_greater_than(para):
    if(flag_arr[-2]==1):
        return para

def Jump_if_equal(para):
    if(flag_arr[-1]==1):
        return para

halt_flag=False

def halt(para):
    halt_flag=True
    return halt_flag