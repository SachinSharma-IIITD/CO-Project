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
