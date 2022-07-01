import sys

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
    'var': {'type' : 'var'},
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
    'var':2,
    'A': 4,
    'B': 3,
    'C': 3,
    'D': 3,
    'E': 2,
    'F': 1,
    
}

errors={'0':'Instruction Name is Invalid!',
       '1':'Register Name is Invalid!',
       '2':'Punctuation Error (except ":" and "$")!',
       '3':'"$" symbol in Instruction (other than MOV)!',
       '4':'"$" symbol is not followed by an immediate numerical value!',
       '5':'Encoding Type Error!',
       '6':'Variables not declared at Beginning!',
       '7':'Variables not defined!',
       '8':'Labels not defined!',
       '9':'Redefining Labels (changing already defined labels)!',
       '10':'Redefining Variables (changing pre-existing variables)!',
       '11':'Illegal Interchange of Labels and Variables!',
       '12':'Illegal use of Flags!',
       '13':'Immediate Value is not an Integer(Whole Number)!',
       '14':'Immediate Value is not in range [0,255]',
       '15':'Halt Instruction is called In-between the program!',
       '16':'Missing Halt Instruction in the program!',
       '17':'":" in wrong position in definition of Labels!',
       '18': 'No. of parameters not valid!',
       '20': '"$" missing in definition of immediate!',
       'general':'general syntax error'}

var = dict()
labels = dict()

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


def Symbolerror(new_line: str):
    symbols = '!@#%^&*()_+-=~`{}[];"\'<>,.?/\|'
    for i in symbols:
        if i in new_line:
            print(errors['2'])
            exit()

def dollarColon(new_line: str):
    new_list = [i for i in new_line.split(' ')]
    flag=0
    if ':' and '$' in new_line:
        flag = 1
    elif ':' in new_line:
        flag =2
    elif '$' in new_line:
        flag = 3

    if flag==0:
        pass
    elif flag==1:
        if ':' not in new_list[0] or new_list[0][-1]!=':':
            print(errors['17'])
            exit()
        instr = new_list[1]
        if instr in opcode:
            if opcode[instr]['type'] != 'B':
                print(errors['20'])
                exit()
        if '$' not in new_list[-1] or new_list[-1][0]!='$' or not(new_list[-1][1:].isnumeric()) or not(255>=int(new_list[-1][1:])>=0):
            print(errors['20'])
            exit()
        elif flag==2:
            if ':' not in new_list[0] or new_list[0][-1]!=':':
                print(errors['17'])
                exit()
        elif flag ==3:
            instr = new_list[0]
            if instr in opcode:
                if opcode[instr]['type'] != 'B':
                    print(errors['20'])
                    exit()
            if '$' not in new_list[-1] or new_list[-1][0]!='$' or not(new_list[-1][1:].isnumeric()) or not(255>=int(new_list[-1][1:])>=0):
                print(errors['20'])
                exit()

def check_4_flags(instr, param_list):
    if len(param_list)>1 and param_list[1] in reg:
        if instr!='mov' and 'FLAGS' not in param_list:
            pass
        elif instr!='mov' and 'FLAGS' in param_list:
            print(errors['12'])
            exit()
        elif instr=='mov' and 'FLAGS' not in param_list:
            pass
        elif instr=='mov' and 'FLAGS'==param_list[0]:
            pass
        elif instr=='mov' and 'FLAGS'==param_list[1]:
            print(errors['12'])
            exit()
        elif instr=='FLAGS':
            print(errors['12'])
            exit()
    else:
        print('Either ' + errors['19'] + ' or ' + errors['1'])
        exit()


def lengthcheck_and_nameinvalid(new_line :str):
    new_list = [i for i in new_line.split(' ')]
    if new_list[0] in opcode:
        if len(new_list)!=inputlengtherror[opcode[new_list[0]]['type']]:
            print(errors['18'])
            exit()
    else:
        print(errors['0'])
        exit()

def main():
    prog = [i.strip() for i in sys.stdin.read().split('\n')]

    vars = dict()
    labels = dict()
    instructions = []

    is_var = 1

    counter = 0

    for line in prog:
        Symbolerror(line)

        line = line.split(' ')
        # print(line)
        
        # Var check
        if line[0] == 'var':
            if is_var == 0:
                print('6')
                exit()
            else:
                if len(line) == 2 and line[1].isalnum():       # Var check
                    var_name = line[1]

                    if var_name in vars:
                        print('10')
                        exit()    # Redefine vars

                    vars[line[1]] = 0
                    continue
                else:
                    print('general')
                    exit()

        # Label check
        if ':' in " ".join(line):
            if ':' not in line[0] or ':' != line[0][-1]:
                print('17')
                exit()    # : at wrong pos
            if ':' in ' '.join(line[1:]):
                print('9')
                exit()    # label redefined
            if len(line[0]) <= 1:
                print('8')
                exit()    # empty label

            label_name = line[0][:-1]
            if not label_name.isalnum():
                print('8')
                exit()    # Invalid label name

            if label_name in labels:
                print('9')
                exit()    # redefine lables

            labels[label_name] = counter
            counter += 1
            instructions.append(line[1:])
            continue

        # Blank Line
        if line == '\n':
            continue

        # Invalid instr
        # if line[0] not in opcode:
        #     print('0')
        #     exit()

        instructions.append(line)
        counter += 1

    for v in vars:
        vars[v] = counter
        counter += 1

def check_params(instr, param_list):
    type = opcode[instr]['type']

    if type == 'A':
        for i in range(len(param_list)):
            if param_list[i] not in reg or param_list[i] == 'FLAGS':
                print(errors["1"])
                exit()

    elif type == 'B':
        if param_list[0] not in reg or param_list[0] == 'FLAGS':
            print(errors["1"])
            exit()

        if '$' not in param_list[1]:
            print(errors['20'])
            exit()

        if len(param_list[1]) <= 1:
            print(errors['4'])
            exit()
        
        imm = eval(param_list[1][1:])

        if type(imm) != int:
            print(errors['13'])
            exit()

        if imm > 255 or imm < 0:
            print(errors['14'])
            exit()

    elif type == 'C':
        for i in range(len(param_list)):
            if param_list[i] not in reg:
                print(errors["1"])
                exit()
            if param_list[1] == 'FLAGS':
                print(errors['12'])
        
    elif type == 'D':
        if param_list[0] not in reg or param_list[0] == 'FLAGS':
            print(errors["1"])
            exit()
        
        arg = param_list[1]

        if arg not in vars:
            if arg in labels:
                print(errors['11'])
                exit()
            else:
                print(errors['7'])
                exit()

    elif type == 'E':
        arg = param_list[0]

        if arg not in labels:
            if arg in vars:
                print(errors['11'])
                exit()
            else:
                print(errors['8'])
                exit()


main()
