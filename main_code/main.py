import sys
from globals import *


def has_symbol_error(line: str) -> bool:
    symbols = '!@#%^&*()_+-=~`{}[];"\'<>,.?/\|'
    for i in symbols:
        if i in line:
            print(f'ERROR: (Line {counter_raw})', errors['2'])
            return True
    return False


def dollarColon(new_line: str):
    new_list = [i for i in new_line.split(' ')]
    flag = 0
    if ':' and '$' in new_line:
        flag = 1
    elif ':' in new_line:
        flag = 2
    elif '$' in new_line:
        flag = 3

    if flag == 0:
        pass
    elif flag == 1:
        if ':' not in new_list[0] or new_list[0][-1] != ':':
            print(f'ERROR: (Line {counter_raw})', errors['17'])
            return
        instr = new_list[1]
        if instr in opcode:
            if opcode[instr]['type'] != 'B':
                print(f'ERROR: (Line {counter_raw})', errors['20'])
                return
        if '$' not in new_list[-1] or new_list[-1][0] != '$' or not(new_list[-1][1:].isnumeric()) or not(255 >= int(new_list[-1][1:]) >= 0):
            print(f'ERROR: (Line {counter_raw})', errors['20'])
            return
        elif flag == 2:
            if ':' not in new_list[0] or new_list[0][-1] != ':':
                print(f'ERROR: (Line {counter_raw})', errors['17'])
                return
        elif flag == 3:
            instr = new_list[0]
            if instr in opcode:
                if opcode[instr]['type'] != 'B':
                    print(f'ERROR: (Line {counter_raw})', errors['20'])
                    return
            if '$' not in new_list[-1] or new_list[-1][0] != '$' or not(new_list[-1][1:].isnumeric()) or not(255 >= int(new_list[-1][1:]) >= 0):
                print(f'ERROR: (Line {counter_raw})', errors['20'])
                return


""" 
def check_4_flags(instr, param_list):
    if len(param_list)>1 and param_list[1] in reg:
        if instr!='mov' and 'FLAGS' not in param_list:
            pass
        elif instr!='mov' and 'FLAGS' in param_list:
            print(f'ERROR: (Line {counter_raw})', errors['12'])
            return
        elif instr=='mov' and 'FLAGS' not in param_list:
            pass
        elif instr=='mov' and 'FLAGS'==param_list[0]:
            pass
        elif instr=='mov' and 'FLAGS'==param_list[1]:
            print(f'ERROR: (Line {counter_raw})', errors['12'])
            return
        elif instr=='FLAGS':
            print(f'ERROR: (Line {counter_raw})', errors['12'])
            return
    else:
        print('Either ' + f'ERROR: (Line {counter_raw})', errors['19'] + ' or ' + f'ERROR: (Line {counter_raw})', errors['1'])
        return
 """


def has_length_or_name_error(line):
    if line[0] in opcode:
        instr = line[0]

        if len(line) != instr_length[opcode[instr]['type']]:
            print(f'ERROR: (Line {counter_raw})', errors['18'])
            return True

        else:
            return False

    else:
        print(f'ERROR: (Line {counter_raw})', errors['0'])
        return True


def is_register(param):
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

    if type == 'A':

        for arg in param_list:
            if is_register(arg):
                if is_flags(arg):               # illegal use of flags
                    print(f'ERROR: (Line {counter_raw})', errors['12'])
                    return True

                else:
                    return False

            else:                               # arg must be a reg
                print(f'ERROR: (Line {counter_raw})', errors['1'])
                return True

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

        arg2 = param_list[0]
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
                print(errors['general'])
                return True

    if 'var' in line[0]:
        print(f'ERROR: (Line {counter_raw})', errors['general'])
        return True

    # Blank Line
    if line == '\n':
        return False

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
    print()

    global counter_raw, pc

    for line in prog:
        counter_raw += 1

        if err_check(line):
            error_flag = 1

    for v in variables:
        variables[v] = pc
        pc += 1


main()
