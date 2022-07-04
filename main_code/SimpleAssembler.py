import sys

opcode = {
    'var': {'type': 'var'},
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

instr_length = {
    'var': 2,
    'A': 4,
    'B': 3,
    'C': 3,
    'D': 3,
    'E': 2,
    'F': 1,

}

errors = {'0': 'Instruction Name is Invalid!',
          '1': 'Register Name is Invalid!',
          '2': 'Punctuation Error (except ":" and "$")!',
          '3': '"$" symbol in Instruction (other than type B)!',
          '4': '"$" symbol is not followed by an immediate numerical value!',
          '5': 'Label is empty!',
          '6': 'Variables not declared at Beginning!',
          '7': 'Variables not defined!',
          '8': 'Labels not defined!',
          '9': 'Redefining Labels (changing already defined labels)!',
          '10': 'Redefining Variables (changing pre-existing variables)!',
          '11': 'Illegal Interchange of Labels and Variables!',
          '12': 'Illegal use of Flags!',
          '13': 'Immediate Value is not an Integer(Whole Number)!',
          '14': 'Immediate Value is not in range [0,255]',
          '15': 'Halt Instruction is called In-between the program!',
          '16': 'Halt instruction not at last line!',
          '17': '":" in wrong position in definition of Labels!',
          '18': 'No. of parameters not valid!',
          '20': '"$" missing in definition of immediate!',
          'general': 'general syntax error'}

variables = dict()
labels = dict()
instructions = []

counter_raw = 0     # first incre to begin from line 1
pc = 0

# pc changes after exec of instr => pc shows current line index, not that of next line

var_flag = 1
error_flag = False


def converter(num1, A=10, B=2):
    tot = 0
    digit = [i for i in num1]
    digit.reverse()
    for val in range(len(digit)):
        if digit[val].isalpha():
            pos = ord(digit[val]) - 55
            tot += (A**val)*pos
        else:
            tot += int(digit[val])*(A**val)
    l = []
    a2 = tot
    while a2 > 0:
        a1 = tot % B
        a2 = tot//B
        tot = a2
        l.append(a1)
    l2 = []
    for converter in l:
        if converter > 9:
            l2.append(chr(converter-10 + 65))
        else:
            l2.append(converter)
    l2 = [str(num1) for num1 in l2]
    l2.reverse()
    finalnum = "".join(l2)
    return finalnum


def Addition(given_list: list):
    opcode1 = opcode['add']['opcode']
    unused = '00'
    reg1 = reg[given_list[0]]['addr']
    reg2 = reg[given_list[1]]['addr']
    reg3 = reg[given_list[2]]['addr']
    final = opcode1 + unused + reg1 + reg2 + reg3
    return final


def Subtraction(given_list: list):
    opcode1 = opcode['sub']['opcode']
    unused = '00'
    reg1 = reg[given_list[0]]['addr']
    reg2 = reg[given_list[1]]['addr']
    reg3 = reg[given_list[2]]['addr']
    final = opcode1 + unused + reg1 + reg2 + reg3
    return final


def MoveImmediate(given_list: list):
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


def MoveRegister(given_list: list):
    opcode1 = opcode['mov']['opcode']
    unused = '00000'
    reg1 = reg[given_list[0]]['addr']
    reg2 = reg[given_list[1]]['addr']
    final = opcode1 + unused + reg1 + reg2
    return final


def Multiply(given_list: list):
    opcode1 = opcode['mul']['opcode']
    unused = '00'
    reg1 = reg[given_list[0]]['addr']
    reg2 = reg[given_list[1]]['addr']
    reg3 = reg[given_list[2]]['addr']
    final = opcode1 + unused + reg1 + reg2 + reg3
    return final


def Divide(given_list: list):
    opcode1 = opcode['div']['opcode']
    unused = '00000'
    reg1 = reg[given_list[0]]['addr']
    reg2 = reg[given_list[1]]['addr']
    final = opcode1 + unused + reg1 + reg2
    return final


def Rightshift(given_list: list):
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


def Leftshift(given_list: list):
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


def Exclusiveor(given_list: list):
    opcode1 = opcode['xor']['opcode']
    unused = '00'
    reg1 = reg[given_list[0]]['addr']
    reg2 = reg[given_list[1]]['addr']
    reg3 = reg[given_list[2]]['addr']
    final = opcode1 + unused + reg1 + reg2 + reg3
    return final


def Or(given_list: list):
    opcode1 = opcode['or']['opcode']
    unused = '00'
    reg1 = reg[given_list[0]]['addr']
    reg2 = reg[given_list[1]]['addr']
    reg3 = reg[given_list[2]]['addr']
    final = opcode1 + unused + reg1 + reg2 + reg3
    return final


def And(given_list: list):
    opcode1 = opcode['and']['opcode']
    unused = '00'
    reg1 = reg[given_list[0]]['addr']
    reg2 = reg[given_list[1]]['addr']
    reg3 = reg[given_list[2]]['addr']
    final = opcode1 + unused + reg1 + reg2 + reg3
    return final


def Invert(given_list: list):
    opcode1 = opcode['not']['opcode']
    unused = '00000'
    reg1 = reg[given_list[0]]['addr']
    reg2 = reg[given_list[1]]['addr']
    final = opcode1 + unused + reg1 + reg2
    return final


def Compare(given_list: list):
    opcode1 = opcode['cmp']['opcode']
    unused = '00000'
    reg1 = reg[given_list[0]]['addr']
    reg2 = reg[given_list[1]]['addr']
    final = opcode1 + unused + reg1 + reg2
    return final


def Load(given_list: list, memory):
    opcode1 = opcode['ld']['opcode']
    reg1 = reg[given_list[0]]['addr']
    left = 8-len(memory)
    unused = ''
    for i in range(left):
        unused = unused + '0'
    final = opcode1 + reg1 + unused + memory
    return final


def Store(given_list: list, memory):
    opcode1 = opcode['st']['opcode']
    reg1 = reg[given_list[0]]['addr']
    left = 8-len(memory)
    unused = ''
    for i in range(left):
        unused = unused + '0'
    final = opcode1 + reg1 + unused + memory
    return final


def UnconditionalJump(given_list: list, memory):
    opcode1 = opcode['jmp']['opcode']
    unused = '000'
    left = 8-len(memory)
    for i in range(left):
        unused = unused + '0'
    final = opcode1 + unused + memory
    return final


def JumpIfLessThan(given_list: list, memory):
    opcode1 = opcode['jlt']['opcode']
    unused = '000'
    left = 8-len(memory)
    for i in range(left):
        unused = unused + '0'
    final = opcode1 + unused + memory
    return final


def JumpIfgreaterThan(given_list: list, memory):
    opcode1 = opcode['jgt']['opcode']
    unused = '000'
    left = 8-len(memory)
    for i in range(left):
        unused = unused + '0'
    final = opcode1 + unused + memory
    return final


def JumpIfEqual(given_list: list, memory):
    opcode1 = opcode['je']['opcode']
    unused = '000'
    left = 8-len(memory)
    for i in range(left):
        unused = unused + '0'
    final = opcode1 + unused + memory
    return final


def halt():
    return '0101000000000000'


def print_binary(error_flag):
    if not error_flag:

        for line in instructions:

            if line[0] == 'add':
                print(Addition(line[1:]))

            elif line[0] == 'sub':
                print(Subtraction(line[1:]))

            elif line[0] == 'mov' and '$' in line[2]:
                print(MoveImmediate(line[1:]))

            elif line[0] == 'mov':
                print(MoveRegister(line[1:]))

            elif line[0] == 'mul':
                print(Multiply(line[1:]))

            elif line[0] == 'div':
                print(Divide(line[1:]))

            elif line[0] == 'rs':
                print(Rightshift(line[1:]))

            elif line[0] == 'ls':
                print(Leftshift(line[1:]))

            elif line[0] == 'xor':
                print(Exclusiveor(line[1:]))

            elif line[0] == 'or':
                print(Or(line[1:]))

            elif line[0] == 'and':
                print(And(line[1:]))

            elif line[0] == 'not':
                print(Invert(line[1:]))

            elif line[0] == 'cmp':
                print(Compare(line[1:]))

            elif line[0] == 'ld':
                print(Load(line[1:], converter(str(variables[line[2]]))))

            elif line[0] == 'st':
                print(Store(line[1:], converter(str(variables[line[2]]))))

            elif line[0] == 'jmp':
                print(UnconditionalJump(
                    line[1:], converter(str(labels[line[1]]))))

            elif line[0] == 'jlt':
                print(JumpIfLessThan(line[1:], converter(
                    str(labels[line[1]]))))

            elif line[0] == 'jgt':
                print(JumpIfgreaterThan(
                    line[1:], converter(str(labels[line[1]]))))

            elif line[0] == 'je':
                print(JumpIfEqual(line[1:], converter(
                    str(labels[line[1]]))))

            elif line[0] == 'hlt':
                print('0101000000000000')


def has_symbol_error(line: str) -> bool:
    symbols = '!@#%^&*()_+-=~`{}[];"\'<>,.?/\|'
    for i in symbols:
        if i in line:
            print(f'ERROR: (Line {counter_raw})', errors['2'])
            return True
    return False


def has_length_or_name_error(line):
    if line[0] in opcode:
        instr = line[0]

        if len(line) != instr_length[opcode[instr]['type']]:
            print(f'ERROR: (Line {counter_raw})', errors['18'])
            return True

        else:
            return False

    else:
        if '\t' in ' '.join(line):
            print(f'ERROR: (Line {counter_raw})', errors['general'])
            return True

        # print(line[0])
        print(f'ERROR: (Line {counter_raw})', errors['0'])
        return True


def is_register(param):
    global reg

    if param in reg:
        return True
    else:
        return False


def is_flags(param):
    if param == 'FLAGS':
        return True
    else:
        return False


def has_var_error(v):
    if v in variables:
        return False

    else:
        if v in labels:
            print(f'ERROR: (Line {counter_raw})', errors['11'])
            return True
        else:
            print(f'ERROR: (Line {counter_raw})', errors['7'])
            return True


def has_label_error(l):
    if l in labels:
        return False

    else:
        if l in variables:
            print(f'ERROR: (Line {counter_raw})', errors['11'])
            return True
        else:
            print(f'ERROR: (Line {counter_raw})', errors['8'])
            return True


def has_imm_error(arg):
    if '$' not in arg:                  # arg must have $
        print(f'ERROR: (Line {counter_raw})', errors['20'])
        return True

    if len(arg) <= 1:                   # imm empty
        print(f'ERROR: (Line {counter_raw})', errors['4'])
        return True

    imm = eval(arg[1:])

    if type(imm) != int:                # imm must be int
        print(f'ERROR: (Line {counter_raw})', errors['13'])
        return True

    if imm > 255 or imm < 0:            # imm out of range
        print(f'ERROR: (Line {counter_raw})', errors['14'])
        return True

    return False


def has_param_error(instr, param_list):
    type = opcode[instr]['type']

    if instr == 'mov' and '$' in ' '.join(param_list):
        type = chr(ord(type)-1)

    if type == 'A':

        for arg in param_list:
            if is_register(arg):
                if is_flags(arg):               # illegal use of flags
                    print(f'ERROR: (Line {counter_raw})', errors['12'])
                    return True

                else:
                    pass

            else:                               # arg must be a reg
                print(f'ERROR: (Line {counter_raw})', errors['1'])
                return True

        return False

# ----------------------------------------------------------------------------------------

    elif type == 'B':

        arg1 = param_list[0]
        arg2 = param_list[1]

        if not is_register(arg1):               # arg1 must be reg
            print(f'ERROR: (Line {counter_raw})', errors["1"])
            return True

        if is_flags(arg1):                      # illegal use of flags
            print(f'ERROR: (Line {counter_raw})', errors['12'])
            return True

        # check if imm is correct
        if has_imm_error(arg2):
            return True

        return False

# ----------------------------------------------------------------------------------------

    elif type == 'C':

        if instr == 'mov':
            for arg in param_list:
                if not is_register(arg):         # all args must be regs
                    print(f'ERROR: (Line {counter_raw})', errors["1"])
                    return True

            arg2 = param_list[1]

            if is_flags(arg2):                   # FLAGS must be arg1 in mov
                print(f'ERROR: (Line {counter_raw})', errors['12'])
                return True

        else:
            for arg in param_list:               # all args must be regs
                if not is_register(arg):
                    print(f'ERROR: (Line {counter_raw})', errors["1"])
                    return True

                if is_flags(arg):                # illegal use of flags
                    print(f'ERROR: (Line {counter_raw})', errors['12'])
                    return True

        return False

# ----------------------------------------------------------------------------------------

    elif type == 'D':

        arg1 = param_list[0]
        arg2 = param_list[1]

        if not is_register(arg1):               # arg1 must be reg
            print(f'ERROR: (Line {counter_raw})', errors["1"])
            return True

        if is_flags(arg1):                      # illegal use of flags
            print(f'ERROR: (Line {counter_raw})', errors['12'])
            return True

        if has_var_error(arg2):                   # check if var is correct
            return True

        return False

# ----------------------------------------------------------------------------------------

    elif type == 'E':

        arg = param_list[0]
        if has_label_error(arg):                  # check if label is correct
            return True

        return False


def err_check(line):
    global counter_raw, pc, var_flag

    if line == '':
        return False

    if has_symbol_error(line):
        return True

    line = line.split(' ')

    # Var check
    if line[0] == 'var':
        # counter_raw += 1

        if var_flag == 0:
            print(f'ERROR: (Line {counter_raw})', errors['6'])
            return True

        else:
            if len(line) == 2 and line[1].isalnum():        # Var check
                var_name = line[1]

                if var_name in variables:                   # Redefine var
                    print(f'ERROR: (Line {counter_raw})', errors['10'])
                    return True

                variables[line[1]] = 0
                return False

            else:
                print(f'ERROR: (Line {counter_raw})', errors['general'])
                return True

    if 'var' in line[0]:
        print(f'ERROR: (Line {counter_raw})', errors['general'])
        return True
        

    var_flag = 0

    # Label check
    if ':' in ' '.join(line):
        # counter_raw += 1

        if ':' not in line[0] or ':' != line[0][-1]:
            print(f'ERROR: (Line {counter_raw})', errors['17'])
            return True                                    # : at wrong pos

        if ':' in ' '.join(line[1:]):
            print(f'ERROR: (Line {counter_raw})', errors['9'])
            return True                                    # label redefined

        if len(line[0]) <= 1:
            print(f'ERROR: (Line {counter_raw})', errors['8'])
            return True                                    # empty label

        label_name = line[0][:-1]

        if not label_name.isalnum():                       # Invalid label name
            print(f'ERROR: (Line {counter_raw})', errors['8'])
            return True

        if label_name in labels:
            print(f'ERROR: (Line {counter_raw})', errors['9'])
            return True                                   # redefine lables

        if len(line) == 1:                           # Empty label
            print(f'ERROR: (Line {counter_raw})', errors['5'])
            return True

        labels[label_name] = pc
        line = line[1:]

    if has_length_or_name_error(line):
        # counter_raw += 1
        return True

    if has_param_error(line[0], line[1:]):
        return True

    instructions.append(line)
    # counter_raw += 1
    pc += 1
    return False


def main():
    prog = [i.strip() for i in sys.stdin.read().split('\n')]
    # print()     # Comment for final run

    global counter_raw, pc, error_flag
    error_flag = False

    for line in prog:
        counter_raw += 1

        if err_check(line):
            error_flag = True
            continue

    for v in variables:
        variables[v] = pc
        pc += 1

    if instructions[-1] != ['hlt']:
        print(f'ERROR:', errors['16'])
        error_flag = True

    else:
        for line in instructions[:-1]:
            if 'hlt' in line:
                idx = prog.index(' '.join(line))
                print(f'ERROR: (Line {idx+1})', errors['15'])
                error_flag = True

    print_binary(error_flag)
    # print()


main()
