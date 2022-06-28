from ISA_Sachin import opcode, reg

errors = dict()
vars = dict()
labels = dict()

# Not checking for halt

def check_params(instr, param_list):
    type = opcode[instr]['type']

    if type == 'A':
        np = 3

        if len(param_list) > np:
            print(errors['18'])
            exit(1)
        
        if len(param_list) < np:
            print(errors["19"])
            exit(1)
        
        for i in range(np):
            if param_list[i] not in reg:
                print(errors["1"])
                exit(1)
        
    elif type == 'B':
        np = 2
        
        if len(param_list) > np:
            print(errors['18'])
            exit(1)
        
        if len(param_list) < np:
            print(errors["19"])
            exit(1)
        
        if param_list[0] not in reg:
            print(errors["1"])
            exit(1)

        if '$' not in param_list[1]:
            print(errors[20])
            exit(1)

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
        np = 2

        if len(param_list) > np:
            print(errors['18'])
            exit(1)
        
        if len(param_list) < np:
            print(errors["19"])
            exit(1)
        
        for i in range(np):
            if param_list[0] not in reg:
                print(errors["1"])
                exit(1)
        
    elif type == 'D':
        np = 2

        if len(param_list) > np:
            print(errors['18'])
            exit(1)
        
        if len(param_list) < np:
            print(errors["19"])
            exit(1)
        
        if param_list[0] not in reg:
            print(errors["1"])
            exit(1)
        
        arg = param_list[1]

        if arg not in vars:
            if arg in labels:       # uncomment only if labels dict complete till its call
                print(errors['11'])
                exit(1)
            else:
                print(errors['7'])
                exit()

    elif type == 'E':
        np = 1

        if len(param_list) > np:
            print(errors['18'])
            exit(1)
        
        if len(param_list) < np:
            print(errors["19"])
            exit(1)

        arg = param_list[0]

        if arg not in labels:       # Uncomment full block if labels dict complete till its call
            if arg in vars:
                print(errors['11'])
                exit(1)
            else:
                print(errors['8'])
                exit(1)


