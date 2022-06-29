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

opcode = {
    'sub': {'opcode': '10001',
            'type': 'A'},
    'add': {'opcode': '10000',
            'type': 'A'},
    'mov': {'opcode': '10011',
            'type': 'C'},
    'ld':  {'opcode': '10100',
            'type': 'D'},
    'st':  {'opcode': '10101',
            'type': 'D'},
    'mul': {'opcode': '10110',
            'type': 'A'},
    'div': {'opcode': '10111',
            'type': 'C'},
    'rs':  {'opcode': '11000',
            'type': 'B'},
    'ls':  {'opcode': '11001',
            'type': 'B'},
    'xor': {'opcode': '11010',
            'type': 'A'},
    'or':  {'opcode': '11011',
            'type': 'A'},
    'and': {'opcode': '11100',
            'type': 'A'},
    'not': {'opcode': '11101',
            'type': 'C'},
    'cmp': {'opcode': '11110',
            'type': 'C'},
    'jmp': {'opcode': '11111',
            'type': 'E'},
    'jlt': {'opcode': '01100',
            'type': 'E'},
    'jgt': {'opcode': '01101',
            'type': 'E'},
    'je':  {'opcode': '01111',
            'type': 'E'},
    'hlt': {'opcode': '01010',
            'type': 'F'}
}

reg = {
    'R0':    {'addr': '000',
              'data': 0},
    'R1':    {'addr': '001',
              'data': 0},
    'R2':    {'addr': '010',
              'data': 0},
    'R3':    {'addr': '011',
              'data': 0},
    'R4':    {'addr': '100',
              'data': 0},
    'R5':    {'addr': '101',
              'data': 0},
    'R6':    {'addr': '110',
              'data': 0},
    'FLAGS': {'addr': '111',
              'data': [0 for i in range(16)]}
}

inputlengtherror = {
    'sub': 4,
    'add': 4,
    'mov': 3,
    'ld':  3,
    'st':  3,
    'mul': 4,
    'div': 3,
    'rs':  3,
    'ls':  3,
    'xor': 4,
    'or':  4,
    'and': 4,
    'not': 3,
    'cmp': 3,
    'jmp': 2,
    'jlt': 2,
    'jgt': 2,
    'je':  2,
    'hlt': 1
}


def Divide(given_list : list):
    opcode1 = opcode['div']['opcode']
    unused = '00000'
    reg1 = reg[given_list[0]]['addr']
    reg2 = reg[given_list[1]]['addr']
    final = opcode1 + unused + reg1 + reg2
    return final

def Rightshift(given_list : list):
    opcode1 = opcode['rs']['opcode']
    reg1 = reg[given_list[0]]['addr']
    imm = (given_list[1][1:])
    new = converter(imm)
    left = 8-len(new)
    unused = ''
    for i in range(left):
        unused = unused + '0'
    final = opcode1 + reg1 + unused + new
    return final

def Leftshift(given_list : list):
    opcode1 = opcode['ls']['opcode']
    reg1 = reg[given_list[0]]['addr']
    imm = (given_list[1][1:])
    new = converter(imm)
    left = 8-len(new)
    unused = ''
    for i in range(left):
        unused = unused + '0'
    final = opcode1 + reg1 + unused + new
    return final


def Exclusiveor(given_list : list):
    opcode1 = opcode['xor']['opcode']
    unused = '00'
    reg1 = reg[given_list[0]]['addr']
    reg2 = reg[given_list[1]]['addr']
    reg3 = reg[given_list[2]]['addr']
    final = opcode1 + unused + reg1 + reg2 + reg3
    return final

def Or(given_list : list):
    opcode1 = opcode['or']['opcode']
    unused = '00'
    reg1 = reg[given_list[0]]['addr']
    reg2 = reg[given_list[1]]['addr']
    reg3 = reg[given_list[2]]['addr']
    final = opcode1 + unused + reg1 + reg2 + reg3
    return final

def And(given_list : list):
    opcode1 = opcode['and']['opcode']
    unused = '00'
    reg1 = reg[given_list[0]]['addr']
    reg2 = reg[given_list[1]]['addr']
    reg3 = reg[given_list[2]]['addr']
    final = opcode1 + unused + reg1 + reg2 + reg3
    return final

def Invert(given_list : list):
    opcode1 = opcode['not']['opcode']
    unused = '00000'
    reg1 = reg[given_list[0]]['addr']
    reg2 = reg[given_list[1]]['addr']
    final = opcode1 + unused + reg1 + reg2
    return final

def Compare(given_list : list):
    opcode1 = opcode['cmp']['opcode']
    unused = '00000'
    reg1 = reg[given_list[0]]['addr']
    reg2 = reg[given_list[1]]['addr']
    final = opcode1 + unused + reg1 + reg2
    return final

def checklength(checking : list):
    if(checking == []):
        return 0
    a = checking[0]
    if(len(checking)!=inputlengtherror[a]):
        return 0
    return 1
flag = 1
flag1=0
new_l = []
while(flag1!=4):
    a1 = input()
    symbols = '!@#%^&*()_+-=~`{}[]:;"\'<>,.?/\|'
    for i in symbols:
        if i in a1:
            print("ERROR : Invalid symbols found")
            flag =5
            break
    new_list = [i for i in a1.split()]
    new_l.append(new_list)
    if new_list != ['hlt'] and new_list[0] not in opcode:
        print("ERROR : Invalid command provided")
        flag =2
        break

    if new_list == ['hlt']:
        flag1 =4

    if(checklength(new_list)==0 and new_list!=[]):
        print("ERROR : Please provide accurate number of arguments")
        flag =3
        break
    

if(flag==1):
    for i in new_l:
        if i[0]=='div':
            print(Divide(i[1:]))
        elif i[0]=='rs':
            print(Rightshift(i[1:]))
        elif i[0]=='ls':
            print(Leftshift(i[1:]))
        elif i[0]=='xor':
            print(Exclusiveor(i[1:]))
        elif i[0]=='or':
            print(Or(i[1:]))
        elif i[0]=='and':
            print(And(i[1:]))
        elif i[0]=='not':
            print(Invert(i[1:]))
        elif i[0]=='cmp':
            print(Compare(i[1:]))
        elif i[0]=='hlt':
            print('0101000000000000')
    
    



