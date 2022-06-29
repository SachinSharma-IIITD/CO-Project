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
    'var': {''},
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
    'A': 4,
    'B': 3,
    'C': 3,
    'D': 3,
    'E': 2,
    'F': 1,
    
}

def Addition(given_list : list):
    opcode1 = opcode['add']['opcode']
    unused = '00'
    reg1 = reg[given_list[0]]['addr']
    reg2 = reg[given_list[1]]['addr']
    reg3 = reg[given_list[2]]['addr']
    final = opcode1 + unused + reg1 + reg2 + reg3
    return final

def Subtraction(given_list : list):
    opcode1 = opcode['sub']['opcode']
    unused = '00'
    reg1 = reg[given_list[0]]['addr']
    reg2 = reg[given_list[1]]['addr']
    reg3 = reg[given_list[2]]['addr']
    final = opcode1 + unused + reg1 + reg2 + reg3
    return final

def MoveImmediate(given_list : list):
    opcode1 = '10010'
    reg1 = reg[given_list[0]]['addr']
    imm = (given_list[1][1:])
    new = converter(imm)
    left = 8-len(new)
    unused = ''
    for i in range(left):
        unused = unused + '0'
    final = opcode1 + reg1 + unused + new
    return final

def MoveRegister(given_list : list):
    opcode1 = opcode['mov']['opcode']
    unused = '00000'
    reg1 = reg[given_list[0]]['addr']
    reg2 = reg[given_list[1]]['addr']
    final = opcode1 + unused + reg1 + reg2
    return final

def Multiply(given_list : list):
    opcode1 = opcode['mul']['opcode']
    unused = '00'
    reg1 = reg[given_list[0]]['addr']
    reg2 = reg[given_list[1]]['addr']
    reg3 = reg[given_list[2]]['addr']
    final = opcode1 + unused + reg1 + reg2 + reg3
    return final

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

def Load(given_list : list,memory):
    opcode1 = opcode['ld']['opcode']
    reg1 = reg[given_list[0]]['addr']
    memory = str(memory)
    final = opcode1 + reg1 + memory
    return final

def Store(given_list : list,memory):
    opcode1 = opcode['st']['opcode']
    reg1 = reg[given_list[0]]['addr']
    memory = str(memory)
    final = opcode1 + reg1 + memory
    return final

def UnconditionalJump(given_list : list,memory):
    opcode1 = opcode['jmp']['opcode']
    unused = '000'
    memory = str(memory)
    final = opcode1 + unused + memory
    return final

def JumpIfLessThan(given_list : list,memory):
    opcode1 = opcode['jlt']['opcode']
    unused = '000'
    memory = str(memory)
    final = opcode1 + unused + memory
    return final

def JumpIfgreaterThan(given_list : list,memory):
    opcode1 = opcode['jgt']['opcode']
    unused = '000'
    memory = str(memory)
    final = opcode1 + unused + memory
    return final

def JumpIfEqual(given_list : list,memory):
    opcode1 = opcode['je']['opcode']
    unused = '000'
    memory = str(memory)
    final = opcode1 + unused + memory
    return final

def halt():
    return '0101000000000000'
