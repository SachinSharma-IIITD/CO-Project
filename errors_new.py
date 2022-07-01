def symbolError(new_line: str):
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
        if ':' not in new_list[0] and new_list[0][-1]!=':':
            print(errors['17'])
            exit()
        instr = new_list[1]
        if instr in opcode:
            if opcode[instr]['type'] != 'B':
                print(errors['20'])
                exit()
        if '$' not in new_list[-1] and new_list[-1][0]!='$' and not(new_list[-1][1:].isnumeric()) and not(255>=int(new_list[-1][1:])>=0):
            print(errors['20'])
            exit()
        elif flag==2:
            if ':' not in new_list[0] and new_list[0][-1]!=':':
                print(errors['17'])
                exit()
        elif flag ==3:
            instr = new_list[0]
            if instr in opcode:
                if opcode[instr]['type'] != 'B':
                    print(errors['20'])
                    exit()
            if '$' not in new_list[-1] and new_list[-1][0]!='$' and not(new_list[-1][1:].isnumeric()) and not(255>=int(new_list[-1][1:])>=0):
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
            print(errors('18'))
            exit()
    else:
        print(errors('0'))
        exit()
