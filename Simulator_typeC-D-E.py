def execute_c(reg1, reg2):
    if instr=='movr':
        reg_data[reg2]=reg_data[reg1]

    elif instr=='div':
        if reg_data[reg2]!=0:
            reg_data['r0']=reg_data[reg1]//reg_data[reg2]
            reg_data['r1']=reg_data[reg1]%reg_data[reg2]
        else:
            pass
    elif instr=='not':
        reg_data[reg2]= ~reg_data[reg1]
    elif instr=='cmp':
        if(reg_data[reg1]==reg_data[reg2]):
            reg_data['flags'][-1]='1'
            reg_data['flags'][-2]='0'
            reg_data['flags'][-3]='0'
        elif(reg_data[reg1]>reg_data[reg2]):
            reg_data['flags'][-2]='1'
            reg_data['flags'][-1]='0'
            reg_data['flags'][-3]='0'
        elif(reg_data[reg1]<reg_data[reg2]):
            reg_data['flags'][-3]='1'
            reg_data['flags'][-2]='0'
            reg_data['flags'][-1]='0'
    return True

def execute_d(memory_addr,reg1):
    global memory
    if instr=='ld':
        reg_data[reg1]=memory[memory_addr]
    elif instr=='st':
        memory[memory_addr]=reg_data[reg1]
    return True


def execute_e(reg1,label):
    global pc
    if instr=='jmp':
        pc=label
    elif instr=='jlt':
        if(reg_data['flags'][-3]=='1'):
            pc=label
    elif instr=='jgt':
        if(reg_data['flags'][-2]=='1'):
            pc=label
    elif instr=='je':
        if(reg_data['flags'][-1]=='1'):
            pc=label
    return True
