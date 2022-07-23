from simulator import reg_data, memory

overflow_flag_pos = -4
less_flag_pos = -3
greater_flag_pos = -2
equal_flag_pos = -1


def reset_flags():
    reg_data['flags'][-1] = 0
    reg_data['flags'][-2] = 0
    reg_data['flags'][-3] = 0
    reg_data['flags'][-4] = 0


def set_overflow_flag():
    reset_flags()
    reg_data['flags'][overflow_flag_pos] = 1


def set_less_flag():
    reset_flags()
    reg_data['flags'][less_flag_pos] = 1


def set_greater_flag():
    reset_flags()
    reg_data['flags'][greater_flag_pos] = 1


def set_equal_flag():
    reset_flags()
    reg_data['flags'][equal_flag_pos] = 1


def Addition(reg1, reg2, reg3):
    global reg_data

    src1 = reg_data[reg1]
    src2 = reg_data[reg2]

    if src1 + src2 > 255:
        set_overflow_flag()
        reg_data[reg3] = 255

    else:
        reg_data[reg3] = src1 + src2
        reset_flags()


def Subtraction(reg1, reg2, reg3):
    src1 = reg_data[reg1]
    src2 = reg_data[reg2]

    if src2 > src1:
        set_overflow_flag()
        reg_data[reg3] = 0

    else:
        reg_data[reg3] = src1 - src2
        reset_flags()


def Multiply(reg1, reg2, reg3):
    src1 = reg_data[reg1]
    src2 = reg_data[reg2]

    if src1 * src2 > 255:
        set_overflow_flag()
        reg_data[reg3] = 255

    else:
        reg_data[reg3] = src1 * src2
        reset_flags()


def Xor(reg1, reg2, reg3):
    reg_data[reg3] = reg_data[reg1] ^ reg_data[reg2]
    reset_flags()


def Or(reg1, reg2, reg3):
    reg_data[reg3] = reg_data[reg1] | reg_data[reg2]
    reset_flags()


def And(reg1, reg2, reg3):
    reg_data[reg3] = reg_data[reg1] & reg_data[reg2]
    reset_flags()


def Movi(reg, imm):
    reg_data[reg] = imm
    reset_flags()


def LeftShift(reg, imm):
    reg_data[reg] <<= imm
    reset_flags()


def RightShift(reg, imm):
    reg_data[reg] >>= imm
    reset_flags()


def Movr(reg1, reg2):
    reg_data[reg2] = reg_data[reg1]
    reset_flags()


def Div(reg1, reg2):
    reset_flags()

    if reg_data[reg2] != 0:
        reg_data['r0'] = reg_data[reg1]//reg_data[reg2]
        reg_data['r1'] = reg_data[reg1] % reg_data[reg2]
    else:
        pass


def Not(reg1, reg2):
    reg_data[reg2] = ~reg_data[reg1]
    reset_flags()


def Cmp(reg1, reg2):
    if(reg_data[reg1] == reg_data[reg2]):
        set_equal_flag()

    elif(reg_data[reg1] > reg_data[reg2]):
        set_greater_flag()

    elif(reg_data[reg1] < reg_data[reg2]):
        set_less_flag()


def Load(reg, addr):
    reg_data[reg] = memory[addr]
    reset_flags()


def Store(reg, addr):
    memory[addr] = reg_data[reg]
    reset_flags()


def execute_a(instr, reg1, reg2, reg3):
    if instr == 'add':
        Addition(reg1, reg2, reg3)

    elif instr == 'sub':
        Subtraction(reg1, reg2, reg3)

    elif instr == 'mul':
        Multiply(reg1, reg2, reg3)

    elif instr == 'xor':
        Xor(reg1, reg2, reg3)

    elif instr == 'or':
        Or(reg1, reg2, reg3)

    elif instr == 'and':
        And(reg1, reg2, reg3)

    return


def execute_b(instr, reg, imm):
    if instr == 'movi':
        Movi(reg, imm)

    elif instr == 'ls':
        LeftShift(reg, imm)

    elif instr == 'rs':
        RightShift(reg, imm)


def execute_c(instr, reg1, reg2):
    if instr == 'movr':
        Movr(reg1, reg2)

    elif instr == 'div':
        Div(reg1, reg2)

    elif instr == 'not':
        Not(reg1, reg2)

    elif instr == 'cmp':
        Cmp(reg1, reg2)

    return True


def execute_d(instr, memory_addr, reg1):
    global memory

    if instr == 'ld':
        Load(reg1, memory_addr)

    elif instr == 'st':
        Store(reg1, memory_addr)

    return True


def execute_e(instr, label):
    global pc

    if instr == 'jmp':
        pc = label
        reset_flags()

    elif instr == 'jlt':
        if (reg_data['flags'][less_flag_pos] == '1'):
            pc = label
            reset_flags()

    elif instr == 'jgt':
        if (reg_data['flags'][greater_flag_pos] == '1'):
            pc = label
            reset_flags()

    elif instr == 'je':
        if (reg_data['flags'][equal_flag_pos] == '1'):
            pc = label
            reset_flags()

    return True
