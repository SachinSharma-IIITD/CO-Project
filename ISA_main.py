from msilib.schema import Error
import sys
from error import Symbolerror
from FinalAboveMain import opcode

prog = [i.strip() for i in sys.stdin.read().split('\n')]

vars = dict()
labels = dict()
instructions = []

is_var = 1

counter = 0

for line in prog:
    Symbolerror(line)

    line = line.split(' ')

    # Var check
    if line[0] == 'var':
        if is_var == 0:
            raise(Error)
        else:
            if len(line) == 2 and line[1].isalnum():       # Var check
                var_name = line[1]
                
                if var_name in vars:
                    raise(Error)    # Redefine vars

                vars[line[1]] = 0
                continue
            else:
                raise(Error)

    # Label check
    if ':' in line:
        if ':' not in line[0] or ':' != line[0][-1]:
            raise(Error)    # : at wrong pos
        if ':' in line[1:]:
            raise(Error)    # label redefined
        if len(line[0]) <= 1:
            raise(Error)    # empty label

        label_name = line[0][:-1]
        if not label_name.isalnum():
            raise(Error)    # Invalid label name
        
        if label_name in labels:
            raise(Error)    # redefine lables
            
        labels[label_name] = counter
        counter += 1
        instructions.append(line[1:])
        continue

    # Blank Line
    if line == '\n':
        continue
    
    # Invalid instr
    if line[0] not in opcode:
        raise(Error)
    
    instructions.append(line)
    counter += 1

for v in vars:
    vars[v] = counter
    counter += 1