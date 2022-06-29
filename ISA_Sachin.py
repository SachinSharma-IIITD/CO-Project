# If an instr doesn't affect FLAGS reg, then it is reset to 0 => Value in FLAGS reg remains just for 1 execution
# Eg -  instr 1 -> sets a flag in FLAGS reg
#       intr 2 -> doesn't affect FLAGS -> FlAg value is set till its execution
#       FLAGS reset

# Therfore, FLAGS stores content of prev intr

# Data in file reg is 16 bit long (all bits usable)

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

var = dict()
label = dict()


def flag_overflow(set: bool):
    if set:
        reg['FLAGS']['data'][-4] = 1
    else:
        reg['FLAGS']['data'][-4] = 0
    return


def flag_less_than(set: bool):
    if set:
        reg['FLAGS']['data'][-3] = 1
    else:
        reg['FLAGS']['data'][-3] = 0
    return


def flag_greater_than(set: bool):
    if set:
        reg['FLAGS']['data'][-2] = 1
    else:
        reg['FLAGS']['data'][-2] = 0
    return


def flag_equal(set: bool):
    if set:
        reg['FLAGS']['data'][-1] = 1
    else:
        reg['FLAGS']['data'][-1] = 0
    return


def reset_flags():
    reg['FLAGS']['data'] = [0 for i in range(16)]


def assign_var(var_name: str, value: int):      # Call this function for each var
    var[var_name] = value
    return


def read_reg(reg: str) -> int:
    return int(reg[reg]['data'])


def write_to_reg(dest: str, val: int):
    reg[dest]['data'] = val
    return


def read_memory(addr: str) -> int:
    return var[addr]


def write_to_memory(addr: str, data: int):
    var[addr] = data
    return


def addition(param_list: list):
    src1 = read_reg(param_list[0])   # Reg1 data
    src2 = read_reg(param_list[1])   # Reg2 data
    dest = param_list[2]             # Reg3 name

    sum = src1 + src2

    if sum >= pow(2, 16):       # Overflow
        flag_overflow(True)
        sum = 0
    else:
        flag_overflow(False)

    write_to_reg(dest, sum)
    return


def subtraction(param_list: list):
    src1 = read_reg(param_list[0])      # Reg1 data
    src2 = read_reg(param_list[1])      # Reg2 data
    dest = param_list[2]                # Reg3 name

    diff = src1 - src2

    if diff < 0:  # Overflow
        flag_overflow(True)
        diff = 0
    else:
        flag_overflow(False)

    write_to_reg(dest, diff)
    return


def multiply(param_list: list):
    src1 = read_reg(param_list[0])      # Reg1 data
    src2 = read_reg(param_list[1])      # Reg2 data
    dest = param_list[2]                # Reg3 name

    prod = src1 * src2

    if prod >= pow(2, 16):      # Overflow
        flag_overflow(True)
        prod = 0
    else:
        flag_overflow(False)

    write_to_reg(dest, prod)
    return


def move_imm(param_list: list):
    imm = int(param_list[1])        # imm
    dest = param_list[0]            # Reg name

    write_to_reg(dest, imm)
    reset_flags()
    return


def move_reg(param_list: list):
    src = read_reg(param_list[0])
    dest = param_list[1]

    write_to_reg(dest, src)
    reset_flags()
    return


def load(param_list: list):
    addr = param_list[1]            # Param 2 is mem_addr, which is a var
    data = read_memory(addr)        # so value of var in var dict is data
    dest = param_list[0]

    write_to_reg(dest, data)
    reset_flags()
    return


def store(param_list: list):
    addr = param_list[1]
    data = read_reg(param_list[0])

    write_to_memory(addr, data)
    reset_flags()
    return
