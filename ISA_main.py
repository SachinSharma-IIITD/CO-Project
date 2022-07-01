import sys
from error import Symbolerror
from FinalAboveMain import opcode


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


main()
