from ISA_Sachin import opcode, reg

errors = dict()
vars = dict()
labels = dict()

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


